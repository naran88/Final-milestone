import pyodbc

def select(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    results = []
    for row in cursor.fetchall():
        results.append(row)
    cursor.close()
    return results

def execute(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def show(rows):
    for row in rows:
        print(row)

try:
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-ED8GQ7K\MSSQLSERVER01;"
        "Database=Milestone2;"
        "Trusted_Connection=yes;"
    )
except pyodbc.Error as err:
    print("Cannot connect.")
    exit()

print("Select a record")
rows = select(conn, "select * from Accessories where Accessories_id = 'A2'")
show(rows)

print("Now insert a record")
execute(conn, "INSERT INTO Accessories (Accessories_id,name_of_accessories,qty,total_price) VALUES('A6','school_bag',1,100)")
rows = select(conn, "select * from Accessories")
show(rows)
