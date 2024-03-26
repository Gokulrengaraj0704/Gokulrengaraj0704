dic_car = {"car1": "BMW X1", "car2": "Corolla", "car3": "Virtus GT", "car4": "Slavia Sport", "car5": "Taigun"}

print("Printing Key value Pair")
for key, value in dic_car.items():
    print(f"{key} - {value}")
print("--------------------------------")

# Removing the Last element
print("Popped Item", dic_car.popitem())
print("--------------------------------")

# Adding a Key
dic_car.update({"Car":"Tesla"})

print("Updated Car List ", dic_car)
print("--------------------------------")

# Converting The Dictionary TO a list

dic_key = []
dic_value = []

for key, value in dic_car.items():
    dic_key.append(key)
    dic_value.append(value)

print("List for Key Values Of a Dictionary", dic_key)
print("List for Key Values Of a Dictionar", dic_value)
