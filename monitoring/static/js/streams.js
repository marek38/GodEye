document.addEventListener("DOMContentLoaded", function () {
    // Načítanie zoznamu streamov
    fetch('/api/streams/')
        .then(response => response.json())
        .then(data => {
            const streamGrid = document.getElementById('stream-grid');
            streamGrid.innerHTML = '';
            data.forEach((stream, index) => {
                const streamCard = document.createElement('div');
                streamCard.className = 'stream-card bg-secondary rounded-lg overflow-hidden';
                streamCard.innerHTML = `
                    <div class="relative">
                        <video id="video-player-${index}" class="w-full h-48 bg-gray-800" controls>
                            <source src="/hls/${stream.camera.name.toLowerCase().replace(' ', '-')}/index.m3u8" type="application/x-mpegURL">
                        </video>
                        <div class="absolute top-4 left-4 bg-${stream.status === 'live' ? 'green' : 'red'}-600 text-white text-xs font-medium px-2 py-1 rounded-full">${stream.status}</div>
                    </div>
                    <div class="p-4">
                        <h3 class="text-white font-semibold">${stream.camera.name}</h3>
                        <p class="text-gray-400 text-sm">${stream.camera.resolution} | ${stream.camera.fps}fps | ${stream.camera.zone}</p>
                    </div>
                `;
                streamGrid.appendChild(streamCard);

                // Inicializácia HLS pre každý stream
                const video = document.getElementById(`video-player-${index}`);
                if (Hls.isSupported()) {
                    const hls = new Hls();
                    hls.loadSource(`/hls/${stream.camera.name.toLowerCase().replace(' ', '-')}/index.m3u8`);
                    hls.attachMedia(video);
                    hls.on(Hls.Events.MANIFEST_PARSED, () => {
                        video.play();
                    });
                } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
                    video.src = `/hls/${stream.camera.name.toLowerCase().replace(' ', '-')}/index.m3u8`;
                    video.addEventListener('loadedmetadata', () => {
                        video.play();
                    });
                }
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
                data.forEach((stream, index) => {
                    const streamCard = document.createElement('div');
                    streamCard.className = 'stream-card bg-secondary rounded-lg overflow-hidden';
                    streamCard.innerHTML = `
                        <div class="relative">
                            <video id="video-player-${index}" class="w-full h-48 bg-gray-800" controls>
                                <source src="/hls/${stream.camera.name.toLowerCase().replace(' ', '-')}/index.m3u8" type="application/x-mpegURL">
                            </video>
                            <div class="absolute top-4 left-4 bg-${stream.status === 'live' ? 'green' : 'red'}-600 text-white text-xs font-medium px-2 py-1 rounded-full">${stream.status}</div>
                        </div>
                        <div class="p-4">
                            <h3 class="text-white font-semibold">${stream.camera.name}</h3>
                            <p class="text-gray-400 text-sm">${stream.camera.resolution} | ${stream.camera.fps}fps | ${stream.camera.zone}</p>
                        </div>
                    `;
                    streamGrid.appendChild(streamCard);
                });
            })
            .catch(error => console.error('Chyba pri vyhľadávaní streamov:', error));
    });
});