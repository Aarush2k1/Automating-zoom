import pyautogui
import pandas as pd
import tkinter as tk
from tkinter import simpledialog
import time


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


application_window = tk.Tk()
name = simpledialog.askstring(
    "input", "Enter subject name", parent=application_window)
time.sleep(2)

# Reading the file
df = pd.read_csv('links.csv')
row = df.loc[df['sub'] == name]
id = str(row.iloc[0, 1])
pwd = str(row.iloc[0, 2])
print(id + " " + pwd)
join(id, pwd)
print("Done")
# checks time between 10mins  gap


# def is_time_bw(start_time, end_time, check_time=None):
#     check_time = datetime.now().strftime("%H:%M")
#     print(check_time)
#     if start_time < end_time:
#         return check_time >= start_time and check_time <= end_time


# x = is_time_bw(str("08:30"), str("09:00"))
