# Даны три натуральных числа a, b, c, записанные в отдельных строках.
# Определите, существует ли неворожденный треугольник с такими сторонами.

a = int(input())
b = int(input())
c = int(input())

if (a < b + c) or (b < a + c) or (c < a + b):
    print("Yes")
else:
    print("no")