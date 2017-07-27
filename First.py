food = ['a','bb', 'c','d']

print(len(food))

for foodarrayvalues in food[2:]:
    print(foodarrayvalues)
    print(len(foodarrayvalues))

food.append("hi")
print(food)

for x in range(10,50,5):
    print(x)

while len(food) <= 8:
    print("Hi")
    food.append("Added")
    print(food)