import os
from flask import Flask, render_template, request, redirect
from datetime import datetime

USE_SQLITE = os.environ.get("USE_SQLITE", "false").lower() == "true"

app = Flask(__name__)

if USE_SQLITE:
    # --- SQLite DB for Render hosting ---
    import sqlite3
    def get_db():
        conn = sqlite3.connect("hrms.db", check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    # Create table if not exists
    conn = sqlite3.connect("hrms.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS role (
            role_id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_name TEXT,
            description TEXT,
            created_at TEXT,
            updated_at TEXT,
            status INTEGER DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()

else:
    # --- MySQL DB for LOCAL running ---
    import mysql.connector
    def get_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root75",
            database="hrm_db"
        )
