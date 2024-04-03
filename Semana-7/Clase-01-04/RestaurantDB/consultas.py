import sqlite3
conn = sqlite3.connect("restaurant.db")


print("\PEDIDOS:")
conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero, PEDIDOS.fecha 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.id_plato = PLATOS.id 
    JOIN MESAS ON PEDIDOS.id_mesa = MESAS.id
    """
)