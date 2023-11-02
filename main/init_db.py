from flask import Flask
from app import db, Month, Week, Day, Time
from app import app


with app.app_context():
  db.drop_all()
  db.create_all()
  
  month1 = Month(month='August')
  
  week1M1 = Week(month=month1)
  week2M1 = Week(month=month1)
  week3M1 = Week(month=month1)
  
  day1W1 = Day(day='Monday')
  day2W1 = Day(day='Tuesday')
  day3W1 = Day(day='Wednesday')
  day4W1 = Day(day='Thursday')
  day5W1 = Day(day='Friday')
  day6W1 = Day(day='Saturday')
  day7W1 = Day(day='Sunday')  
  
  day1W2 = Day(day='Monday')
  day2W2 = Day(day='Tuesday')
  day3W2 = Day(day='Wednesday')
  day4W2 = Day(day='Thursday')
  day5W2 = Day(day='Friday')
  day6W2 = Day(day='Saturday')
  day7W2 = Day(day='Sunday') 

  day1W3 = Day(day='Monday')
  day2W3 = Day(day='Tuesday')

  week1M1.days.append(day1W1)
  week1M1.days.append(day2W1)
  week1M1.days.append(day3W1)
  week1M1.days.append(day4W1)
  week1M1.days.append(day5W1)
  week1M1.days.append(day6W1)
  week1M1.days.append(day7W1)

  week2M1.days.append(day1W2)
  week2M1.days.append(day2W2)
  week2M1.days.append(day3W2)
  week2M1.days.append(day4W2)
  week2M1.days.append(day5W2)
  week2M1.days.append(day6W2)
  week2M1.days.append(day7W2)

  week3M1.days.append(day1W3)
  week3M1.days.append(day2W3)
  
  
  time1 = Time(time='1:00 AM')
  time2 = Time(time='2:00 AM')
  time3 = Time(time = '11:00 AM')
  time4 = Time(time='9:00 AM')
  time5 = Time(time='9:00 PM')

  day1W1.times.append(time1)
  day1W1.times.append(time2)
  day2W1.times.append(time3)
  day2W2.times.append(time4)
  day2W2.times.append(time5)

  
  db.session.add(month1)
  db.session.add_all([week1M1, week2M1, week3M1])
  db.session.add_all([day1W1, day2W1, day3W1, day4W1, day5W1, day6W1, day7W1])
  db.session.add_all([day1W2, day2W2, day3W2, day4W2, day5W2, day6W2, day7W2])
  db.session.add_all([day1W3, day2W3])
  db.session.add_all([time1, time2, time3, time4, time5])
  
  db.session.commit()
  
  
  
  