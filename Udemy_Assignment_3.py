import os

class ConfigFile(dict):
    def __init__(self, file_name):
        self._file_name = file_name

        if os.path.isfile(self._file_name):
            print('file exists')
            with open(self._file_name, 'r') as f:
                for line in f:
                    line = line.rstrip()
                    key, value = line.split('=',1)
                    dict.__setitem__(self, key, value)
        else:
            print('file is not exists')

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)

        with open(self._file_name, 'a') as f:
            f.write("{0}={1}\n".format(key, value))

dd = ConfigFile('Assignment3.txt')

dd['e'] = 5
dd['f'] = 6

for key in dd.keys():
    print("{0}={1}\n".format(key, dd[key]))

print(dd['e'])
print(dd['f'])

dd['g']=7

print(dd)
