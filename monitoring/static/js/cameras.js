document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/streams/')
        .then(response => response.json())
        .then(data => {
            const streamGrid = document.getElementById('stream-grid');
            streamGrid.innerHTML = '';
            data.forEach((stream) => {
                const cameraName = stream.camera.name.toLowerCase().replace(/\s+/g, '-');

                const streamCard = document.createElement('div');
                streamCard.className = 'stream-card bg-secondary rounded-lg overflow-hidden';

                streamCard.innerHTML = `
                    <div class="relative">
                        <iframe 
                            src="http://localhost:8889/stream/${cameraName}" 
                            class="w-full h-48 bg-gray-800"
                            allow="autoplay; fullscreen"
                            frameborder="0">
                        </iframe>
                        <div class="absolute top-4 left-4 bg-${stream.status === 'live' ? 'green' : 'red'}-600 text-white text-xs font-medium px-2 py-1 rounded-full">
                            ${stream.status}
                        </div>
                    </div>
                    <div class="p-4">
                        <h3 class="text-white font-semibold">${stream.camera.name}</h3>
                        <p class="text-gray-400 text-sm">
                            ${stream.camera.resolution} | ${stream.camera.fps}fps | ${stream.camera.zone}
                        </p>
                    </div>
                `;
                streamGrid.appendChild(streamCard);
            });
        })
        .catch(error => console.error('Chyba pri načítaní streamov:', error));

    // Vyhľadávanie streamov
    const searchInput = document.getElementById('stream-search');
    searchInput.addEventListener('input', function () {
        const query = this.value.toLowerCase();
        fetch(`/api/streams/?search=${query}`)
            .then(response => response.json())
            .then(data => {
                const streamGrid = document.getElementById('stream-grid');
                streamGrid.innerHTML = '';
                data.forEach((stream) => {
                    const cameraName = stream.camera.name.toLowerCase().replace(/\s+/g, '-');

                    const streamCard = document.createElement('div');
                    streamCard.className = 'stream-card bg-secondary rounded-lg overflow-hidden';

                    streamCard.innerHTML = `
                        <div class="relative">
                            <iframe 
                                src="http://localhost:8889/stream/${cameraName}" 
                                class="w-full h-48 bg-gray-800"
                                allow="autoplay; fullscreen"
                                frameborder="0">
                            </iframe>
                            <div class="absolute top-4 left-4 bg-${stream.status === 'live' ? 'green' : 'red'}-600 text-white text-xs font-medium px-2 py-1 rounded-full">
                                ${stream.status}
                            </div>
                        </div>
                        <div class="p-4">
                            <h3 class="text-white font-semibold">${stream.camera.name}</h3>
                            <p class="text-gray-400 text-sm">
                                ${stream.camera.resolution} | ${stream.camera.fps}fps | ${stream.camera.zone}
                            </p>
                        </div>
                    `;
                    streamGrid.appendChild(streamCard);
                });
            })
            .catch(error => console.error('Chyba pri vyhľadávaní streamov:', error));
    });
});


function openModal() {
  document.getElementById('cameraModal').classList.remove('hidden');
}

function closeModal() {
  document.getElementById('cameraModal').classList.add('hidden');
}

function openEditModal(id, name, rtspUrl) {
  document.getElementById('editCameraId').value = id;
  document.getElementById('editCameraName').value = name;
  document.getElementById('editCameraRTSP').value = rtspUrl;
  document.getElementById('editModal').classList.remove('hidden');
}

function closeEditModal() {
  document.getElementById('editModal').classList.add('hidden');
}

function submitCamera() {
  const name = document.getElementById('cameraName').value;
  const rtsp_url = document.getElementById('rtspUrl').value;
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  fetch('/api/cameras/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({ name, rtsp_url })
  })
    .then(response => response.json())
    .then(data => {
      closeModal();
      fetchCameras();
    })
    .catch(error => {
      console.error('Error adding camera:', error);
    });
}

function setupEditFormHandler() {
  const form = document.getElementById('editCameraForm');
  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const id = document.getElementById('editCameraId').value;
    const name = document.getElementById('editCameraName').value;
    const rtsp_url = document.getElementById('editCameraRTSP').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(`/api/cameras/${id}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({ name, rtsp_url })
    })
      .then(response => {
        if (!response.ok) throw new Error('Failed to update');
        return response.json();
      })
      .then(data => {
        closeEditModal();
        fetchCameras();
      })
      .catch(error => {
        alert('Edit failed');
        console.error(error);
      });
  });
}
