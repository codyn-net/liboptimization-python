from optimization.messages import task_pb2 as task

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
        except:
            return False

        try:
            l = int(l)
        except:
            return False

        # Skip space
        try:
            if self._stream.read(1) != ' ':
                return False
        except:
            return False

        # Read protobuf message
        try:
            msg = self._stream.read(l)
        except:
            return False

        try:
            comm = task.Communication.ParseFromString(msg)
        except:
            return False

        if comm.type != task.Communication.CommunicationTask:
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
