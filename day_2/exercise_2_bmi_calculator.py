import math

height = input("Enter your height in m:\n")
weight = input("Enter your weight in kg:\n")
bmi = int(weight) / math.pow(float(height), 2)
print(int(bmi))
