let map = null;
let marker = null;

<<<<<<< HEAD
// Fonction pour charger les shiled selon la ferme sélectionné
=======
// Fonction pour charger les capteurs selon le SHIELD sélectionné
>>>>>>> 8d4992b04bca0766ff43aada8645b7c63a77064c
async function loadSensors() {
    const shieldGroup = document.getElementById('shieldSelect').value;
    
    const response = await fetch(`/get_sensors/${shieldGroup}`);
    const sensors = await response.json();
    
    const sensorSelect = document.getElementById('sensorSelect');
    sensorSelect.innerHTML = '';

    sensors.forEach(sensor => {
        const option = document.createElement('option');
        option.value = sensor.id;
        option.textContent = sensor.id;
        sensorSelect.appendChild(option);
    });

    if (sensors.length > 0) {
        loadSensorData(); // Charge le 1er capteur automatiquement
    }
}

// Fonction pour charger les données du capteur sélectionné + afficher sur carte
async function loadSensorData() {
    const sensorId = document.getElementById('sensorSelect').value;
    const response = await fetch(`/get_sensor_data/${sensorId}`);
    const data = await response.json();

    document.getElementById('longitude').textContent = data.longitude;
    document.getElementById('latitude').textContent = data.latitude;
<<<<<<< HEAD
    //document.getElementById('type').textContent = data.type;
    //document.getElementById('unit').textContent = data.unit;
    //document.getElementById('pin').textContent = data.pin;
=======
    document.getElementById('type').textContent = data.type;
    document.getElementById('unit').textContent = data.unit;
    document.getElementById('pin').textContent = data.pin;
>>>>>>> 8d4992b04bca0766ff43aada8645b7c63a77064c

    const lat = data.latitude;
    const lon = data.longitude;

    // Initialisation ou mise à jour de la carte
    if (!map) {
        map = L.map('map').setView([lat, lon], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap'
        }).addTo(map);
        marker = L.marker([lat, lon]).addTo(map)
<<<<<<< HEAD
            .bindPopup(`Capteur : ${sensorId}<br>`).openPopup();
    } else {
        map.setView([lat, lon], 13);
        marker.setLatLng([lat, lon])
            .setPopupContent(`Capteur : ${sensorId}<br>`)
=======
            .bindPopup(`Capteur : ${sensorId}<br>Type : ${data.type}<br>Unité : ${data.unit}`).openPopup();
    } else {
        map.setView([lat, lon], 13);
        marker.setLatLng([lat, lon])
            .setPopupContent(`Capteur : ${sensorId}<br>Type : ${data.type}<br>Unité : ${data.unit}`)
>>>>>>> 8d4992b04bca0766ff43aada8645b7c63a77064c
            .openPopup();
    }
}

// Appeler automatiquement au chargement
<<<<<<< HEAD
window.onload = loadSensors;
=======
window.onload = loadSensors;
>>>>>>> 8d4992b04bca0766ff43aada8645b7c63a77064c
