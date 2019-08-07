# lottery_player_dict = {
#     'name':'Zwycięzca',
#     'numbers':(22, 33, 1, 4, 5, 7)
# }
#
# class LotteryPlayer:
#     def __init__(self, name, numbers):
#         self.name = name
#         self.numbers = numbers
#
#
# player_one = LotteryPlayer("Zwycięzca", (2, 5, 7, 2, 1, 1))
# player_two = LotteryPlayer("Miotacz ognia", (3, 5, 7, 7, 5, 3))
#
# print(player_one.name)
# print(player_one.numbers)
#
# print(player_two.name)
# print(player_two.numbers)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I am going to school.")


malutek = Student("Ten, co nie dostał się na KUL", "UMCS")
malutek.go_to_school()


