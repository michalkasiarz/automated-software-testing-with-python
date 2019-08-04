my_string = "hello"

for character in my_string:
    print(character)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in my_list:
    print(number ** 2)


user_wants_number = True
while user_wants_number == True:
    print("User wants a number!")

    user_input = input("Should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_number = False
