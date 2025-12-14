import math
from fractions import Fraction
a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))
Discriminant = b*b - 4*a*c
print(f"your Discriminant = {Discriminant}")

if Discriminant < 0:
    print("Don't have roots!")
else:
    sqrt_D = math.sqrt(Discriminant)
    print(f"your root of Discriminant {sqrt_D}")

    if not sqrt_D.is_integer():
        print(f"Discriminant not perfect square")
        print(f"answer: x1 = (-{b} - √{Discriminant}) / {2*a}")
        print(f"answer: x2 = (-{b} + √{Discriminant}) / {2*a}")
    else:
        x1f1 = int(-b - sqrt_D)
        x1f2 = 2 * a
        x2f1 = int(-b + sqrt_D)
        x2f2 = 2 * a
        
        frac1 = Fraction(x1f1, x1f2)
        sign1 = -1 if frac1 < 0 else 1
        abs_frac1 = abs(frac1)
        whole1 = abs_frac1.numerator // abs_frac1.denominator
        rest1 = abs_frac1.numerator % abs_frac1.denominator

        frac2 = Fraction(x2f1, x2f2)
        sign2 = -1 if frac2 < 0 else 1
        abs_frac2 = abs(frac2)
        whole2 = abs_frac2.numerator // abs_frac2.denominator
        rest2 = abs_frac2.numerator % abs_frac2.denominator
        
        if frac1 == frac2:
            print(f"you have one x. Your x = {frac1}")
        else:
            if rest1 == 0:
                print("x1 =", sign1 * whole1)
            elif whole1 > 0:
                print(f"x1 = {sign1 * whole1} {rest1}/{abs_frac1.denominator}")
            else:
                print(f"x1 = {frac1}")

            if rest2 == 0:
                print("x2 =", sign2 * whole2)
            elif whole2 > 0:
                print(f"x2 = {sign2 * whole2} {rest2}/{abs_frac2.denominator}")
            else:
                print(f"x2 = {frac2}")
