class Date(object):
    def get_date(self):
        return '2019-09-18'

class Time(Date):
    def ger_time(self):
        return '09:33:00'

dt = Date()
print(dt.get_date())

tm = Time()
print(tm.ger_time())
print(tm.get_date())