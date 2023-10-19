"""Question-7
HEALTHY PROGRAMMER
Water - water.mp3 (3.5 liters) - Drank - log
Eyes - eyes.mp3 - every 30 min - EyDone - log
Physical activity - Physical.mp3 - every 45min - ExDone - log

Rules
Pygame module to play audio"""

import pygame
import time
from datetime import datetime, time as dt_time


def getdate():
    import datetime
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%d-%m-%y %A at %H:%M:%S")


start_time = dt_time(9, 0)  # 9:00 AM
end_time = dt_time(18, 0)  # 5:00 PM
now = datetime.now().time()
if now < start_time:
    # If the current time is before 9:00 AM, wait until 9:00 AM
    initial_delay = (datetime.combine(datetime.today(), start_time) - datetime.now()).seconds
else:
    # If the current time is after 9:00 AM, calculate the delay until the next 10-second mark#
    seconds_until_next_10s = 10 - (now.second % 10)
    initial_delay = seconds_until_next_10s

while True:
    pygame.init()
    file = "water.mp3"
    pygame.mixer.music.load(file)
    water = str
    current_time = datetime.now().time()
    time.sleep(initial_delay)
    initial_delay = 10
    if start_time <= current_time <= end_time and water != "Drank":
        pygame.mixer.music.play(loops=-1)
        water = str(input("This is the reminder to Drink water."
                          "\nif you have drank water enter 'Drank' : "))
    if start_time <= current_time <= end_time and water == "Drank":
        with open("water_log.txt", "a") as log:
            record = log.write("you have drank water on " + str(getdate()) + "\n")
            print("Thank you boss...good job")
        pygame.mixer.music.stop()
    pygame.init()
    file = "eyes.mp3"
    pygame.mixer.music.load(file)
    water = str
    current_time = datetime.now().time()
    time.sleep(initial_delay)
    initial_delay = 15
    if start_time <= current_time <= end_time and water != "EyDone":
        pygame.mixer.music.play(loops=-1)
        water = str(input("This is the reminder to eye exercise."
                          "\nif you have done eyes exercise enter 'EyDone' : "))
    if start_time <= current_time <= end_time and water == "EyDone":
        with open("eyes_log.txt", "a") as log:
            record = log.write("you have done eyes exercise on " + str(getdate()) + "\n")
            print("Thank you boss...good job")
        pygame.mixer.music.stop()
    pygame.init()
    file = "physical.mp3"
    pygame.mixer.music.load(file)
    water = str
    current_time = datetime.now().time()
    time.sleep(initial_delay)
    initial_delay = 20
    if start_time <= current_time <= end_time and water != "ExDone":
        pygame.mixer.music.play(loops=-1)
        water = str(input("This is the reminder to physical exercise."
                          "\nif you have done physical exercise 'ExDone' : "))
    if start_time <= current_time <= end_time and water == "ExDone":
        with open("physical_log.txt", "a") as log:
            record = log.write("you have done physical exercise" + str(getdate()) + "\n")
            print("Thank you boss...good job")
        pygame.mixer.music.stop()





