from pydantic import BaseModel, Field
from typing import List


class QueryRequest(BaseModel):
    question: str = Field(min_length=3)


class ClarificationResponse(BaseModel):
    is_ambiguous: bool
    clarification_question: str | None = None


class SQLResponse(BaseModel):
    sql: str
    explanation: str


class QueryResult(BaseModel):
    question: str
    sql: str | None = None
    answer: List[dict] | None = None
    clarification: str | None = None