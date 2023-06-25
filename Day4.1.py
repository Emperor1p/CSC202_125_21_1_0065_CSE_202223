
#Randomisation and python list
import random 

random_integer = random.randint(1, 10)
print(random_integer)

#0.0000 - 0.99999999999
random_float = random.random() * 6
print(random_float)


 #list
Fruit = ['Mango' , 'Orange','Pineapple']

#list append
fruit = ['Banana', 'Apple']
Fruit.append(fruit)
print(Fruit[2])


#using str.split(',')
mar = "Hello, from, AskPython"
op = mar.split(",")
print(op)


#import

import  random
a = ['one', 'two', 'three', 'four', 'five', 'six']
print(a)

for i in range(5):
    print(random.choice(a))


