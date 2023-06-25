
#for loop for adding series of number from 1 to 100
total = 0
for num in range(1,101):
    total += num    
print(total)


#sum of all even number from 1 to 100 with one print statement
sumation_even_number = 0
for number in range(2,101,2):
    sumation_even_number += number
print(sumation_even_number)



for num in range (1,101):
    if num % 2 == 0:
        print(f"{num} Even number")
    else:
        print(f"{num} Odd number")
    


