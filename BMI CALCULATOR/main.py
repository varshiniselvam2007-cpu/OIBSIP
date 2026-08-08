print("===== BMI Calculator =====")

height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kg): "))

bmi = weight / (height ** 2)

print("\nYour BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("BMI Category: Underweight")
elif bmi < 25:
    print("BMI Category: Normal Weight")
elif bmi < 30:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")
