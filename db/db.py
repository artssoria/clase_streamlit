import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('prueba.db')
cursor = conn.cursor()

# Creación de la tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL,
        direccion TEXT NOT NULL,
        sexo TEXT NOT NULL
    )
''')
# Confirmación de los cambios
conn.commit()

# Agregar datos a la tabla
cursor.execute("INSERT INTO contactos (nombre, telefono, direccion, sexo) VALUES (?, ?, ?, ?)", ("Juan", "123456789", "Calle 123", "Masculino"))
cursor.execute("INSERT INTO contactos (nombre, telefono, direccion, sexo) VALUES (?, ?, ?, ?)", ("María", "987654321", "Calle 456", "Femenino"))


# Confirmación de la creación de la tabla
conn.commit()

# Leer los datos de la tabla
cursor.execute("SELECT * FROM contactos")
contactos = cursor.fetchall()

# Imprimir los datos
for contacto in contactos:
    print(contacto)


# Cierre de la conexión a la base de datos
conn.close()