# 1) შექმენით ცვლადი რომლის მნიშვნელობა იქნება lambda ფუნქცია, რომელიც გაყოფს 2 რიცხვს ერთმანეთზე. შემდეგ კი გამოიძახეთ ეს ფუნქცია.
func1 = lambda a,b: a / b
print(func1(30, 10))
# 2) შექმენით ცვლადი რომლის მნიშვნელობა იქნება lambda ფუნქცია, რომელიც დააჯამებს 3 რიცხვს. შემდეგ კი გამოიძახეთ ეს ფუნქცია
func2 = lambda a,b,c: a+b+c
print(func2(8, 8, 8))
# 3) შექმენით ცვლადი რომლის მნიშვნელობა იქნება lambda ფუნქცია, რომელიც შეაერთებს 3 სტრინგს. შემდეგ კი გამოიძახეთ ეს ფუნქცია.
func3 = lambda a, b, c: a+b+c
print(func3("niiko", "nika", "nikoloz"))
# 4) შექმენით ცვლადი რომლის მნიშვნელობა იქნება lambda ფუნქცია, რომელიც მიიღებს რიცხვს და გაამრავლებს 10'ზე. შემდეგ კი გამოიძახეთ ეს ფუნქცია
func4 = lambda a,b: a * b
print(func4(5, 5))