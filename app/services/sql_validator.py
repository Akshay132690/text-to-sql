import re


FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE"
]


def validate_sql(sql: str) -> tuple[bool, str]:

    cleaned = sql.strip().upper()

    if not cleaned.startswith("SELECT"):
        return False, "Only SELECT queries are allowed."

    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", cleaned):
            return False, f"Forbidden SQL operation: {keyword}"

    if ";" in cleaned[:-1]:
        return False, "Multiple SQL statements are not allowed."

    return True, "SQL is valid."