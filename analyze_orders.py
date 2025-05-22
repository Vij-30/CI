import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path("orders.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# --- Create the 'orders' table if it doesn't exist ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    status TEXT,
    quantity INTEGER,
    unit_price REAL
)
""")

# --- Insert sample data (run this only once or check if table is empty) ---
cursor.execute("SELECT COUNT(*) FROM orders")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO orders (status, quantity, unit_price)
    VALUES (?, ?, ?)
    """, [
        ('Cancelled', 5, 47.52),
        ('shipped', 9, 59.74),
        ('Shipped', 6, 23.62),
        ('SHIPPED', 3, 67.73),
        ('Processing', 9, 96.59),
    ])
    conn.commit()

# --- Run your SQL query ---
query = """
SELECT AVG(quantity * unit_price) AS avg_order_value
FROM orders
WHERE LOWER(status) = 'shipped';
"""

df = pd.read_sql_query(query, conn)
conn.close()

# Show result
print(df)

