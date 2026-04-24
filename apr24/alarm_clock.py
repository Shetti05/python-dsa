import time

alarm = input("Enter time (HH:MM:SS): ")

while True:
    if time.strftime("%H:%M:%S") == alarm:
        print("Wake up!")
        break