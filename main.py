"""
Program name: FactorPractice
Date of first writing: 07/02/2023
Author: Sam Goldberg
"""


import sympy
from sympy import Symbol
import random

x = Symbol("x")
def main():
    term_generator()

def ask_question(eq):
    print("factor this equation:", eq)
    answers = [input(":>")]
    print(answers)
    print(sympy.factor(eq))

def term_generator():
    #Create two factorable terms
    term1 = random.randint(2, 4)
    term2 = random.randint(8, 12)
    is_factorable(term1, term2)
    eq_generator(term1, term2)

def eq_generator(t1, t2):
     eq = x**2 + t1*x + t2
     ask_question(eq)

def is_factorable(term, tterm):
    #Stuck at trying to make sure the factors for term one are the same as term two, but only used in adding
    #if (sympy.isprime(term) == True) and (sympy.isprime(tterm) == True) and 
            term_generator()


if __name__ == '__main__': main()