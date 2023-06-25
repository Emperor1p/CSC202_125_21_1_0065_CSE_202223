#Use simple if else statement to deduce leap and not leap year
year = int(input('Which year do you want to check? '))

if year % 4 == 0:
    print("Leap year")
    if year % 100 == 0:
        print("Not leap year")
        if year % 400 == 0:
            print("Leap year")
    
        else:
            print("Not leap year")
        
    else:
        print("leap year")
else:
    print("Not leap year")
    
    
    


#love calculator
print("Welcome to love calculator")
name = input("What is your name? ")
name2 = input("What is the name of your partner ? ")
combine = name + name2
lowercase = combine.lower()

t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")

true = t + r + u + e

l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")

love = l + o + v + e

loveScore = int(str(true) + str(love))

if (loveScore < 10) or (loveScore > 90):
    print(f"Your love score is{loveScore}, you go together like coke and mentos")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your love score is {loveScore}, you are alright together")
else:
    print(f"Your love score is {loveScore}, you are good to go ")

print(loveScore)


