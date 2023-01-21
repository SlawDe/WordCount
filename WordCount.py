text = input("Napisz słowo: ")

words = text.split(" ")
sin_words = set(words)

for word in sin_words:
    print(f"'{word}' occurs {words.count(word)} times.")