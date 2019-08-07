grades_list = [77, 80, 90, 95, 100, 230, 14, 1, 22, 1, 1, 1, 2] # a list is mutable and ordered
grades_tuple = (77, 80, 90, 95, 100, 230, 14, 1, 22, 1, 1, 1, 2) # a tuple is immutable
set_grades = {77, 80, 100, 100, 92} # a set is collection of unique and unordered values

print(sum(grades_tuple) / len(grades_tuple))

grades_list.append(20)
print(grades_list)

new_tuple = grades_tuple + (888,)
print(new_tuple)

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 8, 11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print(your_lottery_numbers.difference(winning_numbers))
 
