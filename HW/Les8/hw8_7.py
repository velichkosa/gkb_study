"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""

class C_number:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return C_number((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return C_number((self.a * other.a) - (self.b * other.b), ((self.a * other.b)+(self.b * other.a)))

    def __str__(self):
        znak = ''
        if self.b > 0:
            znak = '+'
        return f'z = {self.a} {znak} {self.b} * i'


z1 = C_number(1, -2)
z2 = C_number(3, 4)

print(z1 + z2)
print(z1 * z2)

