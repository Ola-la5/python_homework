import sqlite3
#task1


#task3
def add_publisher(cursor, publisher_id, name):
    try:
        cursor.execute("INSERT INTO publishers (publisher_id, name) VALUES (?,?)", (publisher_id, name,))
    except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

def add_magazine(cursor, magazine_id, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (magazine_id, name, publisher_id) VALUES (?,?,?)", (magazine_id, name, publisher_id))
    except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

def add_subscriber(cursor, subscriber_id, name, address):
    try:
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"Subscriber with name '{name}' and address '{address}' is already in the database.")
            return

        cursor.execute("INSERT INTO subscribers (subscriber_id, name, address) VALUES (?,?,?)", (subscriber_id, name, address))
        print(f"Subscriber {name} added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"An error occurred: {e}")
       
    
def add_subscription(cursor, subscription_id, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO subscriptions (subscription_id, subscriber_id, magazine_id, expiration_date) VALUES (?,?,?,?)", (subscription_id, subscriber_id, magazine_id, expiration_date,))
    except sqlite3.IntegrityError:
        print(f"{expiration_date} is already in the database.")

try:

    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1") 
        print("Database created and connected successfully")

#task2
        cursor=conn.cursor()

        cursor.execute(
             """CREATE TABLE IF NOT EXISTS publishers(
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE)"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS magazines(
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id))"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS subscribers(
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL)"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS subscriptions(
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id))"""
        )


        print("Tables created successfully.")


        add_publisher(cursor, 1010, 'Good day')
        add_publisher(cursor, 1011, 'Starz')
        add_publisher(cursor, 1012, 'Blob')

        add_magazine(cursor, 11, 'B&B', 1010)
        add_magazine(cursor, 12, 'M&m', 1012)
        add_magazine(cursor, 53, 'Peanut', 1011)

        add_subscriber(cursor, 898, 'Andrew Bean', '123 Sunny Dr 2028')
        add_subscriber(cursor, 899, 'Holly Bean', '5656 Main St 5658')
        add_subscriber(cursor, 900, 'Joe Dassen', '123 Sunny Dr 2028')


        add_subscription(cursor, 3130, 899, 53, '09-10-2027')
        add_subscription(cursor, 3131, 898, 11, '12-12-2026')
        add_subscription(cursor, 3132, 900, 12, '01-01-2028')

        #task4
        cursor.execute("SELECT * FROM subscribers")
        result = cursor.fetchall()
        for row in result:
            print(row)

        cursor.execute("SELECT * FROM magazines ORDER BY name")
        result = cursor.fetchall()
        for row in result:
            print(row)    

        cursor.execute("""SELECT magazines.name, publishers.name 
                       FROM magazines 
                       JOIN publishers ON magazines.publisher_id = publishers.publisher_id 
                       WHERE publishers.name= 'Starz'""")
        result = cursor.fetchall()
        for row in result:
            print(row) 

        conn.commit()
        print("Sample data inserted successfully.")
except sqlite3.Error as e:
    print(f"Error: {e}")
        


