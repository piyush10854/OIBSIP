# BMI Calculator for Beginners

print("==== BMI Calculator ====")

# Take input
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI
print("\nYour BMI is:", round(bmi, 2))

# Categorize BMI
if bmi < 18.5:
    print("Category: Underweight")
    
elif bmi >= 18.5 and bmi < 24.9:
    print("Category: Normal Weight")
    
elif bmi >= 25 and bmi < 29.9:
    print("Category: Overweight")
    
else:
    print("Category: Obese")