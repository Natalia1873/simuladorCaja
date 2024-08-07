import sqlite3

con = sqlite3.connect("data/productos.sqlite")

cur = con.cursor()

cur.execute("select id, nombre, precio_unitario from productos")

columns_description = cur.description

result = cur.fetchall()

print(result)

con.close