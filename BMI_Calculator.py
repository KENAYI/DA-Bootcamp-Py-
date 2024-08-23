# Calculator takes input and outputs users body mass index BMI

# Request users name
name = input("Enter your name: ")

# Request users weight, in lbs
weight = int(input("Please enter your weight (in lbs): "))

# Request users height, in inches
height = int(input("Please enter your height (in inches): "))

#print(weight)

# Calculate and output users BMI
BMI = round((weight * 703) / (height * height), 1)
print(BMI)

if BMI > 0:
    if(BMI<18.5):
        print(name + ", you are underweight :()")
    elif (BMI <= 24.9):
        print(name + ", you are normal weight :)")
    elif (BMI <= 29.9):
        print(name + ", you are overweight :/")
    elif (BMI <= 34.9):
        print(name + ", you are obese!")
    elif (BMI <= 39.9):
        print(name + ", damn! You are severely obese... ")
    else:
        print(name + ", please try seeking help :/")
else:
    print(name + ", please enter valid weight and height!")