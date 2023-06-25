#Conditional statement for detecting odd or even number
number =int(input("Enter a number you want to check: "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#if else statement with for loop
for num in range (1,29):
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
        

#conditonal statement inside conditional statement
print("Welcome to the rollercoaster! ")
height = int(input("Enter your height in cm : "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5$")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay 12$")
else:
    print("Sorry, you have to grow taller before you can ride.")

