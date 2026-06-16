CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    created_at DATETIME
);

CREATE TABLE accounts(
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    user_id INTEGER,
    account_no TEXT,
    balance REAL,
    
    FOREIGN KEY(user_id)
    REFERENCES users(id)
);

CREATE TABLE transactions(
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    user_id INTEGER,
    type TEXT,
    category TEXT,
    amount REAL,
    description TEXT,
    created_at DATETIME
);

CREATE TABLE savings(
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    target_amount REAL,
    saved_amount REAL,
    deadline DATE
);

CREATE TABLE recommendations(
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    user_id INTEGER,
    recommended_amount REAL,
    message TEXT,
    created_at DATETIME
);