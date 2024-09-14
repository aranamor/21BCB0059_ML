function searchDocuments() {
    const query = document.getElementById('search-query').value;
    const user_id = prompt("Please enter your user ID:");

    if (!user_id) {
        alert("User ID is required for searching.");
        return;
    }

    // Make an API request to the /search endpoint
    fetch(`/search?text=${query}&user_id=${user_id}`)
        .then(response => {
            if (response.status === 429) {
                alert("Rate limit exceeded. Please wait before making more requests.");
                return;
            }
            return response.json();
        })
        .then(data => {
            const resultContainer = document.getElementById('search-results');
            if (data.results) {
                resultContainer.innerHTML = `<h3>Results from ${data.source}:</h3>`;
                data.results.forEach(doc => {
                    resultContainer.innerHTML += `
                        <div class="document">
                            <h4>${doc.title}</h4>
                            <p>${doc.content}</p>
                        </div>
                    `;
                });
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
}
