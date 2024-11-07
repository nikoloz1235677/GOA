# 1) ჩამოთვალეთ ყველა დღეს ნასწავლი error'ის ტიპი და ახსენით რა რა შემთხვევაში გამოდის
# 2) დაწერეთ ისეთი კოდი სადაც იქნება NameError და გაუმკლავდით try/except'ით
# 3) დაწერეთ ისეთი კოდი სადაც იქნება IndexError და გაუმკლავდით try/except'ით
# 4) დაწერეთ ისეთი კოდი სადაც იქნება ValueError და გაუმკლავდით try/except'ით
# 5) კომენტარებით ახსენით რაში გვადგება try/except


# sintax error  aris pythonis codis nawili indentacia






fruit = "apple"

try:
    print(fruit)
except NameError:
    print("...")




cars = ['bmw', 'mercedes', 'opel'] 
try:
    print(cars[3]) 
except IndexError:
    print("...")



try:
    number = int("no num")
except ValueError:
    print("არ არის როცხვი")
