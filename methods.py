season = "Summer"
print(season.upper())
print(season.find('mer'))
print(season.replace('m', '3'))


temperature = 15

if temperature > 30:
    print("It's a hot day")
elif temperature < 20:
    print("It's cold")
else:
    print("DOne")


weight = int(input("Weight: "))
kilogram_or_pound = input("(K)g or (L)bs: ")
weight_converted_to_kg = int(weight) * 0.45
weight_converted_to_lbs = int(weight) / 0.45

if kilogram_or_pound == "k":
    print("Weight in lbs: " + str(weight_converted_to_kg))
else:
    print("Weight in kg: " + str(weight_converted_to_lbs))




