
# from playsound import playsound

# from gtts import gTTS


# def playaudio(audio):
#     playsound(audio)


# def convert_to_audio(text):
#     audio = gTTS(text)
#     audio.save("textaudio.mp3")
#     playaudio("textaudio.mp3")


# convert_to_audio("""Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.
#  """)


from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


root = Tk()
app = Window(root)
root.mainloop()
