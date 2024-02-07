def ageCalculater(y,m,d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age= int((today-dob).days/365)
    print(age)
ageCalculater(1996,11,10)