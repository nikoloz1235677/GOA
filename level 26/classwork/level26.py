1                                                                                                                                                                     def  greet(name):
    """
    ეს ფუნქცია მიესალმება ადამიანს, რომლის სახელიც მიაწვდოს.
    :param name: პიროვნების სახელი (სტრინგი)
    :return: დასალმებელი შეტყობინება (სტრინგი)
    """
    return f"გამარჯობა, {name}!"

ფუნქციის ტესტირება
print(greet("გიორგი"))
print(greet("ანა"))
2                                                                                                                                                                                             def wish_success(name):
    """
    ეს ფუნქცია უსურვებს წარმატებას ადამიანს, რომლის სახელიც მიაწვდოს.
    :param name: პიროვნების სახელი (სტრინგი)
    :return: წარმატების სურვილი (სტრინგი)
    """
    return f"წარმატებები, {name}! გისურვებთ საუკეთესო წარმატებებს თქვენს საქმიანობაში!"

ფუნქციის ტესტირება
print(wish_success("გიორგი"))
print(wish_success("ანა")) 
3                                                                                                                                                                            def remind_lesson(name, lesson, date):
    """
    ეს ფუნქცია შეახსენებს ადამიანს გაკვეთილის დროით და სახელს.
    :param name: პიროვნების სახელი (სტრინგი)
    :param lesson: გაკვეთილის სახელი (სტრინგი)
    :param date: გაკვეთილის თარიღი და დრო (სტრინგი)
    :return: გაფრთხილება გაკვეთილის შესახებ (სტრინგი)
    """
    return f"მოითხოვე გახსოვდეს, {name}! გაქვს გაკვეთილი '{lesson}' {date}-ზე."

ფუნქციის ტესტირება
print(remind_lesson("გიორგი", "GOA", "08/11/2024 12:17 PM"))
print(remind_lesson("ანა", "GOA", "08/11/2024 12:17 PM"))
4                                                                                                                                                                                  def greet_person(name):
    """
    ეს ფუნქცია მიესალმება ადამიანს, რომლის სახელიც მიაწვდოს.
    :param name: პიროვნების სახელი (სტრინგი)
    :return: დასალმებელი შეტყობინება (სტრინგი)
    """
    # მორგებული დასალმება
    greeting = f"გამარჯობა, {name}! როგორ ხარ?"
    return greeting

ფუნქციის ტესტირება
print(greet_person("გიორგი"))
print(greet_person("ანა"))
5                                                                                                                                                                                  def check_adulthood(age):
    """
    ეს ფუნქცია შეამოწმებს, არის თუ არა პიროვნება სრულწლოვანი.
    :param age: პიროვნების ასაკი (integer)
    :return: შეტყობინება იმის შესახებ, არის თუ არა სრულწლოვანი (სტრინგი)
    """
    if age >= 18:
        return "გილოცავ! შენ სრულწლოვანი ხარ."
    else:
        return "სამწუხაროდ, შენ არასრულწლოვანი ხარ."

ფუნქციის ტესტირება
print(check_adulthood(20))  # სრულწლოვანი
print(check_adulthood(15))  # არასრულწლოვანი
saba shubitidze (დეკას რაზმი)  Today at 10:47 PM
6                                                                                                                                                                                    def assess_financial_status(salary):
    """
    ეს ფუნქცია შეაფასებს ადამიანის ფინანსურ მდგომარეობას ხელფასის მიხედვით.
    :param salary: ადამიანის ხელფასი (integer ან float)
    :return: ფინანსური მდგომარეობის შეფასება (სტრინგი)
    """
    if salary < 2000:
        return "ღარიბია"
    elif 2000 <= salary <= 5000:
        return "გაწონასწორებული"
    else:
        return "მდიდარი"

ფუნქციის ტესტირება
print(assess_financial_status(1500))  # ღარიბია
print(assess_financial_status(3000))  # გაწონასწორებული
print(assess_financial_status(6000))  # მდიდარი



