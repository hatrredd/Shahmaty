i = 0;
while i != 1:
    k, l = map(int, input("Введите через пробел первую пару натуральных чисел, не превышающих 8: ").split())            # Ввод 2 переменных с разделением(функция .split()) по пробелу
    m, n = map(int, input("Введите через пробел вторую пару натуральных чисел, не превышающих 8: ").split())
    if (k == m) and (l == n):
        print("\nЭто одна и та же клетка, попробуйте ещё раз\n")
    elif (k >= 1 and k <= 8) and (l >= 1 and l <= 8) and (m >= 1 and m <= 8) and (n >= 1 and n <= 8):
        i += 1
    else: print("\nНе соблюдены условия ввода, попробуйте ещё раз\n")
k2 = k; l2 = l
razn1 = abs(k - m); razn2 = abs(l - n)
razn = razn1 + razn2
if (k%2 == 0 and l%2 != 0) or (k%2 != 0 and l%2 == 0):
        colour1 = "b"
else: colour1 = "w"
if (m%2 == 0 and n%2 != 0) or (m%2 != 0 and n%2 == 0):
        colour2 = "b"
else: colour2 = "w"
if colour1 == colour2:
    print("Клетки (", k, ",", l,") и (", m, ",", n, ") одного цвета", sep="")
else: print("Клетки (", k, ",", l,") и (", m, ",", n, ") разных цветов", sep="")
figure = input("\n\nВведите одну из данных фигур: Ферзь, Ладья, Слон, Конь: ")
figure = figure.lower()         #.lower меняет все буквы на строчные
while i != 0:
    if figure != "ферзь" and figure != "ладья" and figure != "слон" and figure != "конь":
        figure = input("\n\nВведено неправильное название фигуры, попробуйте ещё раз: ")
        figure = figure.lower()
    else:
        i -= 1
        if figure == "ладья" and (k == m or l == n):
                print(figure.capitalize() + " угрожает клетке (", m,",", n, ")", sep="")           #.capitalize меняет первую букву на заглавную
        elif figure == "слон" and (razn1 == razn2):
                print(figure.capitalize() + " угрожает клетке (", m,",", n, ")", sep="")           #sep="" убирает пробелы между словами, которые есть по умолчанию
        elif (figure == "конь") and ((k-m == 1 or k-m == -1) and (l-n == 2 or l-n == -2)) or ((k-m == 2 or k-m == -2) and (l-n == 1 or l-n == -1)):
                print(figure.capitalize() + " угрожает клетке (", m,",", n, ")", sep="")
        elif (figure == "ферзь") and ((k-m==1 or k-m == -1) and (l-n == 1 or l-n == -1) or (k == m or l == n) or (abs(k-m) == abs(l-n))) :
                print(figure.capitalize() + " угрожает клетке (", m,",", n, ")", sep="")
        else:
            print(figure.capitalize() + " не угрожает клетке (", m,",", n, ")", sep="")
            if figure == "слон" and colour1 != colour2:
                print("Не может угрожать клетке (", m, ",", n,"), так как не может попасть на клетку другого цвета", sep="")
            elif figure == "слон":
                if (k + razn//2 <=8) and (l + razn//2 <= 8):
                    k2 += razn//2; l2 += razn//2
                elif (k + razn//2 >8) and (l + razn//2 > 8):
                    k2 -= razn//2; l2 -= razn//2
                elif (k + razn//2 <=8) and (l + razn//2 > 8):
                    k2 += razn//2; l2 -= razn//2
                elif (k + razn//2 >8) and (l + razn//2 <= 8):
                    k2 -= razn//2; l2 += razn//2
                print(figure.capitalize() + " при переходе с клетки (", k, ",", l, ") на клетку (", k2,",", l2,") угрожает клетке (", m,",",n,")", sep="")
            elif figure == "ладья" or figure == "ферзь":
                if k > m:
                    k2 -= k-m
                elif k < m:
                    k2 += m-k
                print(figure.capitalize() + " при переходе с клетки (", k, ",", l, ") на клетку (", k2, ",", l, ") угрожает клетке (", m,",",n,") - первый вариант хода", sep="")
                if  l > n:
                    l2 -= l-n
                elif l < n:
                    l2 += n-l
                print(figure.capitalize() + " при переходе с клетки (", k, ",", l, ") на клетку (", k, ",", l2, ") угрожает клетке (", m,",",n,") - второй вариант хода", sep="")