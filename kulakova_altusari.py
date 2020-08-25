def BMI(height, weight):
    BMI = round(weight / (height/100) ** 2, 2)
    if BMI < 18:
        print(str(BMI) + "," + " you are underweight")
    elif BMI > 25:
        print(str(BMI) + "," + " you are overweight")
    else:
        print(str(BMI) + "," + " you are normal")


def cal_intake(activity, gender, age, weight, height):
    kcalIntake = 0
    k = 0
    if activity == 1:
        k = 1.2
    elif activity == 2:
        k = 1.4
    else:
        k = 1.6
    if gender == "f":
        kcalIntake = (10*weight + 6.25*height - 5*age - 161) * k
    else:
        kcalIntake = (10 * weight + 6.25 * height - 5 * age + 5) * k
    kcalIntake = str(kcalIntake)
    print("Your daily recommended kcal intake is " + kcalIntake)

users = []

print("Hello, user! I wanna help you to calculate your BMI calculator and daily kcal intake recommendation.")


name = input("What is your name?")
print("Nice to meet you " + name + "!")

gender = input("What is your gender (enter f or m)? ")
age = int(input("Please enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight: "))
activity = float(input("How much of physical activity do you have?"
                       "\n Enter 1 if you have low activity level."
                       "\n Enter 2 if you have medium activity."
                       "\n Enter 3 if you have a lot of physical activities: "))

users.append({'name': name, 'age': age, 'weight': weight, 'height': height, 'activity': activity})
BMI(height, weight)
cal_intake(activity, gender, age, weight, height)
print(users)
