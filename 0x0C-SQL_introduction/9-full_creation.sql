-- Create table 'second_table' in db 'hbtn_0c_0'
-- Add descriptions (id INT), (name VARCHAR(256)), (score INT)
-- db name will be passed as arg to mysql cmd
-- Not allowed to use SELECT or SHOW
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

-- Script should create 4 records
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
