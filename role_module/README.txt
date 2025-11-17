Role Management Module (Module 2)
--------------------------------

Files included:
- app.py            : Flask application (single-file backend)
- templates/        : HTML templates (dashboard, create, edit)
- schema.sql        : Exact SQL queries to create database and roles table (DO NOT MODIFY)
- requirements.txt  : Python dependencies

Database setup (run these EXACTLY as-is in your MySQL client):

> CREATE DATABASE hrm_db;
> USE hrm_db;
> CREATE TABLE roles (
>     role_id INT PRIMARY KEY AUTO_INCREMENT,
>     role_name VARCHAR(100),
>     description VARCHAR(200),
>     created_at DATETIME,
>     updated_at DATETIME,
>     status BOOLEAN DEFAULT 1
> );

Running locally:
1. Install dependencies: pip install -r requirements.txt
2. Make sure MySQL/MariaDB is running and you can connect with user 'root' and no password.
   If your DB credentials differ, update the get_db() function in app.py.
3. Run: python app.py
4. Open http://127.0.0.1:5000/ in your browser.

 