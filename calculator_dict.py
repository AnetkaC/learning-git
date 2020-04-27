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

print(f"Wynik działania to: {result}")



