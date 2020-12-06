def to_date(val):
  dates = ('Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday',
           'Saturday',
           'Sunday')
  return ', ' + dates[val]

def from_date(val):
  dates = {'monday' : 0,
           'tuesday' : 1,
           'wednesday' : 2,
           'thursday' : 3,
           'friday' : 4,
           'saturday' : 5,
           'sunday' : 6}
  return dates[val.lower()]

# Put a 0 in front of single digits
def fmt_num(val):
  return str(val) if val >= 10 else '0' + str(val)

def fmt_day(val):
  if val == 0:
    return ''
  elif val == 1:
    return ' (next day)'
  else:
    return ' (%d days later)' % val

def add_time(start, duration, s_day=None):

  splt_a = start.split(' ')
  splt_b = splt_a[0].split(':')

  day = 0
  hour = int(splt_b[0]) + (0 if splt_a[1] == 'AM' else 12)
  minute = int(splt_b[1])
  ampm = ''
  dotw = ''

  splt_c = duration.split(':')

  minute += int(splt_c[1])

  if minute >= 60:
    minute -= 60
    hour += 1

  hour += int(splt_c[0])

  if hour >= 24:
    day += hour // 24
    hour = hour % 24

  if hour == 0:
    ampm = ' AM'
    hour = 12
  elif hour == 12:
    ampm = ' PM'
  elif hour < 12:
    ampm = ' AM'
  else:
    hour -= 12
    ampm = ' PM'
  
  if s_day is not None:
    dotw = to_date((from_date(s_day) + day) % 7)

  return str(hour) + ':' + fmt_num(minute) + ampm + dotw + fmt_day(day)