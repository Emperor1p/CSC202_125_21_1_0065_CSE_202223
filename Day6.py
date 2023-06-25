#function
print("Hello")
print(len("Hello"))

#want to maake our own function
def my_function():
    print("Hello")
    print("How are you doing")
my_function()


#Another function
def greeting(fname):
    print("Hello",fname)
greeting("Python")


#Another function
def greeting(fname = "Python"):
    print("Hello", fname)
greeting()
greeting("World")
greeting("Sara")


#Another function
def add_num(i):
    return i + 5
print(add_num(4))



def factorial(i):
    if(n>0):
        result = n + factorial(n-1)
        print(result)
    else :
        result = 0
    return result
factorial(5)

