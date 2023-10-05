CREATE TABLE IF NOT EXISTS payment(
    id SERIAL PRIMARY KEY ,
    user_id INT,
    summa INT,
    reg_date date
);

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY ,
    tg_id INT,
    username VARCHAR(50),
    reg_date date, 
    status VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS category(
    id SERIAL PRIMARY KEY ,
    name varchar(20) 
);

CREATE TABLE IF NOT EXISTS book(
    id SERIAL PRIMARY KEY ,
    name varchar(20),
    file varchar(20),
    add_date date  
    category_id int
);