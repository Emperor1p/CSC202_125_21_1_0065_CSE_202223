#!/usr/bin/env python
# coding: utf-8

# In[44]:


#DATA TYPES

#string

"Hello"

#You can print any number of the string with the use of index, example

print("Hello" [2]) #this will print third letter of the world "Hello"

#You can represent integers as astring with the use of quotation mark
print("133" + "354")


#Integer are number
print(224_21 + 34) #if you out underscore inside your int computer will remove it


#float
3.142

#Boolean
#statement with 
true or false

#How to find the len of a data type
num =  len(input("What is your name: "))
print(num)

#Adding len to the value assign to a variable that is string will make it int
#note you can not find the len of integer

num_cha = len(input("What is your name? :"))
print(type(num_cha))

#mathematical operation
print(3 + 4)
print(6 - 3)
print(2 * 5)
print(3 ** 3)
print(4/2)

print(round(2.666666666, 4))
#note 4 is the decinal place

#BMI callculator

height = int(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
BMI = ((weight) / (height) ** 2)
print(BMI)

#f_string
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}")
      
#Exercise for the DAY
print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15 or 20? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person pay {final_amount} ")




 


# In[ ]:




