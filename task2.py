# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print()
print("Данная программа принимает предикаты 0(Ложь) и 1(Истина) в качестве значений")
print()
print("и проверяет истинность следующего утверждения: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")

print()
X = int(input("Введите X: "))
print()
Y = int(input("Введите Y: "))
print()
Z = int(input("Введите Z: "))

if X > 1 or X < 0 or Y > 1 or Y < 0 or Z > 1 or Z < 0:
    print()
    print("Ошибка ввода. Введите, пожалуйста, значение 0(Ложь) или 1(Истина).")
else:
    phrase = not (X or Y or Z) == (not X) and (not Y) and (not Z)
    print()
    if phrase == True:
        print("Утверждение истинно!")
    elif phrase == False:
        print("Утверждение ложно!")
