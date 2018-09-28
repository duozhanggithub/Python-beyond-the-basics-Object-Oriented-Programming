import os


class ConfigKeyError(Exception):
    def __init__(self, ConfigDict, key_requested):
        self.ConfigDict = ConfigDict
        self.key_requested = key_requested
        self.key_exist = self.ConfigDict.keys()

    def __str__(self):
        return 'key (0) not found. Available keys: (1)'.format(self.key_requested, ','.join(self.key_exist))


class ConfigDict(dict):
    def __init__(self, file_name):
        self._file_name = file_name
        if not os.path.isfile(self._file_name):
            try:
                open(self._file_name, 'r').close()
            except IOError:
                raise IOError('file is not exists')

        if os.path.isfile(self._file_name):
            print('file exists')
            with open(self._file_name, 'r') as f:
                for line in f:
                    line = line.rstrip()
                    key, value = line.split('=',1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._file_name, 'a') as f:
            f.write("{0}={1}\n".format(key, value))

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

cd = ConfigDict('aa.txt')