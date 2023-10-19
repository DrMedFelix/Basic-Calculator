from tkinter import Y
import math

class calc:
    history = []
    
# Define a function for each operation (add, subtract, multiply, divide)
    def add(num1, num2):
        return num1+num2

    def substract(num1, num2):
        return num1-num2

    def multi(num1, num2):
        return num1*num2

    def div(num1, num2):
        return num1/num2

    def pow(num1, num2):
        return pow(num1, num2)
        
    def sqrt(num1):
        return math.sqrt(num1)
    
    def prozent(num1, num2):
        return num1/100 * num2
    
# Main program loop
    while True:
    # Display the menu
        print("Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square root")
        print("6. Exponential")
        print("7. %")
        print("8. HISTORY")
    # Get user choice
        choice = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))
    
        while choice == 0:
            print("0 isn't an option here!")
            choice = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))
        while choice >= 9:
            print("You can only choose between 1 to 8!")
            choice = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))

        if choice ==5:
            num1 = float(input("Enter the number:"))
            result = sqrt(num1)
            history.append(f"sqrt({num1}) = {result}")
            print("Result: ", result)
        else:
            if choice == 7:
                print("!number1! out of !number2!")
                num1 = float(input("Enter the first number: "))
                num2 = float(input(str(num1) +  "%" + " out of "))
                result = prozent(num1, num2)
                history.append(f"{num1}% out of {num2} = {result}")
                print("Result: ", result)
            else:
                if choice == 8:
                    if len(history) !=0:
                        for entry in history:
                            print(entry)
                    else:
                        print("History empty!")
                else:
    # Get user input for two numbers
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))

    # Perform the selected operation and display the result
        if choice == 1:
        # Call the add function
            result = add(num1, num2)
            history.append(f"{num1}+{num2} = {result}")
            print("Result: ", result)
    # Add code for the other operations (subtract, multiply, divide) here
        if choice == 2:
        # Call the add function
            result = substract(num1, num2)
            history.append(f"{num1}-{num2} = {result}")
            print("Result: ", result)
    
        if choice == 3:
        # Call the add function
            result = multi(num1, num2)
            history.append(f"{num1}*{num2} = {result}")
            print("Result: ", result)

        if choice == 4:
        # Call the add function
            if num2 == 0:
                print("You can't devide by zero!")
            else:
                result = div(num1, num2)
                history.append(f"{num1}/{num2} = {result}")
                print("Result: ", result)
        
        if choice == 6:
        # Call the add function
            result = pow(num1, num2)
            history.append(f"{num1}^{num2} = {result}")
            print("Result: ", result)

    # Ask the user if they want to perform another calculation
        another = input("Do you want to perform another calculation? (yes/no): ")
        if another.lower() != "yes":
            history.clear()
            break
