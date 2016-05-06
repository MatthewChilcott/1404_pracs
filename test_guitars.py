from guitars import Guitars

user_input = ''
guitars = []
user_finished = False
while user_finished == False:
    guitar_name = input("Name: ")
    if guitar_name == '':
        user_finished = True
    guitar_year = input("Year Made: ")
    guitar_price = input("Price: ")
    new_guitar = Guitars(guitar_name, guitar_year, guitar_price)
    guitars.append(new_guitar)
gibson = Guitars("Gibson L-5 CES", 1922, 16035.40)
fender = Guitars("Fender Stratocaster", 2014, 765.40)
line = Guitars("Line 6 JTV-59", 2010, 1512.90)

guitars.append(gibson)
guitars.append(fender)
guitars.append(line)

for i in guitars:
    print("""Guitar {}:
    Name: {}
    Year: {}
    Cost: ${}
    {} ({}) : ${} added.""".format(i, guitars[i][1], guitars[1], guitars[1], guitars[1], guitars[1], guitars[1]))
    # {} ({}) : ${} added.""".format(i,guitar_name, guitar_year, guitar_price, guitar_name, guitar_year, guitar_price))