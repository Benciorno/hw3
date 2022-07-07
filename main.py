# 1
# def choose(first, second):
#     try:
#         return first + second
#     except TypeError:
#         return f'{first}{second}'
#
#
# print(choose(1, 'abc'))


# 2
# import re
#
# sample = 'Exercises number 1, 12, 13 and 345 are important 456'
# print(re.findall(r'\d{3}', sample))

# 3
# food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
# fifth = []
# for x in food:
#     try:
#         fifth.append(x[4])
#     except IndexError:
#         pass
# print(fifth)
# 4
# import re
#
# sample = 'Веб-цвета — методы описания и определения этих цветов. Например - #123ABC'
# print(re.findall(r'[A-Z0-9a-z]{6}', sample))

# 5
# import re
#
# sample = 'Завтрак в 09:00'
# print(re.findall(r'[0-2][0-9]:[0-6][0-9]', sample))

# 6
