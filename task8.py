# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

print()
print("Введите номер билета и узнайте счастливый он или нет.")
print()
num = int(input("Ваш номер: "))

if num < 100000 or num > 999999 or num < 0:
    print()
    print("Ошибка ввода. Ваш билет должен содержать в себе 6 цифр и быть больше нуля.")
else:
    firstNum = int(num/100000)
    secondNum = int(num/10000) % 10
    thridNum = int(num/1000) % 10
    forthNum = int(num/100) % 10
    fifthNum = int(num/10) % 10
    sixNum = num % 10

    firstOfthree = firstNum + secondNum + thridNum
    lastOfthree = forthNum + fifthNum + sixNum
    
    if firstOfthree == lastOfthree:
        print()
        print("Ура! Ваш билет оказался счастливым.")
        print()
        print("Результат вычислений по вашему билеты под №", num, ":", firstNum,
              "+", secondNum, "+", thridNum, "=", forthNum, "+", fifthNum, "+", sixNum)
    else:
        print()
        print("Увы ... Ваш билет не является счастливым.")
