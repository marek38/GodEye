document.addEventListener("DOMContentLoaded", function () {
    // Načítanie zoznamu alertov
    function loadAlerts(filter = 'all') {
        const url = filter === 'all' ? '/api/alerts/' : `/api/alerts/?alert_type=${filter}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const alertList = document.getElementById('alert-list');
                alertList.innerHTML = '';
                data.forEach(alert => {
                    const alertItem = document.createElement('div');
                    alertItem.className = 'alert-item flex items-center justify-between p-4 bg-gray-800 rounded-lg';
                    alertItem.innerHTML = `
                        <div>
                            <p class="text-white font-medium">${alert.alert_type} - ${alert.camera.name}</p>
                            <p class="text-gray-400 text-sm">${alert.camera.name} | ${new Date(alert.timestamp).toLocaleString()} | ${alert.severity} Priority</p>
                        </div>
                        <div class="flex space-x-2">
                            <button class="px-3 py-1 bg-primary text-black font-medium rounded-button hover:bg-yellow-500 view-alert" data-id="${alert.id}">View</button>
                            <button class="px-3 py-1 bg-gray-700 text-white font-medium rounded-button hover:bg-gray-600 acknowledge-alert" data-id="${alert.id}">Acknowledge</button>
                        </div>
                    `;
                    alertList.appendChild(alertItem);
                });

                // Pridanie event listenerov pre tlačidlá
                document.querySelectorAll('.view-alert').forEach(button => {
                    button.addEventListener('click', () => {
                        alert('Zobrazenie detailov alertu ID: ' + button.dataset.id);
                        // Tu môže byť logika pre zobrazenie detailov alertu
                    });
                });

                document.querySelectorAll('.acknowledge-alert').forEach(button => {
                    button.addEventListener('click', () => {
                        fetch(`/api/alerts/${button.dataset.id}/`, {
                            method: 'PATCH',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                            },
                            body: JSON.stringify({ status: 'acknowledged' })
                        })
                        .then(response => response.json())
                        .then(() => {
                            loadAlerts(filter); // Obnoviť zoznam
                        })
                        .catch(error => console.error('Chyba pri potvrdení alertu:', error));
                    });
                });
            })
            .catch(error => console.error('Chyba pri načítaní alertov:', error));
    }

    // Inicializácia načítania alertov
    loadAlerts();

    // Filtrovanie alertov
    document.querySelectorAll('.filter-btn').forEach(button => {
        button.addEventListener('click', function () {
            document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('bg-primary', 'text-black'));
            button.classList.add('bg-primary', 'text-black');
            loadAlerts(button.dataset.filter);
        });
    });

    // Vyhľadávanie alertov
    const searchInput = document.getElementById('alert-search');
    searchInput.addEventListener('input', function () {
        const query = this.value.toLowerCase();
        fetch(`/api/alerts/?search=${query}`)
            .then(response => response.json())
            .then(data => {
                const alertList = document.getElementById('alert-list');
                alertList.innerHTML = '';
                data.forEach(alert => {
                    const alertItem = document.createElement('div');
                    alertItem.className = 'alert-item flex items-center justify-between p-4 bg-gray-800 rounded-lg';
                    alertItem.innerHTML = `
                        <div>
                            <p class="text-white font-medium">${alert.alert_type} - ${alert.camera.name}</p>
                            <p class="text-gray-400 text-sm">${alert.camera.name} | ${new Date(alert.timestamp).toLocaleString()} | ${alert.severity} Priority</p>
                        </div>
                        <div class="flex space-x-2">
                            <button class="px-3 py-1 bg-primary text-black font-medium rounded-button hover:bg-yellow-500 view-alert" data-id="${alert.id}">View</button>
                            <button class="px-3 py-1 bg-gray-700 text-white font-medium rounded-button hover:bg-gray-600 acknowledge-alert" data-id="${alert.id}">Acknowledge</button>
                        </div>
                    `;
                    alertList.appendChild(alertItem);
                });
            })
            .catch(error => console.error('Chyba pri vyhľadávaní alertov:', error));
    });
});