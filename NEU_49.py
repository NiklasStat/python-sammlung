from tkinter import *
from PIL import ImageTk, Image
import sqlite3

from docutils.nodes import address

root = Tk()
root.title("Canvas")
root.geometry("400x600")


conn = sqlite3.connect("address_book.db")


c = conn.cursor()
# EINMAL einlesen reicht
'''
c.execute("""CREATE TABLE addresses (
           first_name text,
           last_name text,
           address text,
           city text,
           state text,
           zipcode integer
           )""")
'''

def edit():
    editor = Tk()
    editor.title("Update A Record")
    editor.geometry("400x300")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()

    if not record_id.isdigit():
        error_label = Label(editor, text="Ungültige ID! Bitte eine Zahl eingeben.", fg="red")
        error_label.grid(row=0, column=0)
        return

    # c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    c.execute("SELECT * from addresses WHERE oid = ?",  (record_id,))
    records = c.fetchall()
    print(records)

    if not records:
        error_label = Label(editor, text="Keine Daten für diese ID gefunden.", fg="red")
        error_label.grid(row=0, column=0)
        return

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_name_editor = Entry(editor, width=30)
    address_name_editor.grid(row=2, column=1, padx=20)

    city_name_editor = Entry(editor, width=30)
    city_name_editor.grid(row=3, column=1, padx=20)

    state_name_editor = Entry(editor, width=30)
    state_name_editor.grid(row=4, column=1, padx=20)

    zipcode_name_editor = Entry(editor, width=30)
    zipcode_name_editor.grid(row=5, column=1, padx=20)


    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)

    address_name_label_editor = Label(editor, text="Address")
    address_name_label_editor.grid(row=2, column=0)

    city_name_label_editor = Label(editor, text="City")
    city_name_label_editor.grid(row=3, column=0)

    state_name_label_editor = Label(editor, text="State")
    state_name_label_editor.grid(row=4, column=0)

    zipcode_name_label_editor = Label(editor, text="Zipcode")
    zipcode_name_label_editor.grid(row=5, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_name_editor.insert(0, record[2])
        city_name_editor.insert(0, record[3])
        state_name_editor.insert(0, record[4])
        zipcode_name_editor.insert(0, record[5])

    def save_record():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        c.execute("""UPDATE addresses SET
            first_name = ?,
            last_name = ?,
            address = ?,
            city = ?,
            state = ?,
            zipcode = ?
            WHERE oid = ?""", (
            f_name_editor.get(),
            l_name_editor.get(),
            address_name_editor.get(),
            city_name_editor.get(),
            state_name_editor.get(),
            zipcode_name_editor.get(),
            record_id
        ))
        conn.commit()
        conn.close()
        editor.destroy()  # Editor-Fenster schließen

    save_btn_editor = Button(editor, text="Save Record", command=save_record)
    save_btn_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=144)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid = ?",  (delete_box.get(),))
    conn.commit()
    conn.close()



def submit():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address_name, :city_name, :state_name, :zipcode_name) ",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address_name': address_name.get(),
                  'city_name': city_name.get(),
                  'state_name': state_name.get(),
                  'zipcode_name': zipcode_name.get(),
              })


    conn.commit()

    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address_name.delete(0, END)
    city_name.delete(0, END)
    state_name.delete(0, END)
    zipcode_name.delete(0, END)

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    print_records = ""
    for record in records:
        # Breitere Werte angepasst: erste Spalte 10 Zeichen, zweite Spalte 15 Zeichen, dritte Spalte 5 Zeichen
        print_records += f"{record[0]:<10} {record[1]:<15} {record[6]:>5}\n"

    query_label = Label(root, text=print_records, font=("Courier", 10), justify=LEFT, anchor="w")
    query_label.grid(row=11, column=0, columnspan=2, pady=50)

    conn.commit()
    conn.close()

f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)

address_name = Entry(root, width = 30)
address_name.grid(row = 2, column = 1, padx = 20)

city_name = Entry(root, width = 30)
city_name.grid(row = 3, column = 1, padx = 20)

state_name = Entry(root, width = 30)
state_name.grid(row = 4, column = 1, padx = 20)

zipcode_name = Entry(root, width = 30)
zipcode_name.grid(row = 5, column = 1, padx = 20)

delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1, pady = 5)



f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0, pady = (10, 0))

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address_name_label = Label(root, text = "Address")
address_name_label.grid(row = 2, column = 0)

city_name_label = Label(root, text = "City")
city_name_label.grid(row = 3, column = 0)

state_name_label = Label(root, text = "State")
state_name_label.grid(row = 4, column = 0)

zipcode_name_label = Label(root, text = "Zipcode")
zipcode_name_label.grid(row = 5, column = 0)

delete_box_label = Label(root, text = "Select ID")
delete_box_label.grid(row = 9, column = 0, pady = 5)



submit_btn = Button(root, text = "Add Record To Database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, ipadx = 110)

query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 138)

delete_btn = Button(root, text = "Delete Record", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

edit_btn = Button(root, text = "Edit Record", command = edit)
edit_btn.grid(row = 12, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 144)








conn.commit()

conn.close()

root.mainloop()