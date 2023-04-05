# try:
#     print(5 /0)
# except ZeroDivisionError:
#     print('на ноль делить нельзя')

# num = input('введите число от 1 до 7')


# print(f'Вы ввели число {num}')
#
# if int(num) > 7 or int(num) < 1:
#     raise Exception('введите дни недели от 1 до 7')
#
#
# days_of_week = {
#     '1': 'Mon',
#     '2': 'Tue',
#     '3': 'Wed',
#     '4': 'Thu',
#     '5': 'Fr',
#     '6': 'Sa',
#     '7': 'Su'
# }
#
# print(days_of_week[num])

import datetime

def get_birth_year(age):
    this_year = datetime.date.today()
    birth_year = this_year.year - age
    return birth_year

if __name__ == '__main__':
    age = input('Введите ваш возраст: ')
    birth_year = get_birth_year(age)
    print(birth_year)
