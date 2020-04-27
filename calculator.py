import sys
from typing import Union

def add(a: int, b: int) -> int:
    return a + b

def deduct(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def division(a: int, b: int) -> Union[int, float]:
    if b == 0:
        print("Nie można dzielić przez 0!")
        return 0
    return a / b

def wrong_choice():
    print("Dokonałeś złego wyboru !")
    sys.exit()

a = round(float(input("Podaj pierwszą liczbę: ")))
b = round(float(input("Podaj drugą liczbę: ")))
c = input("Podaj rodzaj działania: 1 - add, 2 - deduct, 3 - multiply, 4 - division: ")
result_dispacer = {'1': add,
'2': deduct,
'3': multiply,
'4': division}
if not c in result_dispacer:
    wrong_choice()
result = result_dispacer[c](a, b)


# if c =='1':
#     result = add(a, b)
# elif c == '2':
#     result = deduct(a, b)
# elif c == '3':
#     result = multiply(a, b)
# elif c == '4':
#     result = division(a, b)
# else:
#     wrong_choice()

print(f"Wynik działania to: {result}")



