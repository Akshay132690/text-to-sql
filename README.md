# QueryPilot — Text-to-SQL with Clarification Engine

An LLM-powered Text-to-SQL assistant that converts natural-language questions into SQL queries while first detecting ambiguity and asking clarification questions when the user's intent is unclear.

Instead of blindly generating SQL, QueryPilot follows a safer workflow:

**User Question → Clarification Engine → SQL Generation → SQL Validation → MySQL → Results**

## 🚀 Live Demo

**Live Application:** https://text-to-sql-jkip.onrender.com/ui

**GitHub Repository:** https://github.com/Akshay132690/text-to-sql

> The application may take a few seconds to respond after inactivity because it is deployed on a free hosting tier.

## ✨ Key Features

* 🧠 **Natural Language to SQL** — Ask questions about the database using plain English.
* ❓ **Clarification Engine** — Detects ambiguous queries before SQL generation.
* 🔒 **SQL Validation** — Allows only `SELECT` queries and blocks destructive SQL operations.
* 🤖 **LLM Integration** — Uses Groq for natural-language understanding and SQL generation.
* 🗄️ **MySQL Database** — Executes validated SQL queries against a relational database.
* ⚡ **FastAPI Backend** — Lightweight REST API for processing queries.
* 🎨 **Interactive Web UI** — Simple interface for entering questions and viewing SQL/results.
* ☁️ **Cloud Deployment** — Backend deployed using Render with a managed MySQL database.

## 💡 Why Clarification Matters

Traditional Text-to-SQL systems may generate a query even when the user's question is ambiguous.

For example:

> **"Who is the best customer?"**

"Best" could mean:

* Customer with the highest total spending
* Customer with the most orders
* Customer with the highest average order value

Instead of guessing, QueryPilot asks the user to clarify their intended metric.

### Example

**User:**

```text
Who is the best customer?
```

**QueryPilot:**

```text
Do you mean the customer with the highest total spending,
the most orders, or the highest average order value?
```

After clarification, the system can generate the appropriate SQL query.

## 🏗️ Architecture

```text
                  ┌─────────────────┐
                  │   User Question │
                  └────────┬────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Clarification Engine│
                └──────────┬──────────┘
                           │
                  ┌────────┴────────┐
                  │                 │
              Ambiguous           Clear
                  │                 │
                  ▼                 ▼
          Clarification       SQL Generator
             Question               │
                                    ▼
                             SQL Validator
                                    │
                                    ▼
                              MySQL Database
                                    │
                                    ▼
                               Query Results
```

## 🛠️ Tech Stack

| Technology             | Purpose                                      |
| ---------------------- | -------------------------------------------- |
| Python                 | Core application logic                       |
| FastAPI                | Backend REST API                             |
| Groq                   | LLM-powered clarification and SQL generation |
| MySQL                  | Relational database                          |
| Pydantic               | Data validation                              |
| mysql-connector-python | MySQL connectivity                           |
| HTML/CSS/JavaScript    | Frontend UI                                  |
| Render                 | Backend deployment                           |
| Aiven                  | Managed MySQL database                       |

## 📁 Project Structure

```text
text-to-sql/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   │
│   ├── llm/
│   │   └── client.py
│   │
│   └── services/
│       ├── clarification.py
│       ├── sql_generator.py
│       ├── sql_validator.py
│       └── query_service.py
│
├── database/
│   └── schema.sql
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔄 How It Works

### 1. User submits a question

The user enters a natural-language question through the web interface.

Example:

```text
Show all customers from Pune
```

### 2. Clarification Engine

The system checks whether the question is ambiguous or missing important information.

If clarification is required, the system asks the user for additional information.

### 3. SQL Generation

For a clear question, the LLM generates a MySQL `SELECT` query based on the database schema.

Example:

```sql
SELECT *
FROM customers
WHERE city = 'Pune';
```

### 4. SQL Validation

The generated SQL is checked before execution.

The validator blocks operations such as:

```text
INSERT
UPDATE
DELETE
DROP
ALTER
TRUNCATE
CREATE
GRANT
REVOKE
```

Only `SELECT` queries are allowed.

### 5. Database Execution

The validated query is executed against MySQL.

### 6. Results

The query results are returned to the frontend and displayed to the user.

## ⚙️ Local Setup

### Prerequisites

* Python 3.10+
* MySQL 8+
* Groq API key

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd text-to-sql
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=text_to_sql

MODEL_NAME=openai/gpt-oss-20b
```

### 5. Create the database

Create the MySQL database:

```sql
CREATE DATABASE text_to_sql;
```

Then execute the schema:

```text
database/schema.sql
```

### 6. Start the application

```bash
python -m uvicorn app.main:app --reload
```

### 7. Open the application

```text
http://127.0.0.1:8000/ui
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## 🧪 Example Queries

### Clear Query

```text
Show all customers from Pune
```

### Aggregation

```text
Show the total number of orders for each customer
```

### Product Query

```text
Show all products in the Electronics category
```

### Ambiguous Query

```text
Who is the best customer?
```

The system should ask for clarification instead of making an assumption.

## 🔐 Security Considerations

The project includes a basic SQL validation layer designed to prevent destructive SQL operations generated by the LLM.

The current implementation:

* Allows only `SELECT` queries
* Blocks common write/DDL operations
* Prevents multiple SQL statements
* Validates the generated query before database execution

> This is a portfolio project and the validation layer should not be considered a complete production-grade SQL security system.

## 📌 Future Improvements

* Conversation-based clarification flow
* More advanced SQL parsing and validation
* Query result visualization
* Support for larger database schemas
* Authentication and authorization
* Query history
* Better error recovery
* Database schema discovery instead of hardcoded schema
* Streaming LLM responses
* More comprehensive test coverage

## 👨‍💻 Author

**Akshay Ingle**

Built as a portfolio project to explore LLM-powered database interaction, natural-language interfaces, and safer Text-to-SQL systems.
