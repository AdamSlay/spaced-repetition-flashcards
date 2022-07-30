import tkinter
from tkinter import StringVar, ttk

from datetime import date
yesterday = date(2022, 6, 5)
today = date.today()
diff = today - yesterday
print(diff.days)