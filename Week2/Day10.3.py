
#calc
def add(n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return(n1 * n2)
 
def divide(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "*" : multiply,
    "-" : subtract, 
    "/" : divide,
}

def calculator():

    num1 = float(input("What is the first number?: "))

    for symbol in operation:
        print(symbol)

    should_continue = True

    while should_continue:
    
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            print(f"Your answer is {answer}\n\n Take another operation")
            
            
            calculator()
calculator()
        





operation_symbol = input("Pick another operation: ")
num3 = int(input("What is the next number?: "))
calculation_function = operation[operation_symbol]
second_answer = calculation_function(first_answer, num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
#return and print  


