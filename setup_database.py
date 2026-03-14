import sqlite3

# 1. CONNECT (This creates the file if it doesn't exist)
# 'transport_system.db' is the name of the file that will be created.
try:
    conn = sqlite3.connect(
        'raphski_user_data.db')

    # 2. CREATE CURSOR
    # The cursor allows us to give commands to the database
    cursor = conn.cursor()

    # 3. CREATE TABLE
    # This defines the structure of your data (Columns)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            surname TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT NOT NULL
        )
    ''')

    # 4. COMMIT (Save changes)
    conn.commit()
    print("Database created and table structured successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # 5. CLOSE
    if conn:
        conn.close()