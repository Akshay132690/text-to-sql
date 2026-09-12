import json

from app.llm.client import ask_llm
from app.models import SQLResponse


SCHEMA = """
customers(
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    city VARCHAR
)

products(
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    category VARCHAR,
    price NUMERIC
)

orders(
    id SERIAL PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    status VARCHAR
)

order_items(
    id SERIAL PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT
)
"""


def generate_sql(question: str) -> SQLResponse:

    prompt = f"""
You are a PostgreSQL SQL generation system.

Database schema:
{SCHEMA}

User question:
{question}

Generate ONE SELECT query that answers the question.

Rules:

1. PostgreSQL syntax only.
2. Only SELECT queries are allowed.
3. Never use INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE.
4. Use correct table relationships.
5. Do not invent columns.
6. Return only JSON.

Format:

{{
    "sql": "SELECT ...",
    "explanation": "Short explanation of the query."
}}
"""

    result = ask_llm(prompt)

    data = json.loads(result)

    return SQLResponse(**data)