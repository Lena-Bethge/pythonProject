# Напишите программу, которая получает три числа и выводит количество одинаковых чисел в этой цепочке.
# Программа должна вывести количество одинаковых чисел из переданного ей набора или число 0, если все числа различные.

number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1 == number2 == number3:
    print(3)
elif (number1 == number2) or (number2 == number3) or (number1 == number3):
    print(2)
else:
    print(0)