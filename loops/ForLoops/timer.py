# import time 
# my_time = int(input("Enter the time in seconds: "))
# for x in range (0, my_time):
#     print(x)
#     time.sleep(1)
# print("Time's up!")

# import time 
# my_time = int(input("Enter the time in seconds: "))
# for x in reversed(range(0, my_time)):
#     print(x)
#     time.sleep(1)
# print("Time's up!")

import time 
my_time = int(input("Enter the time in hours: "))
if my_time ==  0:
    print("Enter the time in minutes: ")
    my_time = int(input("Enter the time in minutes: "))
    if my_time == 0:
        print("Enter the time in seconds: ")
        my_time = int(input("Enter the time in seconds: "))
else:
        minutes = my_time * 60
        seconds = minutes * 60

for x in reversed(range(0, seconds)):
    print(f"{x//3600:02d} : {(x%3600)//60:02d} : {x%60:02d}")
    time.sleep(1)
print("Time's up!")


