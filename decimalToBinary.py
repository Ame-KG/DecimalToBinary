# Decimal to Binary Logic:
# to get thebinary version of a number you must divide it by 2, take the remainder and store that 
# then divide the qotient and store the remainder again and keep doing this until the quotient = 0
# at that point all the remainders will give you the binary version of that number

# Implementation


binary = ''

# Iitialisaton Function
def deciToBinary(decimal):
	recursor(decimal)
	return binary

# Logic Function
def recursor(decimal):
	# qotient and remainder tracker
	qoutient = decimal // 2
	remainder = decimal % 2
	global binary
	binary += str(remainder)

	if qoutient == 0:
		return binary

	recursor(qoutient)

print(deciToBinary(13))