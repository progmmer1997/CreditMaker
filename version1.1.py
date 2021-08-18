# возрастной коэффициент, который влияет на платёжеспособность12
# возраст, размер кредита и количество месяцев
age_coeff = 0
credit_time = int(input("На какое время вы берете кредит:"+" "))  # Вреия, на которое берется кредит
credit_size= int(input("Укажите размер кредита:"+" "))  # размер кредита
percent = int(input("Под какой процент?:"+" "))  # процент
age = int(input("Введите Ваш возраст?:"+" "))  # возраст клиента
SalarySize = int(input("Введите размер своего ежемесячного дохода"+" "))  # Размер зарплаты
personal_expense = int(input("Введите размер ежемесячных трат:"+""))  # личные траты
childrenCount = int(input("Введите количество детей:"+" "))  # количество детей

child_expense = int(input("Введите траты на детей в месяц: "+" "))
expense = personal_expense + child_expense
# Изначально предполагаетсячто у клиента нет детейт.н. траты на них равны  0
child_expense = 0
# если клиенту больше 55 лет, устанавливаем повышенный коэффициент риска
if (age > 55):
    age_coeff = 3
# если не больше, чем 55 — устанавливаем стандартный возрастной коэффициент
else:
    age_coeff = 2
if childrenCount == 1:
    child_expense = 10000
else:
    child_expense = childrenCount * 8000
payment_of_month = ((credit_size + (credit_size * percent / (12 * 100)) * credit_time))//credit_time  # ежемесячный платёж
required_salary = (payment_of_month * age_coeff) + expense  # рекомендуемая зарплата
print("Ежемесячная платеж :"+" " + str(
    payment_of_month) + "\n" + "Для одобрения кредита ваша зарплата должна составлять:"+" " + str(required_salary))

