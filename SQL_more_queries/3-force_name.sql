-- Use the specified database
USE ${DB_NAME};

-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

