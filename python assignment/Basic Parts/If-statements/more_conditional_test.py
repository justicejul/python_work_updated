name = "Justice"
print(name == "favour")
print(name == "justice")

print(name.lower() == "justice")


print("\nThe second part")
print("\nEquality N Inequality")
age = 17
print(16 == age)
print(17 == age)
print(17 != age)
print(16 != age)
print("\nGreater than N Less than")
print(19 > age)
print(19 < age)
print(16 > age)
print(16 < age)
print("\nGreater than or equal to")
print(20 >= age)
print(15 >= age)
print("\nLess than or equal to")
print(15 <= age)
print(20 <= age)


print("\nThe Third Part")
print("\nUsing the and keyword and the or keyword")
print("AND Keyword")
car = "ford"
print(car == "toyota" and car == "benz")
print(car != "toyota" and car != "benz")
print(car == "ford" and car == "benz")
print(car == "ford" and car == "ford")

print("\nOR Keyword")
print(car == "toyota" or car == "benz")
print(car != "toyota" or car != "benz")
print(car == "ford" or car == "benz")
print(car == "ford" or car == "ford")

print("\nTest whether an item is in a list")
musicians = ["sigrid", "big-sean", "birdy", "florence+machine", "sia", "labrinth", "lana-del-rey", "aurora"]
print("sia" in musicians)
print("kevin-hart" in musicians)

print("\nTest whether an item is not in a list")
print('birdy' not in musicians)
print("griff" not in musicians)