import sqlite3

DB_PATH = "demo.db"

def main():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS orders;")
    cur.execute("DROP TABLE IF EXISTS customers;")

    cur.execute("""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        product TEXT NOT NULL,
        amount REAL NOT NULL,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );
    """)

    cur.executemany(
        "INSERT INTO customers (id, name, email) VALUES (?, ?, ?);",
        [
            (1, "Alice Johnson", "alice@example.com"),
            (2, "Bob Smith", "bob@example.com"),
            (3, "Charlie Lee", "charlie@example.com"),
        ],
    )
    cur.executemany(
        "INSERT INTO orders (id, customer_id, product, amount, order_date) VALUES (?, ?, ?, ?, ?);",
        [
            (1, 1, "Laptop", 1200.00, "2025-09-01"),
            (2, 1, "Mouse", 25.50, "2025-09-02"),
            (3, 2, "Keyboard", 75.00, "2025-09-03"),
            (4, 3, "Monitor", 300.00, "2025-09-05"),
            (5, 2, "Headset", 55.00, "2025-09-06"),
        ],
    )

    con.commit()
    con.close()
    print(f"Initialized {DB_PATH}")

if __name__ == "__main__":
    main()
