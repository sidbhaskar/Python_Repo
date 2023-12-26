def convert_time(time):
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    elif time[-2:] == "AM":
        return time[:-2]
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
    else:
        return str(int(time[:2]) + 12) + time[2:5]

print(convert_time("02:30 PM"))
print(convert_time("12:00 AM"))
print(convert_time("12:00 PM"))
print(convert_time("01:00 AM"))
