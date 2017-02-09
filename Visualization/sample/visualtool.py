from pygal import Config,Pie,Bar,HorizontalBar,HorizontalStackedBar
from pygal.style import Style
import svgwrite
from math import ceil
from datetime import datetime


class tools:
    def __init__(self):
        self.style = Style(background='transprent')

    def update_style(self, data):
        for key, value in data.items():
            self.style = setattr(self.style, key, value)
        return self.style

    def pie_in_calendar(self, data, datetime_format):

        def week_of_month(data):
            dt = datetime.strptime(data, datetime_format)
            first_day = dt.replace(day=1)
            dom = dt.day
            adjusted_dom = dom + first_day.weekday()
            return int(ceil(adjusted_dom/7.0))

        calendar_pie = {}
        for i in ['week1', 'week2', 'week3', 'week4']:
            for j in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
                calendar_pie[i+j] = None

        ##TODO accept dataframe format or not

        self.table_string = '''
        <table id="pies" style="left:0;top:0;width:70%;height:70%;text-align:middle">
        <tr>
        <td></td><td>Mon</td><td>Tue</td><td>Wed</td><td>Thu</td><td>Fir</td><td>Sat</td><td>Sun</td>
        </tr>
        <tr><td>Week1</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td></tr>
        <tr><td>Week2</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td></tr>
        <tr><td>Week3</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td></tr>
        <tr><td>Week4</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td>
        <td>'''+pie_svg+'''</td></tr>
        '''
