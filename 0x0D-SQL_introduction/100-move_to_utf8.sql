-- edit table structure after built it.
ALTER DATABASE hbtn_0c_0 DEFAULT COLLATE=utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
