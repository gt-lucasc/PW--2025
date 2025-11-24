import sqlite3
with sqlite3.connect('meu_banco_de_dados.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        nome TEXT NOT NULL,
        idadade INTEGER
)
''')
    
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Alice', 20)")

    nome_usuario = 'Lucas'
    idade_usuario = 20

    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome_usuario, idade_usuario))