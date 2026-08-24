print("Hello there!")
while True:
    answer = input("Do you want to see me count to 20? ")
    if answer == "yes":
        for number in range(1, 21):
            print(number)
        break
    elif answer == "no":
        print("Okay, maybe next time!")
        break
    else:
        print("Answer yes or no, please!")