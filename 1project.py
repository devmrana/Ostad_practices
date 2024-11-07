# Basic Calculator Operation
print("1. Addition")
print("2. Subtraction")
print("3. Multiplecation")
print("4. Division")
print("--------------------------")

while True:
    option = int(input("Select an option for Basic Calculator Operation: "))
    
    if option == 1:
        print("You are selected Addition")
        n1 = int(input("Enter 1st input: "))
        n2 = int(input("Enter 2nd input: "))
        sum = n1+n2
        print("Summation is= " + str(sum))
    elif option == 2:
        print("You are selected Subtraction")
        n1 = int(input("Enter 1st input: "))
        n2 = int(input("Enter 2nd input: "))
        sub = n1-n2
        print(f"Subtraction is= {sub}")
    elif option == 3:
        print("You are selected Multiplecation")
        n1 = int(input("Enter 1st input: "))
        n2 = int(input("Enter 2nd input: "))
        multi = n1*n2
        print(f"Multiplecation is= {multi}")

    elif option == 4:
        print("You are selected Division")
        n1 = int(input("Enter 1st input: "))
        n2 = int(input("Enter 2nd input: "))
        divin = n1/n2
        print(f"Division is= {divin:.2f}")
    else:
        print("Invalid input. Try 1 to 4 any digit")

