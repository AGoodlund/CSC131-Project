from flask import Flask
from app import db, Month, Week, Day, Time
from app import app


with app.app_context():
  db.drop_all()
  db.create_all()
  
  month1 = Month(month='August')
  
  week1 = Week(month=month1)
  week2 = Week(month=month1)
  
  day1_1 = Day(day='Monday', week_id=1)
  day2_1 = Day(day='Tuesday', week_id=1)
  day3_1 = Day(day='Wednesday', week_id=1)
  day4_1 = Day(day='Thursday', week_id=1)
  day5_1 = Day(day='Friday', week_id=1)
  day6_1 = Day(day='Saturday', week_id=1)
  day7_1 = Day(day='Sunday', week_id=1)  
  
  day1_2 = Day(day='Monday', week_id=2)
  day2_2 = Day(day='Tuesday', week_id=2)
  day3_2 = Day(day='Wednesday', week_id=2)
  day4_2 = Day(day='Thursday', week_id=2)
  day5_2 = Day(day='Friday', week_id=2)
  day6_2 = Day(day='Saturday', week_id=2)
  day7_2 = Day(day='Sunday', week_id=2) 
  
  time1 = Time(time='2:00 PM', day_id=1)
  time2 = Time(time='3:00 PM', day_id=9)
  time3 = Time(time = '11:00 AM', day_id=9)
  time4 = Time(time='9:00 AM', day_id=1)
  time5 = Time(time='9:00 PM', day_id=2)
  
  
  db.session.add(month1)
  db.session.add_all([week1, week2])
  db.session.add_all([day1_1, day2_1, day3_1, day4_1, day5_1, day6_1, day7_1])
  db.session.add_all([day1_2, day2_2, day3_2, day4_2, day5_2, day6_2, day7_2])
  db.session.add_all([time1, time2, time3, time4, time5])
  
  db.session.commit()
  
  print(Time.query.all())
  
  
  