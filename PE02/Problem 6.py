#1. Count words in a file**
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print("Word count:", len(words))
    except FileNotFoundError:
        print("File not found!")

# Example use
# count_words("sample.txt")

#2. Guest Book**
while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    print(f"Hi {name}, thanks for visiting!")
    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")
