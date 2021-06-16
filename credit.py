'''
Write a program that prompts the user for a credit card number and then by using Luhn’s Algorithm,
reports (via print) whether it is a valid American Express, MasterCard, or Visa card number.
So that we can automate some tests of your code, we ask that your program’s last line of output 
be AMEX and print() or MASTERCARD and print() or VISA and print() or INVALID and print(),
nothing more, nothing less.
'''


def luhn_algo(cc):
	luhns_list = []

	# For anyone reason someone wants to test this fuctinon itself (not through valid_creditcard()), create a list of CC numbers
	# Otherwise this line of code below can be deleted 
	cc = [y for y in cc]

	# Take even index numbers from list of digits.
	for i in range(0,len(cc)):
	  if i % 2 == 1:

	  	# Append each even positioned item to luhn_list while multiplying the string digit by 2
	    luhns_list.append(str(int(cc[i])*2))

	    # Iterate through the new list to find string int's that are "> 9"
	    for x in range(0,len(luhns_list)):
	      if int(luhns_list[x]) > 9:

	      	# Add the digits together
	        luhns_list[x] = str(int(luhns_list[x][0]) + int(luhns_list[x][1]))

	      # Replace old string digit with new digit at it's original position within the CC number.
	      cc[i] = luhns_list[x] 

	# Sum the total integers in the list of CC digits.
	modulo10 = sum(int(num) for num in cc)


	# if modulo10 has no remainder when dividing by 10, then according to Luhn's formula this CC number is valid 
	if modulo10 % 10 == 0:
	  	return True
	else:
		return False


def valid_creditcard(cc_number):

	# Remove hyphens from string
	cc_number = ''.join(c for c in cc_number.replace('-',''))


	# Validate length of CC number depending on length of input().
	if len(cc_number) not in range(14,17):
		return print("INVALID")

	# Visa
	elif int(cc_number[0]) == 4 and (len(cc_number) == 13 or len(cc_number) == 16):
		if luhn_algo(cc_number):
			return print("VISA")
		else:
			return print("INVALID")

	# AMEX
	elif len(cc_number) == 15 and (int(cc_number[:2]) == 34 or int(cc_number[:2]) == 37):
		if luhn_algo(cc_number):
			return print("AMEX")
		else:
			return print("INVALID")

	# MasterCard
	elif len(cc_number) == 16 and int(cc_number[:2]) in range(51,56):
		if luhn_algo(cc_number):
			return print("MASTERCARD")
		else:
			return print("INVALID")

	else:
		return print("INVALID")


# User input for CC number
print("Please Enter Your Credit Card Number")
valid_creditcard(input())
