def replay():
    answer = ["Y", "N"]
    choice = input("Do you want to decode/encode again Y or N: ")
    while choice not in answer:
        choice = input("Sorry, please select  Y or N: ")
    if choice == "Y":
        return True
    else:
        return False
