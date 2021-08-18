# personal data collecting
age_coeff = 0
minumal_income = 30000  # минимальный требуемый доход
general_income = 0  # общий доход
additional_income_Size = 0 # ополнительный доход
living_wage = 13000  # прожиточный минимум
child_expense = 0
credit_time = int(input(" На какое время хотите взять кредит?"+" "))
credit_size = int(input("Укажите размер кредита:"+" "))
percent = int(input("Под какой процент?:"+" "))
age = int(input("Укажите ваш возраст:"+""))
salarySize = int(input("Введите размер своего ежемесячного дохода"+" "))  # Размер зарплаты
additional_income= input("у вас есть дополнительные источники дохода")
if additional_income == "есть" or additional_income == "да":
    additional_income_Size = int(input("Введите размер дополнительного дохода"))
    general_income = salarySize+additional_income_Size
else:  general_income = salarySize
personal_expence = int(input("Введите уровень личных затрат затратв месяц"))
childrenCount = int(input("Введите количество детей:"+" "))  # количество детей
child_expense = int(input("Введите траты на детей в месяц"+" "))
expense = personal_expence + child_expense
workTime = int(input("Введите свой стаж работы в месяцах "))
last_work_space = int(input("Введите срок,который в проработали на последнем месте работы в месяцах"))
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
expense = personal_expence + child_expense
payment_of_month = ((credit_size + (credit_size * percent / (12 * 100)) * credit_time)) //credit_time # ежемесячный платёж
required_salary = (payment_of_month * age_coeff) + expense  # рекомендуемая зарплата
remaining_funds = general_income-payment_of_month # осиаток средств после выплаты кредита
if salarySize > minumal_income and remaining_funds >= living_wage and workTime > 12 and last_work_space >= 6:
    print("Ваш кредит одобрен."+" "+" Ежемесячный платеж составит "+" "+str(payment_of_month))
else : print("Кредит не одобрен. "+ " "+ " Для одобрения кредита ваша зарплата должна быть не менее"+" "+str(required_salary))