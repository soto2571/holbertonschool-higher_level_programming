SELECT CONCAT('Table   Create Table') AS 'first_table',
       CONCAT(t.TABLE_NAME, '     ', t.CREATE_STATEMENT) AS 'first_table'
FROM INFORMATION_SCHEMA.TABLES t
WHERE t.TABLE_SCHEMA = 'hbtn_0c_0'
  AND t.TABLE_NAME = 'first_table';

