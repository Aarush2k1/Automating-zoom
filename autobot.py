import math
import pandas as pd
import numpy as np
from pandastable import Table, TableModel
import tkinter as tk
import tkinter.ttk as ttk
import datetime as dt
import time

df = pd.read_csv('tt.csv')
curr_day = dt.datetime.now().strftime("%A")
curr_time = time.strftime("%H:%M")
h2 = curr_time.split(":")[0]
m2 = curr_time.split(":")[0]


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


def difference(h1, m1, h2, m2):
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    diff = abs(t2-t1)
    return diff


def getNearest():
    temp_min = 600
    array = np.asarray(df['HOURS'])
    for ele in array:
        h1 = ele.split(":")[0]
        m1 = ele.split(":")[1]
        res = difference(int(h1), int(m1), int(h2), int(m2))
        if(temp_min >= res):
            temp_min = res
            idx = array.tolist().index(ele)
    return idx


link = df[curr_day.upper()].loc[getNearest()]
if(pd.isnull(link)):
    print("No class")
else:
    print(link.split(":")[1])
