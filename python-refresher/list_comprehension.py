my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]

print(my_list == an_equal_list)

print(sum([n for n in range(100) if n % 2 == 0]))

people_you_know = ["Andrzej", " Jędrzej", "Janusz ", "oleg", "ODYSEŁ", "   jaszczomp    "]
normalised_names = [person.strip().lower().capitalize() for person in people_you_know]
print(normalised_names)
