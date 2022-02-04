import tkinter as tk
from pandastable import Table, TableModel

filepath = 'tt.csv'

root = tk.Tk()
root.geometry('700x900+10+10')
root.title('Workshop Manager')


class TestApp(tk.Frame):
    def __init__(self, parent, filepath):
        super().__init__(parent)
        self.table = Table(self, showtoolbar=True, showstatusbar=True)
        self.table.importCSV(filepath)
        self.table.show()


app = TestApp(root, filepath)
app.pack(fill=tk.BOTH, expand=1)

root.mainloop()
