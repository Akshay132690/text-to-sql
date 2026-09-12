const questionInput = document.getElementById("question");
const askButton = document.getElementById("askButton");

const loading = document.getElementById("loading");

const clarification = document.getElementById("clarification");
const clarificationText = document.getElementById("clarificationText");

const sqlSection = document.getElementById("sqlSection");
const sqlCode = document.getElementById("sqlCode");

const resultsSection = document.getElementById("resultsSection");
const resultsTable = document.getElementById("resultsTable");

const errorSection = document.getElementById("errorSection");
const errorText = document.getElementById("errorText");


function useExample(text) {
    questionInput.value = text;
    questionInput.focus();
}


function hideResults() {

    clarification.classList.add("hidden");
    sqlSection.classList.add("hidden");
    resultsSection.classList.add("hidden");
    errorSection.classList.add("hidden");

}


async function askDatabase() {

    const question = questionInput.value.trim();

    if (!question) {
        questionInput.focus();
        return;
    }

    hideResults();

    loading.classList.remove("hidden");

    askButton.disabled = true;
    askButton.innerHTML = "Processing...";


    try {

        const response = await fetch("/query", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }


        /*
         * AMBIGUOUS QUESTION
         */

        if (data.clarification) {

            clarificationText.textContent = data.clarification;

            clarification.classList.remove("hidden");

            return;
        }


        /*
         * SQL
         */

        if (data.sql) {

            sqlCode.textContent = data.sql;

            sqlSection.classList.remove("hidden");

        }


        /*
         * RESULTS
         */

        if (data.answer) {

            renderTable(data.answer);

            resultsSection.classList.remove("hidden");

        }

    }

    catch (error) {

        errorText.textContent = error.message;

        errorSection.classList.remove("hidden");

    }

    finally {

        loading.classList.add("hidden");

        askButton.disabled = false;

        askButton.innerHTML = `
            Ask Database
            <span>→</span>
        `;

    }

}


function renderTable(rows) {

    if (!rows || rows.length === 0) {

        resultsTable.innerHTML = `
            <p style="padding:15px;color:#777;">
                No results found.
            </p>
        `;

        return;
    }


    const columns = Object.keys(rows[0]);


    let html = "<table>";


    html += "<thead><tr>";

    columns.forEach(column => {

        html += `<th>${formatColumn(column)}</th>`;

    });

    html += "</tr></thead>";


    html += "<tbody>";


    rows.forEach(row => {

        html += "<tr>";

        columns.forEach(column => {

            html += `<td>${formatValue(row[column])}</td>`;

        });

        html += "</tr>";

    });


    html += "</tbody></table>";


    resultsTable.innerHTML = html;

}


function formatColumn(column) {

    return column
        .replaceAll("_", " ")
        .replace(/\b\w/g, letter => letter.toUpperCase());

}


function formatValue(value) {

    if (value === null || value === undefined) {
        return "-";
    }

    return String(value);

}


questionInput.addEventListener("keydown", function (event) {

    if (event.key === "Enter" && event.ctrlKey) {

        askDatabase();

    }

});