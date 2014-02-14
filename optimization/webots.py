from optimization.messages import task_pb2 as task
from optimization.dispatcher import Dispatcher

import warnings, os, socket, threading

class Webots(Dispatcher):
    class IOSocket:
        def __init__(self, s):
            self.s = s

        def read(self, bufsize):
            return self.s.recv(bufsize)

        def write(self, data):
            self.s.sendall(data)

        def flush(self):
            pass

        def close(self):
            self.s.close()

    def __init__(self):
        try:
            self._socket = self._connect()
        except:
            self._socket = None

        Dispatcher.__init__(self, instream=self._socket, outstream=self._socket)

        if self and not 'no-periodic-ping' in self.settings:
            self._setup_periodic_ping()

    def _setup_periodic_ping(self):
        self._periodic_ping_thread = threading.Thread(target=self._periodic_ping, name='periodic-ping')
        self._periodic_ping_thread.start()

    def _periodic_ping(self):
        while True:
            comm = task.Communication()

            comm.type = task.Communication.CommunicationPing
            comm.ping.id = self.id

            self._send_comm(comm)

            time.sleep(15)

    def _connect(self):
        usock = os.getenv('OPTIMIZATION_UNIX_SOCKET')

        if usock is None:
            return None

        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(usock)

        return Webots.IOSocket(s)

# vi:ts=4:et
