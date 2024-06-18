-- Script: 9-full_creation.sql

-- Purpose: Create a table second_table in the hbtn_0c_0 database and insert multiple rows

-- Author: [Your Name]

-- Date: [Date]

USE hbtn_0c_0;

-- Create second_table if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple rows into second_table
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);

-- Confirmation message
SELECT 'Table second_table created and populated successfully' AS 'Result';

