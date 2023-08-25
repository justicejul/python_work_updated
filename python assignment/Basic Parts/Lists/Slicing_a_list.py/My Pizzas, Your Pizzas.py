pizzas = ['chicken-flavoured pizza', 'beef-flavoured pizza', 'vege-flavoured pizza']
friend_pizzas = pizzas[:]
pizzas.insert(0, 'pepperoni-pizza')
friend_pizzas.insert(0, 'pork-flavoured pizza')

print(pizzas)


for pizza in pizzas:
	print(pizza)
print("this are my favourite pizza:\n")

for friend_pizza in friend_pizzas:
	print(friend_pizza)
print("this are my friends favourite pizza:")