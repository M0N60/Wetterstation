/* 
    Befehle

    SELECT - extracts data from a database
    UPDATE - updates data in a database
    DELETE - deletes data from a database
    INSERT INTO - inserts new data into a database
    CREATE DATABASE - creates a new database
    ALTER DATABASE - modifies a database
    CREATE TABLE - creates a new table
    ALTER TABLE - modifies a table
    DROP TABLE - deletes a table
    CREATE INDEX - creates an index (search key)
    DROP INDEX - deletes an index
*/
--  ! HELP XD !       https://www.w3schools.com/sql/sql_select.asp

CREATE DATABASE Wetterdaten
CREATE TABLE Niederschlag (
    column1 VARCHAR(255),
    column2 VARCHAR(255),
    column3 VARCHAR(255),
    --  column_name  datatype(size),
); 


BACKUP DATABASE Wetterdaten
TO DISK = 'filepath'; --zb backups\Wetterdaten.bak 