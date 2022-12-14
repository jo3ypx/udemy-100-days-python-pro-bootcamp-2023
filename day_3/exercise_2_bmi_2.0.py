import math

height = input("Enter your height in m:\n")
weight = input("Enter your weight in kg:\n")
bmi = round(int(weight) / math.pow(float(height), 2))

if bmi < 18.5:
    print("Your BMI is " + str(bmi) + ", you are underweight.")
elif bmi <= 25:
    print("Your BMI is " + str(bmi) + ", you have a normal weight.")
elif bmi <= 30:
    print("Your BMI is " + str(bmi) + ", you are slightly overweight.")
elif bmi <= 35:
    print("Your BMI is " + str(bmi) + ", you are obese.")
elif bmi > 35:
    print("Your BMI is " + str(bmi) + ", you are clinically obese.")
