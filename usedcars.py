from car import Car


def main():
    limo = Car("limo", 180)
    limo.add_fuel(30)
    limo.drive(115)

    print("limo odometer", limo.odometer)
    print("limo fuel:", limo.fuel)
    print("{}, fuel={}, odometer={}".format(limo.name, limo.fuel, limo.odometer))


main()
