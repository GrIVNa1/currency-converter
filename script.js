function getCurrencyRates() {
    const currency = document.getElementById("currency").value;
    const resultDiv = document.getElementById("result");
    const errorDiv = document.getElementById("error");

    resultDiv.innerHTML = "";
    errorDiv.innerHTML = "";

    fetch(`http://127.0.0.1:8000/currency/${currency}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Ошибка при получении данных");
            }
            return response.json();
        })
        .then(data => {
            let resultHTML = `<h3>Курс ${currency}:</h3><ul>`;
            for (const [key, value] of Object.entries(data)) {
                resultHTML += `<li>1 ${currency} = ${value.value} ${key}</li>`;
            }
            resultHTML += "</ul>";
            resultDiv.innerHTML = resultHTML;
        })
        .catch(error => {
            errorDiv.innerHTML = "Не удалось получить курс. Проверьте сервер.";
        });
}
