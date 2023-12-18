from googletrans import Translator


def translate_text(text):
    translator = Translator()
    result = translator.translate(text, dest='en' if detect_language(text[0]) == 'ru' else 'ru')
    return result.text


def detect_language(text):
    return 'ru' if (text >= 'а' and text <= 'я') or (text >= 'А' and text <= 'Я') else 'en'
