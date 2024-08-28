import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create the student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        class TEXT NOT NULL,
        grade TEXT NOT NULL,
        marks INTEGER NOT NULL
    )
''')

# Insert 20 records into the student table
students = [
    (1, 'Alice', 'Mathematics', '10', 'A', 95),
    (2, 'Bob', 'Mathematics', '10', 'B', 85),
    (3, 'Charlie', 'Mathematics', '10', 'C', 75),
    (4, 'David', 'Science', '10', 'A', 92),
    (5, 'Eva', 'Science', '10', 'B', 88),
    (6, 'Frank', 'Science', '10', 'C', 78),
    (7, 'Grace', 'English', '10', 'A', 93),
    (8, 'Hannah', 'English', '10', 'B', 82),
    (9, 'Ian', 'English', '10', 'C', 73),
    (10, 'Jack', 'History', '10', 'A', 90),
    (11, 'Kara', 'History', '10', 'B', 86),
    (12, 'Leo', 'History', '10', 'C', 76),
    (13, 'Mia', 'Geography', '10', 'A', 91),
    (14, 'Nina', 'Geography', '10', 'B', 87),
    (15, 'Oscar', 'Geography', '10', 'C', 77),
    (16, 'Paul', 'Mathematics', '11', 'A', 94),
    (17, 'Quinn', 'Science', '11', 'B', 89),
    (18, 'Rose', 'English', '11', 'A', 92),
    (19, 'Sam', 'History', '11', 'B', 84),
    (20, 'Tina', 'Geography', '11', 'A', 95)
]

cursor.executemany('''
    INSERT INTO student (id, name, subject, class, grade, marks)
    VALUES (?, ?, ?, ?, ?, ?)
''', students)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table created and records inserted successfully.")
