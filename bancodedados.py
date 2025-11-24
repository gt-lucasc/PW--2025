import sqlite3
with sqlite3.connect('banco_de_dados') as connection:
    cursor = connection.cursor()

    create_table_query = '''
CREATE TABLE IF NOT EXISTS Pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
'''

cursor.execute(create_table_query)
connection.commit()

print("Tabela criada com sucesso!")