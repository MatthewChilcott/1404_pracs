COLOUR_CODES = {"ALICEBLUE": "#f0f8ff", "AQUAMARINE": "#7fffd4", "AZURE": "#f0ffff", "BLUEVOILET": "#8a2be2", "CYAN": "#00ffff"}

colour = input("Enter a colour for its code").upper()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Colour not defined. Try again")
    colour = input("Enter a colour for its code").upper()