"""Module for functions in the writing project, including file management with assessment"""
import os

def open_file(choice):
    '''Opens a file and reads it from options between 1-4, returns none if there is no file'''
    if choice == 1:
        filename = "easy.txt"
    elif choice == 2:
        filename = "medium.txt"
    elif choice == 3:
        filename = "hard.txt"
    elif choice == 4:
        filename = "score.txt"
    else:
        return None
    
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None

def word_accuracy(input_txt, text):
    '''Calculates the word accuracy of text written'''
    input_words = input_txt.split()
    text_words = text.split()

    min_length = min(len(input_words), len(text_words))
    correct_words = 0
    for i in range(min_length):
        if input_words[i] == text_words[i]:
            correct_words += 1
    accuracy = correct_words / len(text_words)
    return accuracy

def letter_accuracy(input_txt, text):
    '''Calculates the letter accuracy of text written'''
    input_len = len(input_txt)
    text_len = len(text)
    min_length = min(input_len, text_len)
    correct_count = 0
    letter_failed = {}

    for i in range(min_length):
        if input_txt[i] == text[i]:
            correct_count += 1
        else:
            misspelled_letter = input_txt[i]
            letter_failed[misspelled_letter] = letter_failed.get(misspelled_letter, 0) + 1

    accuracy = correct_count / max(input_len, text_len)
    return accuracy, letter_failed

def clear_screen():
    '''Clears the terminal screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

def high_score():
    '''Reads score file and prints out the score'''
    try:
        with open("score.txt", "r") as file:
            content = file.read()
            if content:
                print("High Score:")
                print(content)
            else:
                print("No high score available.")
    except FileNotFoundError:
        print("No high score available.")

def write_score(score):
    '''Asks for username and writes the name with the score in a file'''
    username = input("Enter your username: ")

    with open("score.txt", "a") as file:
        file.write(username + ":" + str(score) + "%" + "\n")

def game_logic(text):
    '''The main game logic of the game'''
    sentences = text.splitlines()
    collected_input = []

    for sentence in sentences:
        clear_screen()
        print(sentence.strip())
        user_input = input("")
        collected_input.append(user_input)

    user_input_combined = " ".join(collected_input)
    word_acc = word_accuracy(user_input_combined, text)
    letter_acc, letter_failed = letter_accuracy(user_input_combined, text)
    rounded_word_acc = round(word_acc * 100, 2)
    rounded_letter_acc = round(letter_acc * 100, 2)
    print(f"Ordprecision: {rounded_word_acc}%")
    print(f"Teckenprecision: {rounded_letter_acc}%")
    if letter_failed:
        print("Felstavade tecken:")
        for letter, count in letter_failed.items():
            if letter != ' ':
                print(f"{letter}: {count}")
    rounded_score = round(word_acc * 100, 2)
    write_score(rounded_score)
