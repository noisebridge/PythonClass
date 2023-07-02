CREATE TABLE IF NOT EXISTS links (
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(255),
  url TEXT,
  created_at TIMESTAMP,
  upvotes INTEGER,
  downvotes INTEGER
);

CREATE TABLE IF NOT EXISTS users (
  id INTEGER NOT NULL PRIMARY KEY,
  email TEXT,
  hashed_password VARCHAR(255),
  profile TEXT
);