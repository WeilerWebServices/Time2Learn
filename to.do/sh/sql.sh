#!/bin/bash

# Database variables
DB_NAME="time2learn_db"
DB_USER="your_db_user"
DB_HOST="localhost"

# SQL statements
psql -h $DB_HOST -U $DB_USER -d $DB_NAME <<EOF
-- Create your tables here
CREATE TABLE IF NOT EXISTS lessons (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    content TEXT
);

CREATE TABLE IF NOT EXISTS quizzes (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id),
    question TEXT,
    answer TEXT
);

-- Add more SQL code here as needed
EOF