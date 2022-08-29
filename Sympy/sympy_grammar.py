from sympy.abc import x, y
from re import T
from sympy.abc import x, y, pi  # 引进符号变量x,y及常量pi
from sympy import *
# 注意全局引用, 避免发生错误

# symbols()--构建符号变量--
x, y, z = symbols('x y z')
# m0,m1,m2,m3=symbols('m0:4') # 创建多个符号变量

# 变量不多时的写法

# n()或evalf()--取一个数的浮点近似值
print(pi.n())  # 默认保留15位有效数字
print("pi的两种显示格式:{}{}".format(pi, pi.evalf(3)))  # format里不能使用n()函数

# sub()--求值、替换
# 1. 求值
expr1 = y*sin(y**2)
expr2 = y**2+sin(y)*cos(y)+sin(z)
print("y=5时, expr1=", expr1.subs(y, 5))
print("y=2, z=3时, expr2=", expr2.subs({y: 2, z: 3}))
# 2. 替换
x, y = symbols('x,y')
a = x+1
print(a.subs(x, y))

# together()--表达式相加
# simplify(), apart()--化简
x1, x2, x3, x4 = symbols('m1:5')
print(together(x1/x2+x3/x4))
x = symbols('x')
print(simplify((2**x**2+3*x+4)))

# expand()--拓展代数表达式, 消除幂和乘法
expr = sin(x+y)/(sin(y)*cos(x))
print(expr)
expr = simplify(expr)
print(expr)

# equals()--比较表达式
a = cos(x)**2-sin(x)**2
b = cos(2*x)
print(a.equals(b))
print(a == b)

# solve()--求解方程
sol = solve(x**2-x, x)  # x^2 - x = 0
print(sol)

# solveset()--求给定目标区间内的解
sol = solveset(x**2-1, x, Interval(0, 50))  # 解在区间 (0, 50)
print(sol)
sol2 = solveset(x**2-1, x, Interval(-10, 50))  # 解在区间 (-10, 50)
print(sol2)

# limit()--求极限
print(limit(sin(x)/x, x, 0))
print(limit(pow(1+1/x, x), x, oo))  # oo 表示 +∞

# diff()--求导
# diff(func:求导的函数, x:要对其求导的变量, n:可选, 求n阶导数, 默认为1阶导数)
x, y = symbols('x y')  # 定义两个符号变量
z = sin(x)+x**3**exp(y)
print("关于x的二阶偏导数为: ", diff(z, x, 2))
print("关于y的一阶偏导数为: ", diff(z, y))
print("函数对x先求偏导, 然后对y求偏导: ", diff(z, x, y))
# 求某一点的导数
print(diff(x**4, x).subs(x, 2))

# summation()--级数的求和
# factor()--因式分解
k, n = symbols('k n')
print(summation(k**2, (k, 1, n)))
print(factor(summation(k**2, (k, 1, n))))
print(summation(1/k**2, (k, 1, oo)))

# intergreate()--求不定积分与定积分
# 1. 不定积分
expr = exp(x)*sin(x)+exp(x)*cos(x)
print(integrate(expr, x))
# 2. 定积分
print(integrate(sin(x)/x, (x, 0, oo)))

# solve()/roots--方程(组)求解
print(solve(x**3-4*x**2-3*x+18))
print(roots(x**3-4*x**2-3*x+18))  # 如果要求多重根重复次数可以用roots
print(solve([x-y+2, x+y-3], [x, y]))  # 求解方程组

# Function()--声明微分方程
y = Function('y')
y = symbols('y', cls=Function)

