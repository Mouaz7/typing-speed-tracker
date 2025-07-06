"""Main module for the typing game, this module runs the game and handles user interactions"""
import test

def main():
    """Runs the main menu and handles user input for the typing game"""
    print("1) Train easy")
    print("2) Train medium")
    print("3) Train hard")
    print("4) See high score")
    print("0) Exit")

    choice = int(input())

    if choice in [1, 2, 3]:
        file = test.open_file(choice)
        if file is not None:
            test.game_logic(file)
    elif choice == 4:
        test.high_score()
    elif choice == 0:
        print("Exiting...")
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__== "__main__":
    main()
