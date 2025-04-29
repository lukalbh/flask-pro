// Fonction pour charger les capteurs selon le SHIELD sélectionné
async function loadSensors() {
    const shieldGroup = document.getElementById('shieldSelect').value; // Récupère la valeur du SHIELD sélectionné
    
    // Effectue une requête pour récupérer les capteurs du SHIELD choisi
    const response = await fetch(`/get_sensors/${shieldGroup}`);
    const sensors = await response.json(); // Parse la réponse JSON
    
    const sensorSelect = document.getElementById('sensorSelect');
    sensorSelect.innerHTML = ''; // Vider le select existant

    // Ajout des options dynamiquement dans le select
    sensors.forEach(sensor => {
        const option = document.createElement('option');
        option.value = sensor.id; // L'id du capteur
        option.textContent = sensor.id; // Le nom du capteur (par exemple : sensor_1)
        sensorSelect.appendChild(option); // Ajoute l'option au select
    });

    if (sensors.length > 0) {
        loadSensorData(); // Charge les données du premier capteur si disponible
    }
}

// Fonction pour charger les données du capteur sélectionné
async function loadSensorData() {
    const sensorId = document.getElementById('sensorSelect').value; // Récupère l'id du capteur sélectionné
    const response = await fetch(`/get_sensor_data/${sensorId}`);
    const data = await response.json();

    // Mise à jour des informations du capteur dans la page
    document.getElementById('longitude').textContent = data.longitude;
    document.getElementById('latitude').textContent = data.latitude;
    document.getElementById('type').textContent = data.type;
    document.getElementById('unit').textContent = data.unit;
    document.getElementById('pin').textContent = data.pin;
}

// Appel de la fonction au chargement de la page pour afficher les capteurs du SHIELD 1 par défaut
window.onload = loadSensors;