products = {
    'vegetables': ['asparagus', 'cucumber', 'tomato'],
    'protein': ['salmon', 'chicken breast', 'beef'],
    'fruits': ['mango', 'banana', 'kivi']
}

products['snacks'] = ['nuts', 'yogurt', 'berries']

userIntput = input("Hello, Welcome to Nutri Database, pease choose your favourite item: ")
print(products)

cal = {'asparagus': 12, 'cucumber': 10, 'tomato': 5, 'salmon': 30, 'chicken breast': 50, 'beef': 60, 'mango': 40,
       'banana': 30, 'kivi': 30}

joules = {}

for key, value in cal.items():
    joules[key] = value * 4
print(joules)
