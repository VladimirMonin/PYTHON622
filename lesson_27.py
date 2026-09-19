"""
Lesson 27 - Знакомство с ООП
"""

class Fridge:
    prdoducts = ["Колбаска", "Грушевая наливка"]

my_fridge = Fridge()

print(my_fridge.prdoducts)

my_mother_fridge = Fridge()
my_mother_fridge.prdoducts.append("кабачок")
my_mother_fridge.prdoducts.append("кабачок 2")

print(id(my_fridge))
print(id(my_mother_fridge))

print("Мой холодильник", my_fridge.prdoducts)
print(id(my_fridge.prdoducts), id(my_mother_fridge.prdoducts)) # 1581763181056 1581763181056