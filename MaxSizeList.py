class MaxSizeList:

    def __init__(self, max_length):
        self.max_length = max_length
        self.max_length_list = []

    def push(self, value):
        self.max_length_list.append(value)

        if len(self.max_length_list) > self.max_length:
            self.max_length_list.pop(0)

    def get_list(self):
        return self.max_length_list

a = MaxSizeList(5)

a.push('hi')
a.push('let')
a.push('me')
a.push('go')
a.push('you')
a.push('ok')
a.push('I')

print(a.get_list())