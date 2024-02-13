import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hours = int(time.strftime('%H'))
print(hours)

if (hours <= 9):
    print("Good Morning!")
elif (hours >= 10 and hours < 15):
    print("Good non!")
elif (hours >= 15 and hours < 20):
    print("Good afternon!")

else:
    print("Good nigth...you should sleep now, ASAP!")
