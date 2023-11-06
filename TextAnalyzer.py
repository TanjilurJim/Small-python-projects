#Asks user to enter a text
# whatever an article, paragraph, poem anything
#then the program will ask user to input 3 random letters
#from that moment the program will process that info and give 5 different analysis
#1. how many times those letters appear ?
#2. how many words are in the whole list ?
#3. what are the first and last letters of the list?
#4. the system will show how will the text look like if we inverted the words
#5. the system will tell us if the word python is in the list ?



letters_list = []

text = input("Please enter a text, poem, article or anything: ").lower()


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
