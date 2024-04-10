import sqlite3

def crear_tablas():
    conn = sqlite3.connect('personal.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS SALARIOS (
                        id INTEGER PRIMARY KEY,
                        empleado_id INTEGER NOT NULL,
                        salario REAL NOT NULL,
                        fecha_inicio DATE NOT NULL,
                        fecha_fin DATE NOT NULL,
                        fecha_creacion TEXT NOT NULL,
                        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLEADOS (
                        id INTEGER PRIMARY KEY,
                        nombres TEXT NOT NULL,
                        apellido_paterno TEXT NOT NULL,
                        apellido_materno TEXT NOT NULL,
                        fecha_contratacion DATE NOT NULL,
                        departamento_id INTEGER NOT NULL,
                        cargo_id INTEGER NOT NULL,
                        fecha_creacion TEXT NOT NULL,
                        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
                        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS DEPARTAMENTOS (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        fecha_creacion TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS CARGOS (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        nivel TEXT NOT NULL,
                        fecha_creacion TEXT NOT NULL
                    )''')

    conn.commit()
    conn.close()

def insertar_nuevos_departamentos_y_cargos():
    conn = sqlite3.connect('personal.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) VALUES (?, ?)", ("Ventas", "10-04-2020"))
    cursor.execute("INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) VALUES (?, ?)", ("Marketing", "11-04-2020"))

    cursor.execute("INSERT INTO CARGOS (nombre, nivel, fecha_creacion) VALUES (?, ?, ?)", ("Gerente de Ventas", "Senior", "10-04-2020"))
    cursor.execute("INSERT INTO CARGOS (nombre, nivel, fecha_creacion) VALUES (?, ?, ?)", ("Analista de Marketing", "Junior", "11-04-2020"))
    cursor.execute("INSERT INTO CARGOS (nombre, nivel, fecha_creacion) VALUES (?, ?, ?)", ("Representante de Ventas", "Junior", "12-04-2020"))

    conn.commit()
    conn.close()

def insertar_nuevos_empleados_y_salarios():
    conn = sqlite3.connect('personal.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                   ("Juan", "González", "Pérez", "15-05-2023", 1, 1, "10-04-2024"))  # Departamento "Ventas", Cargo "Gerente de Ventas"
    cursor.execute("INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                   ("María", "López", "Martínez", "20-06-2023", 2, 2, "10-04-2024"))  # Departamento "Marketing", Cargo "Analista de Marketing"

    cursor.execute("INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) VALUES (?, ?, ?, ?, ?)",
                   (1, 3000, "01-04-2024", "30-04-2025", "10-04-2024"))  # Salario de Juan González Pérez
    cursor.execute("INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) VALUES (?, ?, ?, ?, ?)",
                   (2, 3500, "01-07-2023", "30-04-2024", "10-04-2024"))  # Salario de María López Martínez

    conn.commit()
    conn.close()

def mostrar_contenido_tablas():
    conn = sqlite3.connect('personal.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM DEPARTAMENTOS")
    print("Contenido de la tabla DEPARTAMENTOS:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM CARGOS")
    print("\nContenido de la tabla CARGOS:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM EMPLEADOS")
    print("\nContenido de la tabla EMPLEADOS:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM SALARIOS")
    print("\nContenido de la tabla SALARIOS:")
    for row in cursor.fetchall():
        print(row)

    conn.close()

def listar_empleados_y_salarios():
    conn = sqlite3.connect('personal.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, SALARIOS.salario
                      FROM EMPLEADOS
                      INNER JOIN SALARIOS ON EMPLEADOS.id = SALARIOS.empleado_id''')
    print("\nEmpleados y sus salarios:")
    for row in cursor.fetchall():
        print(row)

    conn.close()

def listar_empleados_departamento_cargo():
    conn = sqlite3.connect('personal.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre AS departamento, CARGOS.nombre AS cargo
                      FROM EMPLEADOS
                      INNER JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
                      INNER JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id''')
    print("\nEmpleados, departamento y cargo:")
    for row in cursor.fetchall():
        print(row)

    conn.close()

def listar_empleados_departamento_cargo_salario():
    conn = sqlite3.connect('personal.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre AS departamento, CARGOS.nombre AS cargo, SALARIOS.salario
                      FROM EMPLEADOS
                      INNER JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
                      INNER JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
                      INNER JOIN SALARIOS ON EMPLEADOS.id = SALARIOS.empleado_id''')
    print("\nEmpleados, departamento, cargo y salario:")

    for row in cursor.fetchall():
        print(row)

    conn.close()
def actualizar_datos_empleado():
    conn = sqlite3.connect('personal.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE EMPLEADOS SET cargo_id = ? WHERE nombres = ? AND apellido_paterno = ? AND apellido_materno = ?", 
                   (3, "María", "López", "Martínez"))  

    cursor.execute("UPDATE SALARIOS SET salario = ? WHERE empleado_id = ?", (3600, 2))  

    conn.commit()
    conn.close()


if __name__ == "__main__":
    crear_tablas()
    insertar_nuevos_departamentos_y_cargos()
    insertar_nuevos_empleados_y_salarios()
    mostrar_contenido_tablas()
    listar_empleados_y_salarios()
    listar_empleados_departamento_cargo()
    listar_empleados_departamento_cargo_salario()
    actualizar_datos_empleado()
