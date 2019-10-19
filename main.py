import re
import tkinter
import tkinter.scrolledtext as scrolledtext

text_to_translate = " "


def translate_to_uwu(text):
    text = re.sub(r"l", "w", text)
    text = re.sub(r"tt", "dd", text)
    text = re.sub(r"(ddw)", "ddl", text)
    text = re.sub(r"r", "w", text)
    text = re.sub(r"(th)\b", "f", text)
    return text


def get_text():
    global text_to_translate
    text_to_translate = translate_to_uwu(body.get(1.0, "end-1c"))
    body.delete('1.0', "end-1c")
    body.insert("end-1c", text_to_translate)


window = tkinter.Tk()

body = scrolledtext.ScrolledText(window, wrap=tkinter.WORD)
body['font'] = ('consolas', '12')
body.pack()

button = tkinter.Button(window, text="Translate Text", command=get_text)
button.pack()

window.title('UWU Translator')

window.mainloop()
