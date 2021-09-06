# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

company_dict = {'name': [],
                'profit_1': [],
                'profit_2': [],
                'profit_3': [],
                'profit_4': [],
                'profit_avr': []}

num = input('Введите количество предприятий: ')

for i in range(int(num)):
    name = input('Введите название предприятия: ')
    company_dict['name'].append(name)
    a, b, c, d = (float(i) for i in input('Введите прибыль за 4 квартала (4 числа через пробел): ').split())
    company_dict['profit_1'].append(a)
    company_dict['profit_2'].append(b)
    company_dict['profit_3'].append(c)
    company_dict['profit_4'].append(d)
    company_dict['profit_avr'].append((a + b + c + d)/4)

bad_company = []
good_company = []
for i in range(int(num)):
    if company_dict['profit_avr'][i] < sum(company_dict['profit_avr'])/len(company_dict['profit_avr']):
        bad_company.append(company_dict['name'][i])
    elif company_dict['profit_avr'][i] > sum(company_dict['profit_avr'])/len(company_dict['profit_avr']):
        good_company.append(company_dict['name'][i])

#print(company_dict)
print(f'Компании с прибылью ниже среднего: {bad_company}\nКомпании с прибылью выше среднего: {good_company}')







