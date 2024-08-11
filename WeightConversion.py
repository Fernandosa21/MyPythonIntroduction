weight = float(input('Weight: '))
unit = input('(K)g or (L)bs: ').upper()

if unit == 'K':
    # Lbs conversion
    print("Wight in Lbs: " + str(weight - 2.2046))
elif unit == 'L':
    # Kg conversion
    print("Wight in Kg: " + str(weight / 2.2046))
else:
    print('Unknown value')
