CREATE DATABASE IF NOT EXISTS user_db;
USE user_db;

CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    edad INT,
    is_admin BOOLEAN
);

CREATE TABLE IF NOT EXISTS Medidas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha DATE,
    frecuencia_cardiaca INT,
    tipo VARCHAR(50),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Configuraciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    frecuencia_monitoreo INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Alarmas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha DATE,
    tipo ENUM('alto', 'bajo'),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE
);