# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurant.db")

# Crear tabla de PLATOS
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT NOT NULL);
    """
)
# Crear tabla de MESAS
conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)
# Crear tabla de PEDIDOS
conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    id_plato INTEGER NOT NULL,
    id_mesa INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_plato) REFERENCES PLATOS(id),
    FOREIGN KEY (id_mesa) REFERENCES MESAS(id));
    """
)
# ------------------------------------------------------------------
# en la tabla platos crea platos
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizza', 10.99, 'Italiano')    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Hamburguesa', 8.99, 'Italiano')    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Shushi', 12.99, 'Italiano')    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Ensalada', 6.99, 'Italiano')    """
)
# ------------------------------------------------------------------
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)    """
)
# ------------------------------------------------------------------
conn.execute(
    """
    INSERT INTO PEDIDOS (id_plato, id_mesa, cantidad, fecha) 
    VALUES (1,2,2,'2024-04-01')    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (id_plato, id_mesa, cantidad, fecha) 
    VALUES (2,3,1,'2024-04-01')    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (id_plato, id_mesa, cantidad, fecha) 
    VALUES (3,1,3,'2024-04-02')    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (id_plato, id_mesa, cantidad, fecha) 
    VALUES (4,4,1,'2024-04-02')    """
)
# ------------------------------------------------------------------
# Consultar datos
print("\nPLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# Consultar datos
print("\nMESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# Consultar datos
print("\nPEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)
# Cerrar conexión
conn.close()