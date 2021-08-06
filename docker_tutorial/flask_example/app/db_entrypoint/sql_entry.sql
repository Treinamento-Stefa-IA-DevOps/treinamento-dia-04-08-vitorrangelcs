CREATE DATABASE my_db;

-- connect to the newly created database
\c my_db

CREATE TABLE hello_world (
    id SERIAL PRIMARY KEY,
    text VARCHAR(200) NOT NULL
);

INSERT INTO
    hello_world (text)
VALUES
    ('Hello,'), (' World'), ('!');