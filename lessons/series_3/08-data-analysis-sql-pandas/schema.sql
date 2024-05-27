CREATE TABLE IF NOT EXISTS links (
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(255),
  url TEXT,
  created_at TIMESTAMP,
  upvotes INTEGER,
  downvotes INTEGER
);
