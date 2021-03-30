"""
2.*	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""


class HexNum:
    def __init__(self, numb):
        self.numb = "".join(numb)

    def __add__(self, other):
        return list(f"{(int(self.numb, 16) + int(other.numb, 16)):X}")

    def __mul__(self, other):
        return list(f"{(int(self.numb, 16) * int(other.numb, 16)):X}")


num_1 = HexNum(list(input("Введите первое число 16 - ричной системы: ")))
num_2 = HexNum(list(input("Введите второе число 16 - ричной системы: ")))

print("Сложение:", num_1 + num_2)
print("Умножение:", num_1 * num_2)


