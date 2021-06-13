from tkinter import *
from tkinter import ttk
from translator import translate

root = Tk()
root.title('Translator')
root.geometry("600x600")

# Creating a Text Box to input text that needs to be translated
original = Text(root, height=10, width=42, borderwidth=5)
original.config(font=("Courier", 12))

# Creating label
original_label = Label(root, text="Enter the Text to be translated:")
original_label.config(font=("Courier", 14))

original_label.grid(row=0, column=0, columnspan=2)
original.grid(row=1, column=0, padx=80, columnspan=2)

# Label
ttk.Label(root, text="Select the Language :",
          font=("Courier", 14)).grid(column=0,
                                     row=2, padx=10, pady=25)

# Set of languages that can be translated
languages = {'default': '-----', 'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'chinese (simplified)': 'zh-Hans', 'chinese (traditional)': 'zh-Hant', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'finnish': 'fi', 'french': 'fr', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hebrew': 'he', 'hindi': 'hi', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id, in', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jv', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kyrgyz': 'ky', 'korean': 'ko', 'lao': 'lo', 'latin': 'la', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'nepali': 'ne', 'norwegian': 'no', 'polish': 'pl', 'portuguese': 'pt', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'uyghur': 'ug', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi, ji', 'yoruba': 'yo', 'zulu': 'zu'}


options = StringVar()
options.set(languages['default'])
language = OptionMenu(root, options, *languages.keys())
language.grid(column=1, row=2, sticky='W', ipadx=15)


def get_selected():
    # function that translates the user input
    input_text = original.get("1.0", 'end-1c')
    lang = options.get()
    lang_code = languages[lang]

    output = translate(input_text, lang_code)
    translated.insert(END, output + "\n")


# creating Translate Button
btn = Button(root, text='Translate', borderwidth=5, command=get_selected)
btn.grid(column=0, row=3, ipadx=50)
btn.config(font=("Courier", 12))


def button_clear():
    # function to clear the output text box
    translated.delete('1.0', END)


button_clear = Button(root, text="Clear", borderwidth=5, command=button_clear)
button_clear.grid(column=1, row=3, ipadx=50, ipady=3)
btn.config(font=("Courier", 12))

# Creating a Text Box to input text that needs to be translated
translated = Text(root, height=10, width=42, borderwidth=4)
translated.config(font=("Courier", 12))

# Creating label
translated_label = Label(root, text="Translation:")
translated_label.config(font=("Courier", 14))

translated_label.grid(row=4, column=0, columnspan=2, ipady=20)
translated.grid(row=5, column=0, padx=80, columnspan=2)

root.mainloop()
