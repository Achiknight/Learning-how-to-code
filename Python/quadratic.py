from sympy import symbols,Eq,solve


x = symbols("x")

exp = (x**2) + 4*x - x + 4 = 0
res = solve(exp,x)
print(res)