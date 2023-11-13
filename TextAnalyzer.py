#Asks user to enter a text
# whatever an article, paragraph, poem anything
#then the program will ask user to input 3 random letters
#from that moment the program will process that info and give 5 different analysis
#1. how many times those letters appear ?
#2. how many words are in the whole list ?
#3. what are the first and last letters of th e list?
#4. the system will show how will the text look like if we inverted the words
#5. the system will tell us if the word python is in the list ?



letters_list = []

text = input("Please enter a text, poem, article, or anything: ").lower()

for i in range(3):
    letter = input(f"Please enter letter {i+1} of 3 you want: ").lower()

    if len(letter) == 1 and letter.isalpha():
        letters_list.append(letter)
    else:
        print("Please enter only one alphabetical letter.")
        break

if len(letters_list) == 3:
    print("\nLETTER REPETITIONS")

    for letter in letters_list:
        letter_repetition = text.count(letter)
        print(f"The letter '{letter}' is repeated {letter_repetition} times in the text.")
else:
    print("Analysis cannot be performed without 3 valid letters.")

print("\nNUMBER OF WORDS")
words = text.split()
print(f"There are {len(words)} words in your text.")

print("\nFIRST AND LAST LETTERS:")

# Find the last alphabetical character by iterating backward
last_alphabetical_char = None
for char in reversed(text):
    if char.isalpha():
        last_alphabetical_char = char
        break

if last_alphabetical_char:
    print(f"The first letter is '{text[0]}' and the last letter is '{last_alphabetical_char}'")
else:
    print("There are no alphabetical characters in the text.")

print("\nINVERTED TEXT")
words.reverse()
inverted_text = ' '.join(words)
print(f"The text backward would look like this: '{inverted_text}'")

print("\nCHECK FOR 'PYTHON' IN THE TEXT")
if 'python' in text:
    print("The word 'python' is present in the text.")
else:
    print("The word 'python' is not present in the text.")

