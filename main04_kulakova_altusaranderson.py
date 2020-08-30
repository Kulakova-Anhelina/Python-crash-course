foods = ['asparagus', 'broccoli', 'carrot']
cal = [60, 20, 25]
weight = [50, 200, 120]
foods.insert(0, 'apple')
cal.insert(0, 12)
weight.insert(0, 100)

print("maximum kcal per 100 g is " + str(max(cal)))

print("Hello, Welcome to Nutri Database, for now we have a few items, please add more")

for food in foods:
    print(food.upper())


def userInput():
    product = input("Please, enter the product: ")
    foods.append(product)
    k = float(input("Please, enter the calories per 100g: "))
    cal.append(k)
    w = float(input("Please, enter weight in g: "))
    weight.append(w)


answer = ''
while answer != 'no':
    userInput()
    answer = input("Would you like to continue? Type 'yes' or 'no'")

for i in range(len(foods)):
    print(foods[i] + " " + str(cal[i] * (weight[i])) + " calories")