import sqlite3

database = sqlite3.connect("Attendance_File.db")

cursor = database.cursor()

cursor.execute(''' CREATE TABLE Student_Attendence(
    Date text,
    Name text,
    Entry_time text,
    Exit_time text)''')

database.commit()

database.close()