class Recommendation:
    def __init__(self, name):
        self.name = name

    def rec(self):
        print(self.name + " You are advised to eat more vegetables")


user = input("Please, enter your Name: ")
new = Recommendation(user)
new.rec()
