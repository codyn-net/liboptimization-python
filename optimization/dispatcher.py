from optimization import taskreader
from optimization.messages import task_pb2 as task

import sys

class Dispatcher(taskreader.TaskReader):
    def __init__(self, instream=sys.stdin, outstream=sys.stdout):
        taskreader.TaskReader.__init__(self, instream)
        self._outstream = outstream

    def response(self, r):
        comm = task.Communication()

        comm.type = task.Communication.CommunicationResponse
        comm.response.CopyFrom(r)

        self._send_comm(comm)

        # Closing socket to flush, only one response can be send
        self._outstream.close()
        self._outstream = None

    def _send_comm(self, comm):
        if self._outstream is None:
            return

        d = comm.SerializeToString()

        self._outstream.write(str(len(d)))
        self._outstream.write(' ')
        self._outstream.write(d)
        self._outstream.flush()

    def respond(self, f, d={}):
        fitness = {}
        data = {}

        if isinstance(f, (float, int)):
            fitness = {'value': f}
        elif hasattr(f, '__getitem__'):
            fitness = f
        else:
            fitness = {'value': float(f)}

        r = task.Response()

        r.id = 0
        r.status = task.Response.Success

        for name in fitness:
            f = r.fitness.add()

            f.name = name
            f.value = fitness[name]

        for name in data:
            d = r.data.add()

            d.key = name
            d.value = data[name]

        self.response(r)

# vi:ts=4:et
