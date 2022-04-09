import datetime
from persiantools.jdatetime import JalaliDate
from persiantools import characters, digits
import jdatetime
# print('Today date:', datetime.date.today())
# print('Today date with time:', datetime.datetime.now())
print(characters.ar_to_fa("كيك"))
f = "کیک"
print(f)
print(JalaliDate.today())
print(jdatetime.date.today())
print(jdatetime.datetime.now())