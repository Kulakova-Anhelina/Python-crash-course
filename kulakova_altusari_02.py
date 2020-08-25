class Recommendation:
    def __init__(self, name):
        self.name = name

    def rec(self):
        print(self.name + " You are advised to eat more vegetables")


def bmi(height, weight):
    """"Function for calculating BMI"""
    user_bmi = round(weight / (height / 100) ** 2, 2)
    if user_bmi < 18:
        print(str(user_bmi) + "," + " you are underweight")
    elif user_bmi > 25:
        print(str(user_bmi) + "," + " you are overweight")
    else:
        print(str(user_bmi) + "," + " you are normal")
    return user_bmi


def cal_intake(activity, gender, age, weight, height):
    # Function of calories
    kcalIntake = 0
    k = 0
    if activity == 1:
        k = 1.2
    elif activity == 2:
        k = 1.4
    else:
        k = 1.6
    if gender == "f":
        kcalIntake = (10 * weight + 6.25 * height - 5 * age - 161) * k
    else:
        kcalIntake = (10 * weight + 6.25 * height - 5 * age + 5) * k
    kcalIntake = str(kcalIntake)
    print("Your daily recommended kcal intake is " + kcalIntake)


users = []


def read_data():
    print("Hello, user! I wanna help you to calculate your BMI calculator and daily kcal intake recommendation.")
    name = input("What is your name?")
    print("Nice to meet you " + name + "!")
    gender = input("What is your gender (enter f or m)? ")
    age = input("Please enter your age: ")
    height = input("Enter your height in cm: ")
    weight = input("Enter your weight: ")
    activity = input("How much of physical activity do you have?"
                     "\n Enter 1 if you have low activity level."
                     "\n Enter 2 if you have medium activity."
                     "\n Enter 3 if you have a lot of physical activities: ")
    try:
        age = int(age)
        weight = float(weight)
        height = float(height)
        activity = int(activity)
    except ValueError:
        print("Please enter the values in correct format")
    else:
        users.append({'name': name, 'age': age, 'weight': weight, 'height': height, 'activity': activity})
        filename = 'journal.txt'
        with open(filename, 'w') as file_object:
            file_object.write("User: " + name + ', age: ' + str(age) + ', weight: ' + str(weight) + ', height: ' +
                              str(height) + ', activity: ' +
                              str(activity) + "\n")
        if bmi(height, weight) > 25:
            new = Recommendation(name)
            new.rec()
        cal_intake(activity, gender, age, weight, height)


answer = ''
while answer != 'no':
    read_data()
    answer = input("Would you like to continue? Type 'yes' or 'no'")
