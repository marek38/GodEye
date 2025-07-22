document.addEventListener("DOMContentLoaded", function () {
    // Prepínanie tabov
    const tabs = document.querySelectorAll('.settings-tab');
    const tabContents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', function () {
            tabs.forEach(t => {
                t.classList.remove('border-primary', 'text-primary');
                t.classList.add('border-transparent', 'text-gray-400');
            });
            tabContents.forEach(content => content.classList.add('hidden'));

            tab.classList.add('border-primary', 'text-primary');
            tab.classList.remove('border-transparent', 'text-gray-400');
            document.getElementById(`${tab.dataset.tab}-tab`).classList.remove('hidden');
        });
    });

    // Odoslanie formulára pre používateľov
    const userForm = document.querySelector('#users-tab form');
    if (userForm) {
        userForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(userForm);
            const data = {
                username: formData.get('username'),
                role: formData.get('role')
            };
            fetch('/api/users/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                alert('Používateľ pridaný úspešne!');
                userForm.reset();
            })
            .catch(error => console.error('Chyba pri pridávaní používateľa:', error));
        });
    }

    // Odoslanie formulára pre kamery
    const cameraForm = document.querySelector('#cameras-tab form');
    if (cameraForm) {
        cameraForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(cameraForm);
            const data = {
                name: formData.get('camera_name'),
                ip_address: formData.get('ip_address'),
                resolution: '1920x1080',
                fps: 30,
                zone: 'Default Zone',
                status: 'online',
                motion_detection: true,
                recording: true
            };
            fetch('/api/cameras/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                alert('Kamera pridaná úspešne!');
                cameraForm.reset();
            })
            .catch(error => console.error('Chyba pri pridávaní kamery:', error));
        });
    }

    // Načítanie zoznamu AI modelov
    fetch('/api/ai-models/')
        .then(response => response.json())
        .then(data => {
            const aiTab = document.getElementById('ai-tab');
            if (aiTab) {
                const modelList = document.createElement('div');
                modelList.className = 'space-y-4';
                data.forEach(model => {
                    const modelItem = document.createElement('div');
                    modelItem.className = 'p-4 bg-gray-800 rounded-lg';
                    modelItem.innerHTML = `
                        <p class="text-white font-medium">${model.name} v${model.version}</p>
                        <p class="text-gray-400 text-sm">${model.category} | Accuracy: ${model.accuracy}%</p>
                    `;
                    modelList.appendChild(modelItem);
                });
                aiTab.appendChild(modelList);
            }
        })
        .catch(error => console.error('Chyba pri načítaní AI modelov:', error));
});