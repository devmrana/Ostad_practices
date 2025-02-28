def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")
    
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25.0:
        print("Normal weight")
    elif 25.0 <= bmi < 30.0:
        print("Overweight")
    else:
        print("Obese")

# Taking input from user
height, weight = map(float, input("Enter height and weight: ").split())
calculate_bmi(height, weight)
