def to_ascii(user_input):
    try:
        user_input = user_input
        x = ord(user_input)
        print(x)
    except ValueError:
        print("invalid input")


def from_ascii(user_input):
    try:
        user_input = int(user_input)
        x = chr(user_input)
        print(x)
    except ValueError:
        print("invalid input")

if __name__ == "__main__":
    from_or_to = input("Möchtest du von ASCII auf Zeichen konvertieren (A) oder andersherum (B)?").upper()

    if from_or_to == "B" or from_or_to == "A":
        user_input = input("Wie lautet dein Input?")

        if from_or_to == "A":
            from_ascii(user_input)

        elif from_or_to == "B":
            to_ascii(user_input)

    else:
        print("invalid input")
        exit()


