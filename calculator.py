def add(a, b):
    return a + b

def deduct(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if (b == 0):
        print("Nie można dzielić przez 0!")
        return 0
    return a / b

def wrong_choice():
    print("Dokonałeś złego wyboru !")
    sys.exit()

a = round(float(input("Podaj pierwszą liczbę: ")))
b = round(float(input("Podaj drugą liczbę: ")))
c = input("Podaj rodzaj działania: 1 - add, 2 - deduct, 3 - multiply, 4 - division: ")
if (c =='1'):
    wynik = add(a, b)
elif (c == '2'):
    wynik = deduct(a, b)
elif (c == '3'):
    wynik = multiply(a, b)
elif (c == '4'):
    wynik = division(a, b)
else:
    wrong_choice()

print(f"Wynik działania to: {wynik}")




