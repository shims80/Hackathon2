from tkinter import *
from gtts import gTTS
from playsound import playsound
import psycopg2
import os

counter = 0
def run_query(query, type):
    HOSTNAME = '127.0.0.1'
    USERNAME = 'postgres'
    PASSWORD = '********'
    DATABASE = 'text2audio'
    connection = psycopg2.connect(
        host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    if type == 'get':
        connection.commit()
        connection.close()
    else:
        connection.commit()
        results = cursor.fetchall()
        connection.close()
        return results
def get_texts():
    query = 'SELECT * FROM texts;'
    return run_query(query, 'post')
def insert_text():
    text_name = text_entry.get()
    text_file = text_entry2.get()
    query = f"INSERT INTO texts (text_name, text_file) VALUES ('{text_name}','{text_file}');"
    return run_query(query, 'get')
def convert_audio():
    text_file = button_entry.get()
    print(text_file)
    language = 'en'
    myobj = gTTS(text=text_file, lang=language, slow=False)
    myobj.save("audioFile.mp3")
    playsound("audioFile.mp3")
    os.remove("audioFile.mp3")

def previous_text():
    global counter
    global button_entry
    global all_btns
    if counter <= 0:
        return
    else:
        counter -= 1
        print(counter)
        print(len(all_btns))
        print('next')
        button_entry = Entry(window)
        button_entry.insert(END, f'{all_btns[counter][2]}')
        Button(window, text=f'{all_btns[counter][1]}', width=30, command=convert_audio).grid(
            row=8, column=2, sticky=W)
def next_text():
    global counter
    global button_entry
    global all_btns
    if counter > (len(all_btns) - 2):
        all_btns = get_texts()
        return
    else:
        counter += 1
        print(counter)
        print(len(all_btns))
        print('next')
        button_entry = Entry(window)
        button_entry.insert(END, f'{all_btns[counter][2]}')
        Button(window, text=f'{all_btns[counter][1]}', width=30, command=convert_audio).grid(
            row=8, column=2, sticky=W)
# def display_window():
window = Tk()
window.geometry('500x500')
window.title("Text To Audio!")
window.configure(background="green")
# text name label and button
Label(window, text="Text Name:",
      bg="green", fg="white", font="none 12 bold").grid(row=0, column=0, sticky=W)
text_entry = Entry(window, width=20, bg="white")
text_entry.grid(row=1, column=0, sticky=W)
# text file label and button
Label(window, text="Text File:",
      bg="green", fg="white", font="none 12 bold").grid(row=3, column=0, sticky=W)
text_entry2 = Entry(window, width=20, bg="white")
text_entry2.grid(row=4, column=0, sticky=W)
# submit Button
Button(window, text="SUBMIT", width=6, command=insert_text).grid(
    row=6, column=0, sticky=W)
# label for existing buttons
Label(window, text="Existing texts:",
      bg="green", fg="white", font="none 12 bold").grid(row=7, column=0, sticky=W)
# all buttons
all_btns = get_texts()
if all_btns != []:
    print(all_btns)
    button_entry = Entry(window)
    button_entry.insert(END, f'{all_btns[counter][2]}')
    Button(window, text=f'{all_btns[counter][1]}', width=30,
        command=convert_audio).grid(row=8, column=2, sticky=W)
    Button(window, text="<", width=1, command=previous_text).grid(
        row=8, column=0, sticky=W)
    Button(window, text=">", width=1, command=next_text).grid(
        row=8, column=3, sticky=W)
window.mainloop()