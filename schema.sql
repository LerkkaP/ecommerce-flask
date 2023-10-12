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
    watch_id INTEGER REFERENCES watches ON DELETE CASCADE,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    review TEXT,
    rating INTEGER,
    review_date DATE
);

CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    watch_id INTEGER REFERENCES watches ON DELETE CASCADE,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    quantity INTEGER
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER REFERENCES users ON DELETE CASCADE, 
    watch_id INTEGER REFERENCES watches ON DELETE CASCADE,
    first_name TEXT,
    last_name TEXT,
    shipping_address TEXT,
    billing_address TEXT,
    phone_number TEXT,
    email TEXT,
    quantity INTEGER,
    payment_method TEXT,
    order_date DATE
);