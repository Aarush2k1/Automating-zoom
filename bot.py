import datetime as dt
import time
from tkinter import Tk
from csv import *
import pyautogui
import pandas as pd


def join(id, pwd):
    time.sleep(2)
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('zoom')
    pyautogui.press('enter')
    time.sleep(2)

    # Clicking join button
    while True:
        join1 = pyautogui.locateOnScreen('./images/join_btn.png')
        if join1 != None:
            pyautogui.click(join1)
            time.sleep(1)
            break
        else:
            print("Could not find join btn")
            time.sleep(2)

    # Entering id
    while True:
        pyautogui.write(id)
        id_btn = pyautogui.locateOnScreen('./images/join.png')
        pyautogui.click(id_btn)
        time.sleep(5)
        break

    # Entering password
    pyautogui.typewrite(pwd)
    while True:
        join = pyautogui.locateOnScreen('./images/join_meeting_btn.png')
        pyautogui.click(join)
        break


# Reading File


def readfile(name):

    df = pd.read_csv('links.csv')
    # print((df['sub'] == name).any())
    if((df['sub'] == name).any()):
        row = df.loc[df['sub'] == name]
        id = str(row.iloc[0, 1])
        pwd = str(row.iloc[0, 2])
        print(id + " " + pwd)
        join(id, pwd)
        time.sleep(5)
    else:
        print("Invalid Input")
        errlabel.config(text="Invalid Subject name")

    print("Done")


# Main window of UI
win = Tk()
win.geometry("700x540")
win.title("Zoom Bot")
curr_day = dt.datetime.now().strftime("%A")
curr_time = time.strftime("%I:%M %p")

title = Label(win, text="Time Table ", pady=20)
title.pack()

Day = Label(win, text=curr_day, pady=20)
Day.pack()
curtime = Label(win, text=curr_time)
curtime.pack()

win.mainloop()

# Main window
# filepath = 'tt.csv'

# root = tk.Tk()
# root.geometry('900x700+10+10')
# root.title('Time Table')


# class TestApp(tk.Frame):
#     def __init__(self, parent, filepath):
#         super().__init__(parent)
#         self.table = Table(self, showtoolbar=True, showstatusbar=True)
#         self.table.importCSV(filepath)
#         self.table.show()


# app = TestApp(root, filepath)
# app.pack(fill=tk.BOTH, expand=1)

# root.mainloop()
