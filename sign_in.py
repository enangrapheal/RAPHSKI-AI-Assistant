from tkinter import *
import subprocess as sd
import sys
import os
import sqlite3 as sql
import tkinter.messagebox as message

Signin = Tk()
Signin.geometry("300x300+300+0")
Signin.title("Sign in Area")
Signin.resizable(0, 0)


def loading():
    """Checks credentials against the database before logging in"""

    email = ent.get()
    password = ent1.get()

    # 2. Basic validation (Ensure fields aren't empty)
    if email == "" or password == "":
        message.showerror("Error", "Please enter both Email and Password.")
        return

    # 3. Connect to the database
    try:
        conn = sql.connect("users.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        account = cur.fetchone()
        if account:
            # --- LOGIN SUCCESSFUL ---
            print("Login Successful!")

            Signin.withdraw()

            sd.Popen([sys.executable, "raphski.py"])

            Signin.after(3000, Signin.destroy)
        else:
            message.showerror("Login Failed", "Invalid Email or Password.")

        conn.close()

    except Exception as e:
        message.showerror("Database Error", f"An error occurred: {e}")


def open_sign_up():
    """Opens the Sign Up page and closes the Sign In page"""
    try:
        # 1. Get the directory where this script is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        signup_path = os.path.join(current_dir, "sign_up.py")

        Signin.withdraw()

        # 3. Open the sign up script using the correct python executable
        sd.Popen([sys.executable, signup_path])

        Signin.after(1000, Signin.destroy)

    except Exception as e:
        print(f"Error opening sign up: {e}")
        # If it fails, show the window again so the user isn't stuck
        Signin.deiconify()


# --- GUI WIDGETS ---

ibl = Label(Signin, text="Sign in here:", font=("sanserif", 10, "bold"), bg="#ffaaff", fg="#000")
ibl.pack(fill="both")

ibl1 = Label(Signin, text="Email:", font=("sanserif", 14), fg="silver")
ibl1.pack()

ent = Entry(Signin, width=30, relief="flat")
ent.pack()

ibl2 = Label(Signin, text="Password:", font=("sanserif", 14), fg="silver")
ibl2.pack()

ent1 = Entry(Signin, width=30, relief="flat", show="*")
ent1.pack()

btn = Button(Signin, text="Login", bg="#301934", fg="#B6D0E2", width=15, command=loading)
btn.pack(pady=10)

btn_signup = Button(Signin, text="Sign Up", bg="#ffaaff", fg="#000", width=15, command=open_sign_up)
btn_signup.pack()

Signin.mainloop()