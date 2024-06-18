-- Script: 11-best_score.sql

-- Purpose: List all records with a score >= 10 in the table second_table of the hbtn_0c_0 database

-- Author: [Your Name]

-- Date: [Date]

USE hbtn_0c_0;

-- Query to select records with score >= 10 from second_table, ordered by score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

