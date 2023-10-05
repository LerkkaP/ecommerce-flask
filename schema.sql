CREATE TABLE watches (
    id SERIAL PRIMARY KEY,
    brand TEXT,
    model TEXT,
    price INTEGER,
    description TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    privileges TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    watch_id INTEGER REFERENCES watches,
    user_id INTEGER REFERENCES users,
    review TEXT,
    rating INTEGER,
    review_date DATE
);

CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    watch_id INTEGER REFERENCES watches,
    user_id INTEGER REFERENCES users
    quantity INTEGER
);