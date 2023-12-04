class data_packet:
    """user_name = "string"
    user_ID = int
    day_ID = int
    week_ID = int
    month_ID = int
    daily_schedule = bool"""
    packet = []

    def make_package(name = "string", user_ID = int, days_schedule = bool, day_ID = int, week_ID = int, month_ID = int):

        data_packet.packet = [{"User name": name, "User ID": user_ID, "Day ID": day_ID, "Week ID": week_ID, "Month ID": month_ID, "Day's Schedule": days_schedule}]

        """data_packet.user_name = name
        data_packet.user_ID = userID
        data_packet.day_ID = dayID
        data_packet.week_ID = weekID
        data_packet.month_ID = monthID
        data_packet.daily_schedule = schedule.copy()"""

    def create_string_list(): 
        string_list = []
        hour = 0
        minutes = 0
        colon = ":"
        am_pm = "am"

        while hour < 24:
            if hour > 12:
                am_pm = "pm"
            temp = f'{hour % 12+ 1}{colon}{minutes*15}'
            if minutes == 0:
                temp += "0"
            temp += am_pm
            string_list.append(temp)
            minutes += 1
            if minutes > 3:
                minutes = 0
                hour += 1
        return string_list
    

    def send_packet():
        return data_packet.packet
    

def test():
    test = data_packet

    test_list = test.create_string_list()

    print(test_list)


#test()