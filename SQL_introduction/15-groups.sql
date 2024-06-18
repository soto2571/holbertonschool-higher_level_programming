-- Script: 15-groups.sql

-- Purpose: List the number of records with the same score in the table second_table of the hbtn_0c_0 database

-- Author: [Your Name]

-- Date: [Date]

USE hbtn_0c_0;

-- Query to count records by score and sort by count descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;

