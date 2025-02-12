document.getElementById('roadmap-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const role = document.getElementById('role').value;

    fetch('/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ role: role }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});