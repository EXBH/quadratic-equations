from fractions import Fraction
import math
a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))

Discriminant = b*b - 4*a*c
sqrt_D = math.sqrt(Discriminant)  
print(f"your Discriminant = {Discriminant}")
print(f"your root of Discriminant {Discriminant ** 0.5}")
if Discriminant < 0:
    print(" don't have root! ")
else:
    if not sqrt_D.is_integer():
        print(f"Discriminant not equal type INT")
        print(f"answer: x1 = {-b} - √{Discriminant} / {a*2}")
        print(f"answer: x2 = {-b} + √{Discriminant} / {a*2}")
    else:    
        x1f1 = int(-b - Discriminant**0.5)
        x1f2 = int(2 * a)

        frac = Fraction(x1f1, x1f2)
        sign = -1 if frac < 0 else 1
        abs_frac = abs(frac)

        whole = abs_frac.numerator // abs_frac.denominator
        rest = abs_frac.numerator % abs_frac.denominator

        if rest == 0:
            print("x1 =", sign * whole)
        elif whole > 0:
            print(f"x1 = {sign * whole} {rest}/{abs_frac.denominator}")
        else:
            print(f"x1 = {frac}")

        x2f1 = int(-b + Discriminant**0.5)
        x2f2 = int(2 * a)

        frac = Fraction(x2f1, x2f2)
        sign = -1 if frac < 0 else 1
        abs_frac = abs(frac)

        whole = abs_frac.numerator // abs_frac.denominator
        rest = abs_frac.numerator % abs_frac.denominator

        if rest == 0:
            print("x2 =", sign * whole)
        elif whole > 0:
            print(f"x2 = {sign * whole} {rest}/{abs_frac.denominator}")
        else:
            print(f"x2 = {frac}")

