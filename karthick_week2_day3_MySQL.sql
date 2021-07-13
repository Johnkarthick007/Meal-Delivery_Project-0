CREATE TABLE mytable(
   meal_id  INTEGER  NOT NULL PRIMARY KEY,
   category VARCHAR(12) NOT NULL,
   cuisine  VARCHAR(11) NOT NULL
);
    
-- Find
SELECT * FROM mytable;

-- Find One
SELECT * FROM mytable
WHERE meal_id = 11;

-- Limit
SELECT * FROM mytable
LIMIT 5;

-- update one
UPDATE mytable
SET category = "apple"
WHERE meal_id = 11;

SELECT * FROM mytable WHERE meal_id = 11;

-- update many
UPDATE mytable
SET category = "Fish" 
WHERE cuisine = "Thai";

SELECT * FROM mytable WHERE cuisine = "Thai";

-- drop
DROP TABLE mytable;

-- delete one
DELETE FROM mytable
WHERE meal_id = 12;

SELECT * FROM mytable WHERE meal_id = 12;

-- delete many
DELETE FROM mytable
WHERE cuisine = "Continental";

SELECT * FROM mytable WHERE cuisine = "Continental";

-- Insert One
INSERT INTO mytable(meal_id, category, cuisine) 
VALUES (11, "pizza", "Indian");


-- Insert Many
INSERT INTO mytable(meal_id, category, cuisine) 
VALUES
	(11, "pizza", "Indian"), 
    (12, "pie", "Indian"),
    (13, "pizza", "Italian");

-- Inserted id
SELECT LAST_INSERT_ID();

SELECT meal_id FROM mytable;

-- Sort
SELECT * FROM mytable
ORDER BY cuisine ASC;