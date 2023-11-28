import sqlite3

db = sqlite3.connect('student.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        score INTEGER DEFAULT 0
    ) ''')
cursor.executemany('''INSERT INTO student ('name', 'surname', 'date_of_birth', 'score') VALUES (?, ?, ?, ?)''', [
    ('Murat', 'Mukhutdinov', '2008-01-05', 6),
    ('Nurbek', 'Djanaev', '2006-04-11', 8),
    ('Aidar', 'Kubatbekov', '2007-09-18', 12),
    ('Nurai', 'Kubanichbekova', '2007-05-02', 19),
    ('Baizak', 'Myrzaliev', '2007-03-17', 16),
    ('Anvar', 'Matyakubov', '2008-12-04', 4),
    ('Ruslan', 'Krasnojonov', '2007-07-12', 10),
    ('Danil', 'Li', '2007-02-28', 9),
    ('Daniel', 'Toguzbayev', '2007-07-02', 11),
    ('Artem', 'Shakhvorostov', '2006-10-21', 1)
    ])
cursor.execute('''UPDATE student SET name='genius' WHERE score>10''')
for result in cursor:
    print(result)
cursor.execute('''DELETE FROM student WHERE rowid % 2 = 0''')
db.commit()
db.close()