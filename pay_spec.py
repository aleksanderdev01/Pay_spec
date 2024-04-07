hrs = input("Enter Hours:")
h = float(hrs)
ra = input ("Enter Rate:")
r = float(ra)
if h <= 40:
    x = h * r
    print(x)
elif h > 40:
    x = ((40 * r) + ((h - 40) * 1.5 * r))
    print(x)