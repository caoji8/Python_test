def choose_model(len):
    userInput = input('>')
    try:
        userInput = int(userInput)
    except:
        print("Error print")
    if len == 2:
        if userInput == 1:
            return 1
        elif userInput == 2:
            return 2
        else:
            print("Error Choose")
            return "Error Choose"
    elif len == 3:
        if userInput == 1:
            return 1
        elif userInput == 2:
            return 2
        elif userInput == 3:
            return 3
        else:
            print("Error Choose")
            return "Error Choose"
