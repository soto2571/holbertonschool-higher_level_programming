-- Script: 13-change_class.sql

-- Purpose: Remove all records with a score <= 5 in the table second_table of the hbtn_0c_0 database

-- Author: [Your Name]

-- Date: [Date]

USE hbtn_0c_0;

-- Delete statement to remove records with score <= 5
DELETE FROM second_table
WHERE score <= 5;

