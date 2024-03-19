Problem 1: 
1.	Define grades function 
2.	Read grade
3.	Check if grade is digit and not bigger than 100
4.	#grading based on the entered grade
5.	if grade >= 90:
6.	print("The grade is A+")
7.	elif 85 <= grade < 90:
8.	print("The grade is A")
9.	elif grade >= 80:
10.	print("The grade is B+")
11.	elif 75 <= grade < 80:
12.	print("The grade is B")
13.	elif grade >= 70:
14.	print("The grade is C+")
15.	elif 65 <= grade < 70:
16.	print("The grade is C")
17.	elif grade >= 60:
18.	print("The grade is D+")
19.	elif 50 <= grade < 60:
20.	print("The grade is D")
21.	else:
22.	print("The grade is F")

Problem 2: 
1.	define Armstrong function 
2.	get a number from the user 
3.	read the integer variable number 
4.	storing the original value of number before operating to use it in the comparison 
5.	calculate the number of digits of the number 
6.	define the variable digits as integer and give it an initial value of zero 
7.	As the number does not equal to zero, divide the number by 10 and increase number of digits by one 
8.	Give the variable number_of_digits the value of variable digits 
9.	define the variable sum as integer and give it an initial value of zero 
10.	reset the number to its original value 
11.	as the original number does not equal zero, calculate original number % 10 and store the result in variable digit
12.	calculate digit ** number_of_digits and store the result in sum 
13.	check if the sum equals to the original number 
14.	print the number is an Armstrong number 
15.	else 
16.	print the number is not and Armstrong number 

Problem 3: 
1.	set the value of pi to 1
2.	get input_value form user
3.	if input_value.isdigit():
4.	display “you entred a valid value”
5.	else:
6.	display “please enter a valid value”
7.	while True:
8.	try:
9.	get an input from user
10.	if input_value <=0:
11.	display “please enter a positif integer”
12.	else:
13.	display input_value “ is a positif integer”
14.	except ValueError:
15.	display “Invalid input. Please enter a valid input”
16.	for x in range(0,input_value+1)
17.	if x%2==0:
18.	pi-=1/(x*2+3)
19.	else:
20.	pi+=1/(x*2+3)
21.	pi*=4
22.	display “the value of pi is:”,pi
23.	breakwhile

Problem 4: 
1.	define encryption
2.	read sentence
3.	initialize an empty list 
4.	check if the character is space or digit 
5.	append to the list as it is
6.	#Calculate the ASCII value by adding 1 to the current ASCII code
7.	ASCII = ord(char) + 1
8.	#Convert the ASCII value back to a character
9.	character = chr(ASCII)
10.	append the encrypted character to the list 
11.	#Join the characters in the list to form the encrypted message

Problem 5: 
1.	define the function check_lists_that_have_same_elements 
2.	define list1 as string list 
3.	ask the user to enter the elements of list 1 
4.	define list2 as string list 
5.	ask the user to enter the elements of list 2 
6.	create dictionary calculate_number_of_times1 to store elements of list 1
7.	create dictionary calculate_number_of_times2 to store elements of list 2
8.	for element in list1 
9.	calculate the number of times of this element
10.	for element in list2
11.	calculate the number of times of this element
12.	if number_of_times1 == number_of_times2 
13.	print the two lists have the same elements 
14.	else
15.	print the two lists does not have the same elements 
Problem 6: 
1.	set function called findfactors(n):
2.	let multiples= list()
3.	for x in range(1,n+1):
4.	if n%x==0:
5.	multiples.append(x)
6.	return multiples
7.	while True:
8.	try:
9.	get an input from user
10.	if input_value<=0:
a.	display “please enter a valid input”
11.	else:
a.	display input_value “is a positif integer”
12.	breakwhile 
13.	display “welcome to factor finder logiciel”
14.	get input_value from
15.	if number<=0:
16.	display “please reenter the same input value as previous”
17.	let number=int(input_value)
18.	if input_value.isdigit():
19.	display  f“{input_value} is a digit.”
20.	else:
21.	display  please enter a valid input 
22.	let multiple=findfactors(number)
23.	display “the factor of”,number,”are:”
24.	for factor in multiple:
25.	display factor
