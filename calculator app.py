while True:
    options="""
               ("1. Addition")
              ("2. Subtraction")
              ("3. Multiplication")
               ("4. Division")
                ("5. Exit")"""
    print(options)       
    option = input("Enter  the options:")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if option in ('1', '2', '3', '4'):
        if option == '1':
            print("Result:",(num1+num2))
        elif option == '2':
            print("Result:", (num1-num2))
        elif option == '3':
            print("Result:", (num1*num2))
        elif option == '4':
            if num2!=0:
                print("Result:", (num1/num2))
            else:
                print("Division by zero is impossible ")
    elif option == '5':
        print("Exiting...")
        break
    else:
        print("Invalid input")  