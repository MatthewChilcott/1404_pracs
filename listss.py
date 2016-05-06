# incomes_list = []
# months = int(input("How many months? "))
# for number in range(1, months + 1):
#  income = float(input("Enter income for month " + str(number) + ": "))
#  incomes_list.append(income)
# print("\nIncome Report\n-------------")
# total = 0
# for number in range(1, months + 1):
#  income = incomes_list[number - 1]
#  total += income
#  print("Month {:2d} - Income: ${:10.2f} Total: ${:10.2f}".format(number,
#                                                                  income, total))

# number_list = []
# for i in range (5):
#     input_number = int(input("number:"))
#     number_list.append(input_number)
# first_number = number_list[0]
# last_number = number_list[-1]
# smallest_number = min(number_list)
# largest_number = max(number_list)
# avg_number = sum(number_list) / len(number_list)
# print("The first number is {} \n The last number is {} \n The smallest number is {} \n The largest number is {} \n The average number is {}".format(first_number, last_number, smallest_number, largest_number, avg_number))

#
# usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
# access_denied = True
# while access_denied:
#     username = input("Please enter your username to continue:")
#     if username in usernames:
#         access_denied = False
#         print("Access Granted")
#     else:
#         print("Access Denied")

import random

quickpick_amount = 1 + int(input("How many quickpicks?"))

list_of_picks = []

for c in range(1, quickpick_amount):
    random_numbers_list = []
    for i in range(1, 7):
        random_number = random.randrange(0, 45)
        while random_number in random_numbers_list:
            random_number = random.randrange(1, 45)
        random_numbers_list.append(random_number)
    list_of_picks.append(random_numbers_list)
for number in list_of_picks:
    list_of_picks.sort()
    print(list_of_picks)