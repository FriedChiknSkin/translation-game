from translator import get_random_word, translate_word, translate_to_french, translate_to_spanish


def game():
    print("Welcome to the Translation Game!")
    while True:
        # Ask the player which mode they want to use
        mode = input(
            "\n" + "Which mode would you like to use? (game/translator/quit): ")
        # Check which mode the player chose
        if mode == 'game':
            # Ask the player which language they want to translate
            language = input(
                "Which language would you like to translate? (french/spanish): ")
            while language not in ['french', 'spanish']:
                language = input(
                    "Please enter a valid language (french/spanish): ")

            # Set the initial score to 0
            score = 0
            while True:
                # Get a random word to translate
                word = get_random_word(language)
                # Ask the player to translate the word
                print(f"What is the English translation of '{word}'?")
                answer = input("> ")
                # Check if the player wants to quit
                if answer.lower() == 'quit':
                    print(f"Thanks for playing! Your total score is {score}")
                    return
                # Get the correct translation of the word
                translation = translate_word(word, language)
                # Check if the player's answer is correct
                if answer.lower() == translation.lower():
                    print("Correct!")
                    score += 1
                else:
                    print(f"Sorry, the correct answer was '{translation}'")
                # Show the current score
                print(f"Score: {score}")
        elif mode == 'translator':
            # Ask the player which language they want to translate to
            target_language = input(
                "Which language would you like to translate to? (french/spanish): ")
            while target_language not in ['french', 'spanish']:
                target_language = input(
                    "Please enter a valid language (french/spanish): ")

            # Ask the player for the text to translate
            text = input("\n" + "Enter the text you would like to translate: ")
            # Translate the text to the target language
            if target_language == 'french':
                result = translate_to_french(text)
            else:
                result = translate_to_spanish(text)

            # Show the translation to the player
            print(f"The translation is: {result}")
        elif mode == 'quit':
            # End the game
            print("Thanks for playing!")
            return
        else:
            # Handle invalid input
            print("Invalid mode")


if __name__ == '__main__':
    game()
