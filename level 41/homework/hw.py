cars =['bmw', 'mercedes', 'bugat', 'porshe']
cars.append("bentl")
print(cars)


sport =['rugby', 'carate', 'football', 'basketbal']
sport.clear()
print(sport)




fruits = ['cliavi', 'washing machine', 'cherry', 'orange']

x = fruits.copy()
print(x)




player=['messi', 'ronaldo', 'nazario', 'carlos',]

x = player.count("messi")
print(x)



fruits = ['apple', 'banana', 'cherry']

cars = ['mersedes', 'BMW', 'bugat']

fruits.extend(cars)
print(fruits)


fruits = ['washing machine', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)




fruits = ['mango', 'washing machine', 'cherry']

fruits.insert(1, "orange")
print(fruits)




fruits = ['mango', 'cliavi', 'cherry']

fruits.pop(1)
print(fruits)



fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")
print(fruits)






fruits = ['mango', 'cliavi', 'cherry']

fruits.reverse()
print(fruits)





cars = ['cls63amg', 'BMW', 'brabus']

cars.sort()
print(cars)