import translators as ts


def translate_text(text):

    result = ts.translate_text(query_text=text, to_language='en' if detect_language(text[0]) == 'ru' else 'ru')
    return result


def detect_language(text):
    return 'ru' if (text >= 'а' and text <= 'я') or (text >= 'А' and text <= 'Я') else 'en'

