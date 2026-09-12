import json

from app.llm.client import ask_llm
from app.models import SQLResponse


SCHEMA = """
customers(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
)

products(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    price DECIMAL(12,2)
)

orders(
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    status VARCHAR(30)
)

order_items(
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT
)
"""


def generate_sql(question: str) -> SQLResponse:
    prompt = f"""
You are a MySQL SQL generation system.

Database schema:
{SCHEMA}

User question:
{question}

Generate ONE SELECT query that answers the question.

Rules:
1. Use MySQL 8+ syntax only.
2. Only SELECT queries are allowed.
3. Never use INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, CREATE, GRANT, or REVOKE.
4. Use the correct relationships between tables.
5. Do not invent tables or columns.
6. Return only valid JSON.

Format:
{{
    "sql": "SELECT ...",
    "explanation": "Short explanation of the query."
}}
"""

    result = ask_llm(prompt)
    data = json.loads(result)

    return SQLResponse(**data)