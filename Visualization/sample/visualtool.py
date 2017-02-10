from pygal import Config,Pie,Bar,HorizontalBar,HorizontalStackedBar
from pygal.style import Style
import svgwrite
from math import ceil
from datetime import datetime
from htmlwriter import table, tr, td

class tools:
    def __init__(self):
        self.style = Style(background='transprent')

    def update_style(self, data):
        for key, value in data.items():
            self.style = setattr(self.style, key, value)
        return self.style

    def pie_in_calendar(self, data, datetime_format):

        container = table()
        day_in_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        week_in_month = ['week1', 'week2', 'week3', 'week4']

        def week_of_month(data):
            dt = datetime.strptime(data, datetime_format)
            first_day = dt.replace(day=1)
            dom = dt.day
            adjusted_dom = dom + first_day.weekday()
            weeknum = int(ceil(adjusted_dom/7.0))
            return 'week'+str(weeknum)

        def dow(data):
            dt = datetime.strptime(data, datetime_format)
            dow_index= dt.weekday()
            return day_in_week[dow_index]

        calendar_pie = {}
        for i in week_in_month:
            for j in day_in_week:
                calendar_pie[i+j] = None

        for j in data:
            winm = week_of_month(data)
            dofw = dow(data)

            calendar_pie[winm+dofw] =
