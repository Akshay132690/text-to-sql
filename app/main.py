from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException

from app.models import QueryRequest, QueryResult
from app.services.clarification import check_clarity
from app.services.sql_generator import generate_sql
from app.services.sql_validator import validate_sql
from app.services.query_service import execute_query


app = FastAPI(
    title="Text-to-SQL Clarification Engine",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/ui")
def ui():
    return FileResponse("static/index.html")

@app.get("/")
def home():
    return {
        "message": "Text-to-SQL Clarification Engine is running"
    }


@app.post("/query", response_model=QueryResult)
def process_query(request: QueryRequest):

    question = request.question

    # Step 1: Check ambiguity
    clarification = check_clarity(question)

    if clarification.is_ambiguous:

        return QueryResult(
            question=question,
            clarification=clarification.clarification_question
        )

    # Step 2: Generate SQL
    sql_response = generate_sql(question)

    # Step 3: Validate SQL
    valid, message = validate_sql(sql_response.sql)

    if not valid:
        raise HTTPException(
            status_code=400,
            detail=message
        )

    # Step 4: Execute
    try:
        result = execute_query(sql_response.sql)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

    return QueryResult(
        question=question,
        sql=sql_response.sql,
        answer=result
    )