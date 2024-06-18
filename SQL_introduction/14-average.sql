-- Script: 14-average.sql

-- Purpose: Compute the score average of all records in the table second_table of the hbtn_0c_0 database

-- Author: [Your Name]

-- Date: [Date]

USE hbtn_0c_0;

-- Query to compute the average score
SELECT AVG(score) AS average
FROM second_table;

