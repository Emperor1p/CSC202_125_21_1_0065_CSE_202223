#conditional statement
water_level = 70
if water_level > 60:
    print("drain the water")
else:
    print("continue")
    
#another if else statement
print("Welcome to the rollercoaster! ")
height = int(input("what is your height in cm? "))

if height > 34:
    print("You can ride the rollercoaster")
elif height in range(25,33):
    print("You are averagely okay but not not perfectly okay for you to ride")
else:
    print("Sorry, you have to grow taller than before you can ride.")

