-- edit table structure after built it.
ALTER DATABASE hbtn_0c_0 DEFAULT COLLATE=utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
