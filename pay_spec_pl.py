#Pyta o liczbę przepracowanych godzin
hrs = input("Enter Hours:")
#Wczytuje wartość jako liczbę zmiennoprzecinkową
h = float(hrs)
#Pyta o stawkę godzinową
ra = input ("Enter Rate:")
#Wczytuje wartość jako liczbę zmiennoprzecinkową
r = float(ra)
#Stawia warunek kiedy stawka godzinowa ma być liczbą stałą
if h <= 40:
    x = h * r
    print(x)
#Gdy wystąpią nadgodziny stawka godzinowa zwiększa się
elif h > 40:
    x = ((40 * r) + ((h - 40) * 1.5 * r))
    print(x)