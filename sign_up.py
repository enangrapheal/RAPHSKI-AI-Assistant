from tkinter import *
import tkinter.messagebox as message
import subprocess as sd
import sqlite3 as sql
import os


# --- DATABASE SETUP ---
# This function creates the database and table if they don't exist
def init_db():
    db_name = "users.db"
    if not os.path.exists(db_name):
        conn = sql.connect(db_name)
        cur = conn.cursor()
        # Create the table with email as the primary key to prevent duplicates
        cur.execute('''
            CREATE TABLE users (
                firstname TEXT,
                surname TEXT,
                password TEXT,
                email TEXT PRIMARY KEY,
                phone TEXT
            )
        ''')
        conn.commit()
        conn.close()
        print("Database created successfully.")
    else:
        print("Database already exists.")


# Initialize the database when the script runs
init_db()


# --- GUI FUNCTIONS ---

def show():
    sd.Popen(["python", "sign_in.py"])
    root.destroy()


def login():
    sd.Popen(["python", "sign_in.py"])
    root.destroy()


def reg():
    firstname = ent1.get()
    surname = ent2.get()
    password = entp.get()
    email = ent3.get()
    phone = ent4.get()

    # Check for empty fields
    if firstname == "" or surname == "" or password == "" or email == "" or phone == "":
        message.showinfo("Prompt", "Empty record not allowed, please fill the form!")
        return

    try:
        # Connect to the database
        conn = sql.connect("users.db")
        cur = conn.cursor()

        # Insert data
        cur.execute(''' insert into users(firstname,surname,password,email,phone)
                       values(?,?,?,?,?)''', (firstname, surname, password, email, phone))
        conn.commit()
        conn.close()

        message.showinfo("Prompt", "Record submitted successfully")
        show()  # Redirect to sign in

    except sql.IntegrityError:
        message.showerror("Error", "Email already exists")
    except Exception as e:
        message.showerror("Error", f"An error occurred: {e}")


# --- GUI SETUP ---

root = Tk()
root.geometry("400x500+500+0")
root.resizable(0, 0)
root.title("Signup Page")

lbl = Label(root, text="Sign up here:", fg="#000", bg="#ffaaff", pady=5,
            font=("sanserif", 10, "bold"))
lbl.pack(side="top", fill="both")

lbl1 = Label(root, text="First name:", fg="silver", font=("sanserif", 14))
lbl1.pack()
ent1 = Entry(root, width=50, relief="flat")
ent1.pack()

lbl2 = Label(root, text="Surname:", fg="silver", font=("sanserif", 14))
lbl2.pack()
ent2 = Entry(root, width=50, relief="flat")
ent2.pack()

lblp = Label(root, text="Password:", fg="silver", font=("sanserif", 14))
lblp.pack()
entp = Entry(root, width=50, relief="flat", show="*")
entp.pack()

lbl3 = Label(root, text="Email:", fg="silver", font=("sanserif", 14))
lbl3.pack()
ent3 = Entry(root, width=50, relief="flat")
ent3.pack()

lbl4 = Label(root, text="Phone Number:", fg="silver", font=("sanserif", 14))
lbl4.pack()
ent4 = Entry(root, width=50, relief="flat")
ent4.pack()

btn = Button(root, text="Submit", width=20, fg="#B6D0E2", bg="#301934", command=reg)
btn.pack(pady=20)

fr = Frame(root)
btn1 = Button(fr, text="Already have an account Sign in", bg="#ffaaff", fg="#000", relief="flat", command=login)
btn1.grid(row=0, column=0)
fr.pack()

root.mainloop()