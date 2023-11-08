# Decimal to Binary Logic:
# to get thebinary version of a number you must divide it by 2, take the remainder and store that 
# then divide the qotient and store the remainder again and keep doing this until the quotient = 0
# at that point all the remainders will give you the binary version of that number

# Implementation


# Version 2:
# Primary goal is to use only one function for the recursion this time
# Secondary goal is to be able to make negative numbers work as well

binary = ''

# Iitialisaton Function
def deciToBinary(decimal):
	global binary
	if decimal < 0:
		binary += '-'
		decimal = decimal * -1

	# qotient and remainder tracker
	qoutient = decimal // 2
	remainder = decimal % 2
	binary += str(remainder)

	if qoutient == 0:
		return binary

	deciToBinary(qoutient)

	return binary


print(deciToBinary(-13))