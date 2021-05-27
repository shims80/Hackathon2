from tkinter import *
from gtts import gTTS
from playsound import playsound


def convert_audio():
    address_info = address.get()
    language = 'en'
    myobj = gTTS(text=address_info, lang=language, slow=False)
    myobj.save("audioFile.mp3")
    playsound("audioFile.mp3")
    print(address_info)
    address_entry.delete(0, END)


app = Tk()
app.geometry("500x500")
app.title("Python Text to Audio App")
app.configure(background="black")
heading = Label(text="Python Text to Audio", bg="orange",
                fg="blue", font="10", width="500", height="3")
heading.pack()
address_field = Label(text="Text :")
address_field.place(x=15, y=70)
address = StringVar()
address_entry = Entry(textvariable=address, width="50", )
address_entry.place(x=15, y=100)
button = Button(app, text="Convert to Audio",
                command=convert_audio, width="30", height="2", bg="grey")
button.place(x=15, y=140)

mainloop()