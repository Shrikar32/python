import time
my_time = int(input("Enter the time in hours: "))
if my_time == 0:
    minutes = int(input("Enter the time in minutes: "))
    if my_time == 0 and minutes == 0:
        seconds = int(input("Enter the time in seconds: "))
else:
    minutes = 60*my_time
    seconds = 60*60*my_time

for x in reversed(range(0, seconds, 1)):
    print(f"{seconds//3600:02d}:{seconds//60:02d}:{seconds:02d}")
    time.sleep(1)
print("Times up")

          




        
    