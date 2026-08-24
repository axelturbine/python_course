quote = input("Write your favorite quote: ")
with open("quotes.txt", "a") as file:
    file.write("Quote:" + quote + "\n")

with open("quotes.txt", "r") as file:
    content = file.read()
    print(content)