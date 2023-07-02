"""Practice factoring"""
"""As of right now, unfactorable problems are included and therefore won't factor.
This will have to be changed so that the equations actually factor"""
import sympy
from sympy import Symbol
import random

x = Symbol("x")
def main():
    eq_generator(3)

def ask_question(eq):
    print("factor this equation:", eq)
    answers = [input(":>")]
    print(answers)
    print(sympy.factor(eq))

def eq_generator(y=10):
    #Create x number of factoring problems
    for eq in range(y+1):
        term1 = random.randint(1, 10)
        term2 = random.randint(5, 30)
        if term1 // term2 == 0:
            eq = x ** 2 + term1 * x + term2
            ask_question(eq)


if __name__ == '__main__': main()