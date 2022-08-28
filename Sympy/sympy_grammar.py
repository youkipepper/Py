from sympy import *

# expand
x, y = symbols("x y")

print(expand((x+y)**2))
print(expand((x+y)**3))
print(expand(cos(x+y), trig=True))

# simplify
