my_dict = {'name':'Odyseł', 'age':3, 'grades':[4, 4, 3, 2, 1, 5, 4, 5, 6]}
another_dict = {1: 15, 2: 75, 3: 150}

universities = [
    {
        'name':'UMCS',
        'location':'Lublin'
    },
    {
        'name':'KUL',
        'location':'Lublin'
    },
    {
        'name':'UJ',
        'location':'Kraków'
    },
    {
        'name':'UW',
        'location':'Warszawa'
    }
]

#
# i = 0
# for item in universities:
#     print(universities[i]['name'], universities[i]['location'])
#     i = i + 1

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    return total / count


student_list = [{'name':'pioter', 'grades':(5,)},
                {'name':'olo', 'grades':(3,)},
                {'name':'jan', 'grades':(6,)},
                {'name':'weronika', 'grades':(2,)},
                {'name':'ziomek', 'grades':(3,)},
                {'name':'poziomek', 'grades':(4,)}]


print(average_grade_all_students(student_list))
