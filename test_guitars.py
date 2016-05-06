from guitars import Guitars

user_input = ''
guitar_tuple = ()
user_finished = False
while user_finished == False:
    guitar_name = input("Name: ")
    if guitar_name == '':
        user_finished = True
    guitar_year = input("Year Made: ")
    guitar_price = input("Price: ")
    guitar_list = (guitar_name, guitar_year, guitar_price)
    guitar_tuple += guitar_list

print(guitar_list)

gibson = Guitars("Gibson L-5 CES", 1922, 16035.40)
fender = Guitars("Fender Stratocaster", 2014, 765.40)
line = Guitars("Line 6 JTV-59", 2010, 1512.90)

