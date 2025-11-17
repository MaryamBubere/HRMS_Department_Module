CREATE DATABASE hrm_db;

USE hrm_db;

CREATE TABLE roles (
    role_id INT PRIMARY KEY AUTO_INCREMENT,
    role_name VARCHAR(100),
    description VARCHAR(200),
    created_at DATETIME,
    updated_at DATETIME,
    status BOOLEAN DEFAULT 1
);