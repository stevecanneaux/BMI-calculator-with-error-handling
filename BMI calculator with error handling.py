#BMI calculator with error handling

print("BMI Calculator")
inkg = input("enter your weight in kg ")
inm = input("enter your height in m ")
m = inm
kg = inkg
try:
    kg = float(inkg)
except:
    kg = -1
try:
    m = float(inm)
except:
    m = -2
if kg == -1 :
    print("error in kg input")
elif m == -1 :
    print("error in m input")
else:
    bmi = kg / (m * m)
    print("your BMI is", bmi)
if bmi <= 18.5:
    print("You are under weight for your height")
elif bmi <= 24.5:
    print("Your weight is in the healthy range for your height")
elif bmi <= 29.5:
    print("You are over wieght for your height")
else:
    print("You are obese for your height")
