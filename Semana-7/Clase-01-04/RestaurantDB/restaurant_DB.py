# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurant.db")

# Crear tabla de PLATOS
try:
        conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL);
        """
        )
except sqlite3.OperationalError:
    print("La tabla PLATOS ya existe")

# Crear tabla de MESAS
try:
    conn.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla PLATOS ya existe")
# Crear tabla de PEDIDOS
try:
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
except sqlite3.OperationalError:
    print("La tabla PLATOS ya existe")
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
# en la tabla mesas crea las siguientes mesas
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
# en la tabla pedidos crea los siguientes pedidos
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

# Actualizar una fila de la tabla de platos
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)

# Actualizar una fila de la tabla de platos
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 3
    """
)

# Eliminar una fila de la tabla de platos
conn.execute(
    """
    DELETE FROM PLATOS
    WHERE id = 3
    """
)

# Eliminar una fila de la tabla de pedidos
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)

print("\PEDIDOS:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero, PEDIDOS.fecha 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.id_plato = PLATOS.id 
    JOIN MESAS ON PEDIDOS.id_mesa = MESAS.id
    """
)
for row in cursor:
    print(row)

cursor = conn.execute(
    """
    SELECT PLATOS.nombre
    FROM PEDIDOS
    LEFT JOIN PLATOS ON PEDIDOS.id_plato= PLATOS.id
    """
)
for row in cursor:
    print(row)


conn.commit()
conn.close()