import sqlite3
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
);
'''

cursor.execute(create_table_query)

connection.commit()

print("Tabela 'Students' criada com sucesso!")


import sqlite3
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    insert_query = '''
    INSERT INTO Students (name, age, email)
    VALUES (?, ?, ?);
    '''

    student_data = ('Lucas', 20, 'lc@exemplo.com')

    cursor.execute(insert_query, student_data)

    connection.commit()

    print("Dados inseridos com sucesso!")
