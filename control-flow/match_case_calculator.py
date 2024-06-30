first_nbr = int(input("Enter the first number:"))

second_nbr = int(input("Enter the second number:"))

operation  = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = first_nbr + second_nbr
        print(result)
    case "-":
        result = first_nbr - second_nbr
        print(result)
    case "*":
        result = first_nbr * second_nbr
        print(result)
    case "/":
        if second_nbr != 0:
            print(result = first_nbr / second_nbr)
        else:
            print("Cannot divide by zero.")



