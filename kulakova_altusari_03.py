foods = ['asparagus', 'broccoli', 'carrot']
cal = [60, 20, 25]
foods.insert(0, 'apple')
cal.insert(0, 12)

print("Hello, Welcome to Nutri Database, for now we have a few items, please add more")

for food in foods:
    print(food)


def userInput():
    product = input("Please, enter the product: ")
    foods.append(product)
    k = float(input("Please, enter the calories per 100g: "))
    cal.append(k)



answer = ''
while answer != 'no':
    userInput()
    answer = input("Would you like to continue? Type 'yes' or 'no'")
    for x in range(0, (len(foods)-1)):
        print(foods[x] + " contains " + str(cal[x]) + " kcal")

print("the latest food item is - " + foods.pop())
foods.remove('apple')
foods.reverse()
print(foods)
print(sorted(foods))
del cal[0]
print(cal)
