def calc_area (l, w):
    return (l*w)
area1 = calc_area(4,5)
print(area1)

def is_even(a):
    if a % 2 == 0:
        return("Even")
    else:
        return("Odd")
print(is_even(5))

def square(s):
    return s*s
print(square(4))

def is_positive(p):
    if p > 0:
        return("True")
    else:
        return("False")
print(is_positive(-2))

def full_price(quantity, unit_price):
    return (quantity * unit_price)
total_cost = full_price(12, 2500)

print(total_cost * 1.8)

def convert_to_ugx(usd_amount, rate):
    return(usd_amount * rate)

converted = convert_to_ugx(50, 3800)
final = converted + 10000
print(final)

def cel_to_fah(temp):
    return (temp * 9/5) + 32

def describe_weather(c):
    return(f"The weather right is: {cel_to_fah(c)}")
print(describe_weather(25))



