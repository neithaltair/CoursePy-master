import _sqlite3

conexion = _sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE edad > 30")

personas_seleccionadas = cursor.fetchall()

for persona in personas_seleccionadas:
    print(persona)

conexion.close()