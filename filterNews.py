import unsortedMap

d = unsortedMap.makeDictionary()
print(d)

while True:
	msg = input("Enter a word to search\n")
	if msg not in d:
		print('0.0')
	else:
		print(d[msg])

	print("\nNEXT")