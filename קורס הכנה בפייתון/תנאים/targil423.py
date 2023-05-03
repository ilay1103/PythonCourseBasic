temperture = input("Insert the temperture you would like to convert: ").lower()
temperture_value = 0

temperture_value = float(temperture[:len(temperture)-1])

new_temperture=0
if temperture[-1] == 'c':
	new_temperture = ((temperture_value * 9 + (32 * 5)) / 5)
	print(str(new_temperture)+'F')
elif temperture[-1] == 'f':
	new_temperture = ((temperture_value * 5 - 160) / 9)
	print(str(new_temperture)+'C')