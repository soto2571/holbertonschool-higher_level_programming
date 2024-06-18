-- Script to list all tables in a specific database
USE `mysql`; -- Replace `mysql` with the database name passed as an argument

-- Query to list all tables in the current database
SELECT table_name AS Tables_in_database
FROM information_schema.tables
WHERE table_schema = DATABASE();

