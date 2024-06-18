-- Script: 12-no_cheating.sql

-- Purpose: Update the score of Bob to 10 in the table second_table of the hbtn_0c_0 database

-- Author: [Your Name]

-- Date: [Date]

USE hbtn_0c_0;

-- Update statement to set Bob's score to 10 based on his name
UPDATE second_table
SET score = 10
WHERE name = 'Bob';

