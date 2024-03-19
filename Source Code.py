#program description we solved 6 problems through these functions we classify grades , we check if the number is armstrong or not...etc
#date 26-2-2024

def grades():
    try:
        grade = int(input("Enter your grade :"))
        while grade > 100 or grade < 0:
            grade = int(input("Enter the correct grade:"))
    except:
        grade = int(input("Enter a valid value:"))
    if grade >= 90:
        print("The grade is A+")
    elif grade < 90 and grade >= 85:
        print("The grade is A")
    elif grade >= 80:
        print("The grade is B+")
    elif grade < 80 and grade >= 75:
        print("The grade is B")
    elif grade >= 70:
        print("The grade is C+")
    elif grade < 70 and grade >= 65:
        print("The grade is C")
    elif grade >= 60:
        print("The grade is D+")
    elif grade < 60 and grade >= 50:
        print("The grade is D")
    else:
        print("The grade is F")


def armstrong():
    # get a number from the user
    number = int(input("Please enter a number:  "))

    # Storing the original value before operating
    original_number = number
    digits = 0
    while number != 0:
        number = number // 10
        digits += 1

    # store the number of digits in a variable, define variable of sum and original number
    number_of_digits = digits
    sum = 0
    # reset the number to its original value
    number = original_number

    # take each individual digit of the number
    while original_number != 0:
        digit = original_number % 10
        original_number = original_number // 10
        sum += digit ** number_of_digits

    # check if the number is Armstrong number or not
    if sum == number:
        print("The number", number, "is an Armstrong number")
    else:
        print("The number", number, "is not an Armstrong number")


def calculate_pi():
    # all fractions in odd positions are negative
    # all fractions in even positions are positive

    n = 1
    pi = 0

    try:
        increment = int(input("Enter a positive number: "))
        while increment < 1:
            increment = int(input("Enter a positive number bigger than 1: "))
    except ValueError:
        print("Invalid value!")
        increment = int(input("Enter a positive number bigger than 1: "))
    if increment == 0 :
     print ("Approximation of pi = 0")

    for i in range(increment + 1):
        # i is used to determine the position and n is used to determine the denominator
        if i % 2 == 0:
            pi += 4 / n
            n += 2
        else:
            pi -= 4 / n
            n += 2

    print("Approximation of pi:", pi)


def encryption():
    sen = input("Enter the sentence you want to encrypt:")
    # open a new list to add characters after encryption
    encrypted_list = []

    # to make it continuous for all characters
    for char in sen:
        # to leave the space as it is and not turn it to !
        if char.isspace():
            encrypted_list.append(char)
        # the number should stay as it is
        elif char.isdigit():
            encrypted_list.append(char)
        if char == "z":
           encrypted_list.append("a")
        if char == "Z" :
            encrypted_list.append("A")
        else:
            # ASCII is a variable for adding 1 to the ASCII code
            ASCII = ord(char) + 1
            # character is a variable for getting the character of this ASCII code
            character = chr(ASCII)
            encrypted_list.append(character)

    # join function to turn the list to a string
    encrypted_message = ''.join(encrypted_list)
    print("Encrypted message:", encrypted_message)


# define a function that check if the elements of two lists are equal regardless the order
def check_lists_that_have_same_elements():
    # getting lists from the user
    list1 = str(input("Please enter the elements of the first list: "))
    list2 = str(input("Please enter the elements of the second list: "))
    # Create dictionaries to store number of times of each element in both first list and second list
    calculate_number_of_times1 = {}
    calculate_number_of_times2 = {}

    # calculate the number of times that each element occurs in first list
    for element in list1:
        calculate_number_of_times1[element] = calculate_number_of_times1.get(element, 0) + 1

    # calculate the number of times that each element occurs in second list
    for element in list2:
        calculate_number_of_times2[element] = calculate_number_of_times2.get(element, 0) + 1

    # Check if the elements of the two lists are the same
    if calculate_number_of_times1 == calculate_number_of_times2:
        print("The two lists", [list1], "and", [list2], "have the same elements")
    else:
        print("The two lists", [list1], "and", [list2], "does not have the same elements")


def find_factors():
    multiples = list()
    print("Welcome to factor finder logical.")
    input_value = input("Please enter a positive integer:")
    try:
        number = int(input_value)
        while number <= 0:
            number = input("Please enter a positive value:")
    except:
        number = input("enter a valid value :")
    for x in range(1, number + 1):
        if number % x == 0:
            multiples.append(x)
    print("The factors of", number, "are:")
    for factor in multiples:
        print(factor)

def menu():
    while True:
        print(
            " 1-classification grades \n 2-Armstrong number \n 3-calculating pi \n 4-encryption \n 5-checking lists "
            "equality \n 6-finding factors of a number \n 7-exit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            grades()
            continue
        elif choice == 2 :
            armstrong()
            continue
        elif choice == 3 :
            calculate_pi()
            continue
        elif choice == 4 :
            encryption()
            continue
        elif choice == 5 :
            check_lists_that_have_same_elements()
            continue
        elif choice == 6:
            find_factors()
            continue
        elif choice == 7 :
            break
        else:
            print("Enter a valid value !")
            continue


menu()
