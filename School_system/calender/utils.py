from calendar import HTMLCalendar
from .models import Event

class Calender(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calender, self).__init__()

	
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for Event in events_per_day:
			d += f'<li> {Event.Event_Name} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		calender = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		calender += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		calender+= f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			calender += f'{self.formatweek(week, events)}\n'
		return calender