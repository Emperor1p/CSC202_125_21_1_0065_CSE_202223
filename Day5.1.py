
#loop
#for loop this is use to get items in a particular item
fruits = ["Apple", "Watermelon", "Guava", "Pineapple"]
for fruit in fruits:
    print(fruit)
#removing the indentation means the particular line is not inside for loop again
print(fruits) #this will print the list in full 


#for loop to calculate the average of an integer item
students_height = input("Input a list of student heights:  "). split()
for n in range(0, len(students_height)):
    students_height[n] =  int(students_height[n])
print(students_height)
lenght = len(students_height)
summ = sum(students_height)
average = round(summ / lenght)
print(f"The average student heights is {average}")


#for loop for calculating highest number in a list
student_scores = input("Enter the student score: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")


