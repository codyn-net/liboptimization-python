from optimization.messages import task_pb2 as task
import warnings

class TaskReader:
    def __init__(self, stream=None):
        self._stream = stream
        self._settings_map = None
        self._parameters_map = None
        self._data_map = None

        if not self._stream is None:
            self._extract()

    def _extract(self):
        if self._stream is None:
            return False

        untilspace = iter(lambda: self._stream.read(1), ' ')

        try:
            l = ''.join(untilspace)
        except Exception as e:
            warnings.warn('Unable to read space: ' + str(e), RuntimeWarning)
            return False

        try:
            l = int(l)
        except Exception as e:
            warnings.warn('Could not parse message length: ' + str(e), RuntimeWarning)
            return False

        # Read protobuf message
        try:
            msg = self._stream.read(l)
        except Exception as e:
            warnings.warn('Could not read message: ' + str(e), RuntimeWarning)
            return False

        try:
            comm = task.Communication()
            comm.ParseFromString(msg)
        except Exception as e:
            warnings.warn('Could not parse message: ' + str(e), RuntimeWarning)
            return False

        if comm.type != task.Communication.CommunicationTask:
            warnings.warn('Message is not of type `task\'', RuntimeWarning)
            return False

        self._task = comm.task
        return True

    @property
    def id(self):
        return self._task.id

    @property
    def job(self):
        return self._task.job

    @property
    def dispatcher(self):
        return self._task.dispatcher

    @property
    def uniqueid(self):
        return self._task.uniqueid

    @property
    def settings(self):
        if self._settings_map is None:
            self._settings_map = {}

            for s in self._task.settings:
                self._settings_map[s.key] = s.value

        return self._settings_map

    @property
    def parameters(self):
        if self._parameters_map is None:
            self._parameters_map = {}

            for s in self._task.parameters:
                self._parameters_map[s.name] = s

        return self._parameters_map

    @property
    def data(self):
        if self._data_map is None:
            self._data_map = {}

            for s in self._task.data:
                self._data_map[s.key] = s.value

        return self._data_map

# vi:ts=4:et
