import sqlite3

def create_tables():
    conn = sqlite3.connect('yizkor.db')  # Create a connection to the database (or connect if it exists)
    cursor = conn.cursor()

    # Create the User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            role TEXT CHECK (role IN ('admin', 'member')) DEFAULT 'member' 
        )
    ''')

    # Create the Person table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Person (
            person_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            hebrew_first_name TEXT,
            hebrew_last_name TEXT,
            date_of_birth DATE,
            date_of_death DATE,
            date_of_birth_hebrew TEXT, 
            date_of_death_hebrew TEXT,
            content TEXT,
            image_path TEXT 
        )
    ''')

    # Create the Member table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Member (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            person_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES User(user_id),
            FOREIGN KEY (person_id) REFERENCES Person(person_id)
        )
    ''')

    conn.commit()  # Save the changes
    conn.close()  # Close the connection

if __name__ == '__main__':
    create_tables()