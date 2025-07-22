document.addEventListener("DOMContentLoaded", function () {
    // Načítanie súhrnných dát (počet kamier, alertov, úložisko)
    fetch('/api/cameras/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-cameras').textContent = data.length;
        })
        .catch(error => console.error('Chyba pri načítaní kamier:', error));

    fetch('/api/alerts/?status=new')
        .then(response => response.json())
        .then(data => {
            document.getElementById('active-alerts').textContent = data.length;
        })
        .catch(error => console.error('Chyba pri načítaní alertov:', error));

    fetch('/api/storage/')
        .then(response => response.json())
        .then(data => {
            const totalUsed = data.reduce((sum, storage) => sum + storage.used_space, 0);
            const totalSpace = data.reduce((sum, storage) => sum + storage.total_space, 0);
            const usagePercent = Math.round((totalUsed / totalSpace) * 100);
            document.getElementById('storage-usage').textContent = `${usagePercent}%`;
        })
        .catch(error => console.error('Chyba pri načítaní úložiska:', error));

    // Načítanie recentných alertov
    fetch('/api/alerts/?limit=5')
        .then(response => response.json())
        .then(data => {
            const alertList = document.getElementById('recent-alerts');
            alertList.innerHTML = '';
            data.forEach(alert => {
                const alertItem = document.createElement('div');
                alertItem.className = 'alert-item flex items-center justify-between p-4 bg-gray-800 rounded-lg';
                alertItem.innerHTML = `
                    <div>
                        <p class="text-white font-medium">${alert.alert_type} - ${alert.camera.name}</p>
                        <p class="text-gray-400 text-sm">${alert.camera.name} | ${new Date(alert.timestamp).toLocaleString()}</p>
                    </div>
                    <button class="px-3 py-1 bg-primary text-black font-medium rounded-button hover:bg-yellow-500">View</button>
                `;
                alertList.appendChild(alertItem);
            });
        })
        .catch(error => console.error('Chyba pri načítaní recentných alertov:', error));

    // Načítanie stavu kamier
    fetch('/api/cameras/?limit=5')
        .then(response => response.json())
        .then(data => {
            const cameraStatus = document.getElementById('camera-status');
            cameraStatus.innerHTML = '';
            data.forEach(camera => {
                const cameraItem = document.createElement('div');
                cameraItem.className = 'flex items-center justify-between p-4 bg-gray-800 rounded-lg';
                cameraItem.innerHTML = `
                    <div>
                        <p class="text-white font-medium">${camera.name} - ${camera.zone}</p>
                        <p class="text-gray-400 text-sm">${camera.status} | ${camera.resolution} @ ${camera.fps}fps</p>
                    </div>
                    <span class="px-3 py-1 bg-${camera.status === 'online' ? 'green' : 'red'}-600 text-white text-sm rounded-full">${camera.status}</span>
                `;
                cameraStatus.appendChild(cameraItem);
            });
        })
        .catch(error => console.error('Chyba pri načítaní stavu kamier:', error));

    // Simulácia systémových metrík (v reálnom projekte by sa získavali z backendu)
    function updateSystemHealth() {
        document.getElementById('cpu-usage').textContent = `${Math.round(Math.random() * 100)}%`;
        document.getElementById('memory-usage').textContent = `${Math.round(Math.random() * 100)}%`;
        document.getElementById('network-usage').textContent = `${Math.round(Math.random() * 200)} Mbps`;
    }
    updateSystemHealth();
    setInterval(updateSystemHealth, 5000); // Aktualizácia každých 5 sekúnd
});