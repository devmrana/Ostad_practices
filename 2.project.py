def greeting():
    print("\nFavourite Foods Manager\n-------------------------")
    # Display the options
    for index, value in enumerate(options, start=1):
        print(f"{index}. {value}")


# List of options
options = ["Exit", "Add foods", "Remove foods", "View all favourite foods"]
# greeting()

favourite_foods = []


def foodManager(choice):
    # Check the user's choice and respond accordingly
    if choice == 1:
        print("You chose to exit. Thanks for using Favourite Foods Manager")
    elif choice == 2:
        print("You chose to add foods.")
        food = input("Enter you favourite food name: ")
        itemLower = food.lower()
        favourite_foods.append(itemLower)
        print(f"{food.capitalize()} added Successfully")
    elif choice == 3:
        print("You chose to remove foods.")
        food = input("Enter a food name which you want to remove: ")
        itemLower = food.lower()
        favourite_foods.remove(itemLower)
        print(f"{food.capitalize()} remove Successfully")
    elif choice == 4:
        print("You chose to view all favourite foods.")
        if favourite_foods:
            print("Your favourite foods: ")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}. {food.capitalize()}")
        else:
            print("Food List is empty or didn't added yet! ")
    else:
        print("Invalid choice. Please select a number from the list.")


while True:

    # Prompt the user for a choice
    try:
        greeting()
        choice = int(input("Choose an option (1-4): "))  # Convert input to integer
        print("-------------------------------")
        foodManager(choice)  # Call to function
    except ValueError:
        print("Invalid input. Please enter a number.")
