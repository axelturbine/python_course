translation = {
    "Hej": "Hello",
    "Hejdå": "Goodbye",
    "Tack": "Thanks",
    "Bror": "Brother",
    "Syster": "Sister",
}

word = input("Enter a Swedish word: ")
if word in translation:
    print("The English translation is:", translation[word])
else:
    print("Sorry, that word is not in the dictionary.")