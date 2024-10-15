print("Welcome to the Basic Calculator!")
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")  
print("6. Exit")  
choice = input("Enter your choice (1/2/3/4): ")

if choice in ["1", "2", "3", "4"]:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))

    if choice == "1" :
        print("The Sum Of The Number Is ", num1 + num2) 
    elif choice == "2":
        print("The Subtraction Of The Number Is ", num1 - num2)
    elif choice == "3":
        print("The Multiplication Of The Number Is  ", num1 * num2)
    elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The Divison Of The Numbers Is  ", num1/num2)

            else:
                print("Error: Division by zero is not allowed.")
    elif choice == "5":
         print("f{num1} raised to the power of {exponent} is: {result}")
    
else:
    print("The Entered Option Isnt Valid Pls Make Your Selcetion Between 1,2,3,4")
