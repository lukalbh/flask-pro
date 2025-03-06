-- Création de la table capteurs
CREATE TABLE IF NOT EXISTS capteurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_capteur VARCHAR(50) NOT NULL,
    temperature DECIMAL(4,1),  -- Permet des valeurs comme 25.5
    humidite DECIMAL(4,1),    -- Permet des valeurs comme 85.5
    date_mesure TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_date (date_mesure),  -- Index pour optimiser les recherches par date
    INDEX idx_capteur (id_capteur) -- Index pour optimiser les recherches par capteur
);

-- Insertion de quelques données de test
INSERT INTO capteurs (id_capteur, temperature, humidite) VALUES
    ('CAPTEUR_01', 24.5, 65.0),
    ('CAPTEUR_01', 23.8, 67.2),
    ('CAPTEUR_01', 25.2, 63.5),
    ('CAPTEUR_01', 22.9, 70.1),
    ('CAPTEUR_01', 24.0, 68.5),
    ('CAPTEUR_01', 26.1, 62.8),
    ('CAPTEUR_01', 23.5, 66.3); 