import csv
import random
from googletrans import Translator


def get_random_word(language):
    # Open the dictionary file and filter by language
    with open('dictionary.csv') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[1] == language]
    # Choose a random word from the filtered rows
    word = random.choice(rows)[0]
    return word


def translate_word(word, language):
    # Check if the word is in the dictionary
    if language == 'french':
        translation = search_dictionary(word, 'french')
        if translation is None:
            # If not, use the Google Translate API to translate the word
            translation = translate_with_api(word, 'fr')
    elif language == 'spanish':
        translation = search_dictionary(word, 'spanish')
        if translation is None:
            # If not, use the Google Translate API to translate the word
            translation = translate_with_api(word, 'es')
    else:
        raise ValueError("Invalid language")
    # Return the translation
    return translation


def search_dictionary(word, language):
    # Open the dictionary file and search for the word
    with open('dictionary.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == word and row[1] == language:
                return row[2]
    # If the word is not found, return None
    return None


def translate_with_api(word, source_language):
    # Create a translator object
    translator = Translator()
    # Use the translator object to translate the text to the target language
    result = translator.translate(word, src=source_language, dest='en')
    # Return the translated text
    return result.text


def translate_to_french(text):
    # Use the Google Translate API to translate the text to French
    translator = Translator()
    result = translator.translate(text, dest='fr')
    # Return the translated text
    return result.text


def translate_to_spanish(text):
    # Use the Google Translate API to translate the text to Spanish
    translator = Translator()
    result = translator.translate(text, dest='es')
    # Return the translated text
    return result.text
