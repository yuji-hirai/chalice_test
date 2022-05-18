from datetime import datetime, timedelta

def week_day():
    dateJST = datetime.today() + timedelta(hours=9)
    weekday = dateJST.strftime('%a')
    return weekday