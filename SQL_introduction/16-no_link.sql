-- Script: 16-no_link.sql

-- Purpose: List all records of the table second_table of the database hbtn_0c_0 where name is not null

-- Author: [Your Name]

-- Date: [Date]

USE hbtn_0c_0;

-- Query to select records with score and name, filtering out rows where name is null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

