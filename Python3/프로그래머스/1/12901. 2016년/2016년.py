from datetime import datetime, timedelta

def solution(a, b):
    answer = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    standard_date = datetime(2016,1,1)
    date = datetime(2016,a,b)
    
    return answer[(date-standard_date).days%7]