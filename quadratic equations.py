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

        frac1 = Fraction(x1f1, x1f2)
        sign1 = -1 if frac1 < 0 else 1
        abs_frac = abs(frac1)

        whole1 = abs_frac.numerator // abs_frac.denominator
        rest1 = abs_frac.numerator % abs_frac.denominator

        x2f1 = int(-b + Discriminant**0.5)
        x2f2 = int(2 * a)

        frac2 = Fraction(x2f1, x2f2)
        sign2 = -1 if frac2 < 0 else 1
        abs_frac = abs(frac2)

        whole2 = abs_frac.numerator // abs_frac.denominator
        rest2 = abs_frac.numerator % abs_frac.denominator
        if frac1 == frac2 and Discriminant == 0:
            print(f"you have one x. Your x = {frac1}")    
        else:
            if rest1 == 0:
                print("x1 =", sign1 * whole1)
            elif whole1 > 0:
                print(f"x1 = {sign1 * whole1} {rest1}/{abs_frac.denominator}")
            else:
                print(f"x1 = {frac1}")
            if rest2 == 0:
                print("x2 =", sign2 * whole2)
            elif whole2 > 0:
                print(f"x2 = {sign2 * whole2} {rest2}/{abs_frac.denominator}")
            else:
                print(f"x2 = {frac2}")

