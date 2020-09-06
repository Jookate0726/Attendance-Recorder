# Importing modules
import sqlite3
from datetime import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

# Creating window
global main_Window
main_Window = Tk()
main_Window.title("Attendance Manager")
main_Window.geometry("1000x600")
main_Window.configure(bg="gold")

img = ImageTk.PhotoImage(Image.open("download.png"))


# Entered Function
def entered():

    date1 = date.today().strftime("%b-%d-%Y")

    hour = datetime.now().strftime("%H")
    minute = datetime.now().strftime("%M")
    hour1 = str(int(hour) + 1)
    entry = hour + ":" + minute
    exits = hour1 + ":" + minute

    database = sqlite3.connect("Attendance_File.db")

    cursor = database.cursor()

    """
    cursor.execute(''' CREATE TABLE Student_Attendence(
        Date text,
        Name text,
        Entry_time text,
        Exit_time text)''')

    """

    cursor.execute(" INSERT INTO Student_Attendence VALUES (?, ?, ?, ?)",
                   (date1, name.get(), entry, exits))

    database.commit()

    database.close()

    enter_window.withdraw()
    messagebox.showinfo("Attendance", "your Attendance is recorded.... You can stay hear for 1 hour..!!!")


# Enter function
def enter():
    global enter_window

    enter_window = Toplevel()
    enter_window.title("Attendance Manager")
    enter_window.geometry("800x500")
    enter_window.configure(bg="gold")

    global name

    Label(enter_window, image=img).pack(pady=(50, 20))
    Label(enter_window, text="Username", font=("comicsans", 20), bg="gold").pack(pady=(10, 30))
    name = Entry(enter_window)
    name.pack(ipadx=100, ipady=10)

    Button(enter_window, text="Enter Attendance", command=entered).pack(pady=30, ipadx=70)


# Show Details
def details():
    details_window = Toplevel()
    details_window.title("Attendance Manager")
    details_window.geometry("800x500")
    details_window.configure(bg="gold")

    # Using Treeview

    treeview = ttk.Treeview(details_window)
    treeview.pack(pady=50, ipadx=200, ipady=200)

    scrlbar = ttk.Scrollbar(details_window, orient="vertical", command=treeview.yview)
    scrlbar.pack(side='right', fill='x')
    treeview.configure(xscrollcommand=scrlbar.set)

    treeview["columns"] = ("1", "2", "3", "4")

    treeview['show'] = 'headings'

    treeview.column("1", width=90, anchor=W)
    treeview.column("2", width=90, anchor=W)
    treeview.column("3", width=90, anchor=CENTER)
    treeview.column("4", width=90, anchor=CENTER)

    treeview.heading("1", text="Date")
    treeview.heading("2", text="Name")
    treeview.heading("3", text="Entry Time")
    treeview.heading("4", text="Exit Time")

    database = sqlite3.connect("Attendance_File.db")

    cursor = database.cursor()

    """
    cursor.execute(''' CREATE TABLE Student_Attendence(
        Date text,
        Name text,
        Entry_time text,
        Exit_time text)''')

    """

    cursor.execute(" SELECT * FROM Student_Attendence")
    detail = cursor.fetchall()

    for i in detail:
        num = 0
        iid = "l" + str(num)
        num += 1

        treeview.insert("", 'end', text=iid, values=(i[0], i[1], i[2], i[3]))


    database.commit()

    database.close()


# Window
Label(main_Window, image=img).pack(pady=(50, 20))
Button(main_Window, text="Enter Details", bg="silver", font=("comicsans", 20), command=enter).pack(pady=20, ipadx=300)
Button(main_Window, text="Get Details", bg="silver", font=("comicsans", 20), command=details).pack(pady=20, ipadx=310)

main_Window.mainloop()
