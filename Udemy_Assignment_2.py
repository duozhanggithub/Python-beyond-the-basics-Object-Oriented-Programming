import datetime
import abc

dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

class WriteFile(object):

    def __init__(self, file_name):
        self.file_name = file_name

    __metaclass__ =abc.ABCMeta
    @abc.abstractmethod
    def write(self):
        return

    def write_line(self, text):
        fh = open(self.file_name, 'a')
        fh.write(text + '\n')
        fh.close()

class LogFile(WriteFile):
    def write(self, content):
        self.write_line('%s %s' % (dt_str, content))

class DelimFile(WriteFile):
    def __init__(self, file_name, delim):
        super().__init__(file_name)
        self.delim = delim

    def write(self, list):

        for x in list:
            if self.delim in list:
                self.delim.join(piece for piece in x)

        line = self.delim.join(list)
        self.write_line(line)

log = LogFile('log.txt')
c = DelimFile('text.csv', ',')

log.write('This is a log message')
log.write('This is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])

c.write(['a', 'b', 'c', 'd,e,f'])
c.write(['1', '2', '3', '4', '5,6', '7,8'])