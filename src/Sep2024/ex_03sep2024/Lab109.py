# from src.Aug2024.ex_31082024.Lab107 import sleep2

# calc
m=10
class Calc:

    def sum(self, a, b):
        return a + b

    def diff(self, a, b):
        return a - b
        global m
        m="Hi"

    def product(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calc_obj = Calc()

output_sum = calc_obj.sum(3, 4)
output_sum = calc_obj.diff(3, 4)
print(output_sum)
print(m)
