"""
Create a Python program that reads a text file and counts the occurrences of each
word using a dictionary. The program should print the words and their counts.
"""

def count_words(file_path: str):
    all_words = {}

    with open(file_path, "r") as file:
        text = file.read()

    words = text.split()
    for word in words:
        if word in all_words:
            all_words[word] += 1
        else:
            all_words[word] = 1

    return all_words
print(count_words("example.txt"))





        
