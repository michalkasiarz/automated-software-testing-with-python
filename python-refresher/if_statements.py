# should_continue = True
# if should_continue:
#     print("Hello")
#
# known_people = ["John", "Pioter", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print(f"Super, kurwa! Znasz {person}")
# else:
#     print("You don't know shit")



def who_do_you_know():

    people = input("Enter the names of people you know, separated by commas: ")
    people_list = people.split(", ")
    return people_list


def ask_user():

    user_name = input('Give a goddamn\' name: ')
    if user_name in who_do_you_know():
        print(f'You know {user_name}.')
    else:
        print(f'You don\'t know {user_name}.')

ask_user()
