//FILE MANIPULATION


filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    
    words = text.lower().split()

    
    word_count = {}
    for word in words:
        
        word = word.strip(".,!?:;\"'()[]{}")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("\nWord counts (alphabetical order):")
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

except FileNotFoundError:
    print("File not found. Please check the file name.")
