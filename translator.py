# importing translator from googletrans package
from googletrans import Translator


def translate(input_file, lang_code):
    try:
        # creating an instance of Translator class
        translator = Translator()
        # translating the input and returning the translated file
        translation = translator.translate(input_file, dest=lang_code)
        return translation.text
    except Exception as e:
        print('Something went wrong')
