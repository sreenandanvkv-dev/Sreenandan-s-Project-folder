height = float(input("Enter your height in cm: "))
weight = float(input("Enter your height in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("your underweight.")
elif BMI <= 24.9:
    print("you are healthy.")
elif BMI <= 29.9:
    print("you are over weight")
elif BMI <= 34.5:
    print("you are severely over weight")
elif BMI <= 39.5:
    print("You are Obese")
else:
    print("You are severely obese")