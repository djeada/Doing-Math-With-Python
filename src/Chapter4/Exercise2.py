"""
Exercise 2
Write a program that asks the user for two expressions and then graphs them
both,as follows:
>>> expr1 = input('Enter your first expression in terms of x and y: ')
>>> expr2 = input('Enter your second expression in terms of x and y: ')
Once you've complete this, enhance your program to print the solution - the pair
of x and y values that satisfies both equation. This will also be the spot 
where the two lines on the graph intersect. (Hint: Refer to how we used to the
solve () function earlier to find the solution of a system of two linear 
equations)

"""

from sympy import plot, solve, sympify
from sympy.core.sympify import SympifyError
from sympy import Symbol


expr1 = input("Enter your first expression in terms of x and y: ")
expr2 = input("Enter your second expression in terms of x and y: ")

try:
    expr1 = sympify(expr1)
    expr2 = sympify(expr2)

except SympifyError:
    print("Invalid input")


x = Symbol("x")
y = Symbol("y")

# plot(expr1,expr2)
print(solve(expr1, expr2, dict=True))
