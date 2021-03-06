# Напишите программу, которая находит сумму, произведение и среднее арифметическое трёх целых чисел, введённых с клавиатуры.
#
# Входные данные
# Три целых числа вводятся в одной строке через пробелы.
#
# Выходные данные
# Программа должна вывести сумму, произведение и среднее арифметическое введенных чисел. Среднее арифметическое нужно вывести с точностью 3 знака после десятичной точки

a = int(input())
b = int(input())
c = int(input())
print('{}+{}+{}={}'.format(a, b, c, a+b+c))
print('{}*{}*{}={}'.format(a, b, c, a*b*c))
print('({}+{}+{})/3={:.3f}'.format(a, b, c, (a+b+c)/3))

# второй вариант format
a = int(input())
b = int(input())
c = int(input())
print(f'{a}+{b}+{c}={a+b+c}')
print(f'{a}*{b}*{c}={a*b*c}')
print(f'({a}+{b}+{c})/3={(a+b+c)/3:.3f}')
