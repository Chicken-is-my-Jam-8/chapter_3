
#Alexander J. Jackson
#four_digits.py

digit_list = []
digit_sum = 0
four_digits = str(input("Enter a four digit integer: "))

# puts items into digit_list
for x in four_digits:
	digit_list.append(int(x))
# adds up all the digits into digit_sum
for y in digit_list:
	digit_sum += int(y)

if len(digit_list) == 4:
	print(f"The individual digits of your input are: {digit_list}")
	print(f"The sum of your input is: {digit_sum}")
else:
	print("Your input was not four digits. Quiting.")
	
