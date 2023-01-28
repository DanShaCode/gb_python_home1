# Найдите сумму цифр трехзначного числа.

# Пример
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print()
print("Данная программа принимает на вход положительное трехзначное число ")
print("и выдает сумму цифр введеного числа.")
print()
num = int(input("Введите положительное трехзначное число: "))

if num < 100 or num > 999 or num < 0:
    print()
    print("Ошибка ввода. Число должно быть положительным трехзначным числом.")
else:
    firstNum = int(num/100)
    secondNum = int((num/10)) % 10
    thridNum = num % 10
    numSum = firstNum + secondNum + thridNum
    print()
    print("Сумма цифр числа", num, "->", numSum,"(", firstNum, "+", secondNum, "+", thridNum, ")")
