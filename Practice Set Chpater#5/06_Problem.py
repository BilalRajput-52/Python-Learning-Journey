# Create a dictionary of Hindi words with English meanings and 
# allow the user to look up a word.

words = {
    "madad": "help",
    "kursi": "chair",
    "kitab": "book"
}

word = input("Enter a word: ")

print(words.get(word))