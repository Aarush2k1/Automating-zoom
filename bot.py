import time
import tkinter as tk
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


# custom UI
win = tk.Tk()
win.geometry("700x540")
win.title("Zoom Bot")


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


def getInput():
    name = entry.get(1.0, "end-1c")
    if(name != ""):
        print(type(name))
        readfile(str(name))
    else:
        print("Not input")


# Display Label
label = tk.Label(win, text="Enter Subject Name:")
label.pack()
errlabel = tk.Label(win, text="")
errlabel.pack()


# Input box
entry = tk.Text(win, width=10, height=2)
entry.pack()

# Button
button = tk.Button(
    win, text="Join", command=getInput)
button.pack()

win.mainloop()


# checks time between 10mins  gap


# def is_time_bw(start_time, end_time, check_time=None):
#     check_time = datetime.now().strftime("%H:%M")
#     print(check_time)
#     if start_time < end_time:
#         return check_time >= start_time and check_time <= end_time


# x = is_time_bw(str("08:30"), str("09:00"))
