import json

from app.llm.client import ask_llm
from app.models import ClarificationResponse


SCHEMA = """
customers(
    id,
    name,
    city
)

products(
    id,
    name,
    category,
    price
)

orders(
    id,
    customer_id,
    order_date,
    status
)

order_items(
    id,
    order_id,
    product_id,
    quantity
)
"""


def check_clarity(question: str) -> ClarificationResponse:

    prompt = f"""
You are a query clarification engine.

Database schema:
{SCHEMA}

User question:
{question}

Determine whether the question is ambiguous or missing important information.

Examples of ambiguous queries:

"Who is the best customer?"
Ambiguous because "best" could mean highest spending,
most orders, or highest average order value.

"Show me popular products."
Ambiguous because popularity could mean sales quantity,
number of orders, or revenue.

"Show sales."
Ambiguous because the user has not specified
a time period or metric.

If the question is clear, return:

{{
    "is_ambiguous": false,
    "clarification_question": null
}}

If ambiguous, return:

{{
    "is_ambiguous": true,
    "clarification_question": "A concise question asking the user
    for the missing information."
}}

Return ONLY valid JSON.
"""

    result = ask_llm(prompt)

    try:
        data = json.loads(result)
        return ClarificationResponse(**data)

    except Exception:
        return ClarificationResponse(
            is_ambiguous=False,
            clarification_question=None
        )