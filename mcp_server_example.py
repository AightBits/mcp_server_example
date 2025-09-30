import sqlite3, json, re
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

DB_PATH = "demo.db"
mcp = FastMCP("mcp_server_example")

def query(sql: str, params: tuple = ()) -> List[Dict[str, Any]]:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(sql, params)
    rows = [dict(r) for r in cur.fetchall()]
    con.close()
    return rows

SELECT_ONLY = re.compile(r"^\s*select\b", re.IGNORECASE | re.DOTALL)

@mcp.tool()
def get_customer(customer_id: int) -> str:
    """Fetch a single customer by id."""
    data = query("SELECT id, name, email FROM customers WHERE id = ?", (int(customer_id),))
    return json.dumps(data[0] if data else {}, indent=2)

@mcp.tool()
def list_orders(customer_id: Optional[int] = None, min_amount: Optional[float] = None) -> str:
    """List orders (optional filters: customer_id, min_amount)."""
    sql = "SELECT id, customer_id, product, amount, order_date FROM orders WHERE 1=1"
    params: List[Any] = []
    if customer_id is not None:
        sql += " AND customer_id = ?"
        params.append(int(customer_id))
    if min_amount is not None:
        sql += " AND amount >= ?"
        params.append(float(min_amount))
    sql += " ORDER BY order_date, id"
    return json.dumps(query(sql, tuple(params)), indent=2)

@mcp.tool()
def sql_select(sql: str) -> str:
    """Run a SELECT-only SQL query against demo.db."""
    if not SELECT_ONLY.match(sql):
        return json.dumps({"error": "Only SELECT statements are allowed."}, indent=2)
    return json.dumps(query(sql), indent=2)

if __name__ == "__main__":
    # Run directly over HTTP so Claude web can connect to http://<host>:8000/mcp/
    mcp.run(transport="http", host="127.0.0.1", port=8000)
