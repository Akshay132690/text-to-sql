from app.database import get_connection


def execute_query(sql: str):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(sql)

        columns = [desc[0] for desc in cursor.description]

        rows = cursor.fetchall()

        return [
            dict(zip(columns, row))
            for row in rows
        ]

    finally:
        cursor.close()
        connection.close()