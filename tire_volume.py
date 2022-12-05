#Import math to use math.pi for volume

import math

#from datetime import datetime to output the dat and time into the volumes.txt file

from datetime import datetime

#today = datetime.now() to out the exact date and time

today = datetime.now()

print("Welcome to Los Hermanos de los Neumaticos Tire Shop!! Please fill out all the information of your tire below.\n")

#Opens and closes the volumes.txt file and reads it in Python as volumes_files

with open("volumes.txt", "a+",) as volumes_file:
    
    #User input for their tire

    width = int(input('Enter the width of the tire in millimeters: '))
    aspect_ratio = int(input('Enter the aspect ratio of the tire: '))
    diameter = int(input('Enter the diameter of the wheel in inches: '))
    volume = ((((math.pi) * ((width**2)*aspect_ratio))*((width * aspect_ratio) +(2540 * diameter))) / 10000000000)
    print(f"Thank you for your tire information! The approximate volume of your tire is {volume:.2f} liters.\n")

    
    #Writes and prints the date and time, user input, and volume separated by commas

    volumes_file.write(str(today))
    volumes_file.write(", ")
    volumes_file.write(str(width))
    volumes_file.write(", ")
    volumes_file.write(str(aspect_ratio))
    volumes_file.write(", ")
    volumes_file.write(str(diameter))
    volumes_file.write(", ")
    volumes_file.write(f'{float(volume):.2f}\n')

print("Thank you for shopping at Los Hermanos de los Neumaticos Tires Shop!!! Hope to see you again!!")       
