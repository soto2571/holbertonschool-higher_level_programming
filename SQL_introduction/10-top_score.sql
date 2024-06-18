-- Script: 10-top_score.sql

-- Purpose: List all records of the table second_table in the hbtn_0c_0 database, ordered by score

-- Author: [Your Name]

-- Date: [Date]

USE hbtn_0c_0;

-- Query to select all records from second_table, ordered by score descending
SELECT score, name
FROM second_table
ORDER BY score DESC;

