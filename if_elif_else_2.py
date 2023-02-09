#Using UPPER INTERVALS

""" person < 2 (Baby)
    person >= 2 and < 4 (Toddler)
    person >= 4 and < 13 (Kid)
    person >= 13 and < 20 (Teenager)
    person >= 20 and < 65 (Adult)
    person >= 65 (Elder) """

age = int(input("Enter your age: "))

if age < 2:
    msg = 'Baby'

elif age < 4:
    msg = 'Toddler'

elif age < 13:
    msg = 'Kid'

elif age < 20:
    msg = 'Teenager'

elif age < 65:
    msg = 'Adult'

else:
    msg = 'Elder'

print(msg)
