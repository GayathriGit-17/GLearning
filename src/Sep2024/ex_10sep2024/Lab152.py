import math

try:
    math.exp(1000)  # Overflow error : math range error
except Exception as e:
    print(e)
