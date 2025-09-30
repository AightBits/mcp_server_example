# MCP Server Session History

**Protocol:** Model Context Protocol (MCP) over HTTP/SSE  
**Client:** Claude AI (Web Interface)

---

## Table of Contents

- [Interaction 1: Get Customer by ID](#interaction-1-get-customer-by-id)
- [Interaction 2: Discover Available Commands](#interaction-2-discover-available-commands)
- [Interaction 3: Enumerate All Customers](#interaction-3-enumerate-all-customers)
- [Interaction 4: Aggregate Order Totals](#interaction-4-aggregate-order-totals)
- [Interaction 5: Export Session History](#interaction-5-export-session-history)
- [Session Summary](#session-summary)

---

## Interaction 1: Get Customer by ID

### User Request
```
Get customer 1.
```

### MCP Function Call
```json
{
  "function": "mcp_server_example:get_customer",
  "parameters": {
    "customer_id": 1
  }
}
```

### Function Result
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice@example.com"
}
```

### Assistant Response
| Field | Value |
|-------|-------|
| **Name** | Alice Johnson |
| **Email** | alice@example.com |
| **Customer ID** | 1 |

---

## Interaction 2: Discover Available Commands

### User Request
```
What other commands does the MCP server support?
```

### Assistant Response

The MCP server exposes three tools:

#### 1. `get_customer`
Fetches a single customer by their ID.

**Parameters:**
- `customer_id` (integer, required)

#### 2. `list_orders`
Lists orders with optional filtering.

**Parameters:**
- `customer_id` (integer, optional) - Filter orders by customer
- `min_amount` (number, optional) - Filter orders by minimum amount

#### 3. `sql_select`
Runs SELECT-only SQL queries against the demo database.

**Parameters:**
- `sql` (string, required) - A SELECT query to execute

---

## Interaction 3: Enumerate All Customers

### User Request
```
So if I asked you to enumerate all customers, can you?
```

### MCP Function Call
```json
{
  "function": "mcp_server_example:sql_select",
  "parameters": {
    "sql": "SELECT * FROM customers"
  }
}
```

### Function Result
```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice@example.com"
  },
  {
    "id": 2,
    "name": "Bob Smith",
    "email": "bob@example.com"
  },
  {
    "id": 3,
    "name": "Charlie Lee",
    "email": "charlie@example.com"
  }
]
```

### Assistant Response

Complete customer list from database:

| ID | Name | Email |
|----|------|-------|
| 1 | Alice Johnson | alice@example.com |
| 2 | Bob Smith | bob@example.com |
| 3 | Charlie Lee | charlie@example.com |

**Total Customers:** 3

---

## Interaction 4: Aggregate Order Totals

### User Request
```
Great! Can you show the dollar amount totals of all orders for each?
```

### MCP Function Call
```json
{
  "function": "mcp_server_example:sql_select",
  "parameters": {
    "sql": "SELECT customer_id, SUM(amount) as total_amount FROM orders GROUP BY customer_id"
  }
}
```

### Function Result
```json
[
  {
    "customer_id": 1,
    "total_amount": 1225.5
  },
  {
    "customer_id": 2,
    "total_amount": 130.0
  },
  {
    "customer_id": 3,
    "total_amount": 300.0
  }
]
```

### Assistant Response

Order totals by customer:

| Customer ID | Name | Total Order Amount |
|-------------|------|--------------------|
| 1 | Alice Johnson | **$1,225.50** |
| 2 | Bob Smith | $130.00 |
| 3 | Charlie Lee | $300.00 |

**Key Insight:** Alice Johnson accounts for 74% of total order value.

---

## Interaction 5: Export Session History

### User Request
```
How can I get the json or formatted output of this session including 
expanded thinking steps/code windows?
```

### Assistant Response

For information about:
- Exporting conversation history
- Accessing raw JSON outputs  
- Viewing expanded thinking or function call details
- Other application-specific functionality

**Resources:**
- [Claude Support Documentation](https://support.claude.com)
- [Claude API Documentation](https://docs.claude.com) (for API users)

> **Note:** API responses include the full conversation structure with all function calls, parameters, and results in JSON format.

---

## Session Summary

### Statistics

| Metric | Value |
|--------|-------|
| **Total Interactions** | 5 |
| **MCP Function Calls** | 3 |
| **Unique Tools Used** | 2 |
| **Database Queries** | 2 |

### Tools Usage Breakdown

```
get_customer    ████░░░░░░ 1 call  (33%)
sql_select      ████████░░ 2 calls (67%)
```

### Business Intelligence Insights

**Customer Base:**
- Total Customers: 3
- All customers have order history

**Order Analysis:**
- Total Order Value: **$1,655.50**
- Average per Customer: **$551.83**
- Highest Spender: Alice Johnson ($1,225.50)
- Lowest Spender: Bob Smith ($130.00)
- Revenue Concentration: Top customer represents 74% of total value

### Demonstrated Capabilities

✅ **Direct Tool Invocation** - Fetching specific records by ID  
✅ **Schema Discovery** - Listing available MCP tools  
✅ **Flexible Querying** - Using SQL for ad-hoc analysis  
✅ **Data Aggregation** - Computing totals and summaries  
✅ **Natural Language Interface** - No API syntax required from user

---

## Technical Notes

**Protocol:** Model Context Protocol (MCP)  
**Transport:** HTTP/SSE  
**Server Framework:** FastMCP  
**Database:** SQLite (demo.db)  
**Tables:** `customers`, `orders`

**Security Considerations:**
- Demo uses unauthenticated access
- SQL queries are SELECT-only (read-only)
- Production deployments should implement:
  - Authentication and authorization
  - Rate limiting
  - Query validation
  - Audit logging
