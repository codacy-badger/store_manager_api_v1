CREATE TABLE IF NOT EXISTS cart (
  product_id TEXT NOT NULL,
  name VARCHAR(255) DEFAULT NULL,
  category VARCHAR(255) DEFAULT NULL,
  quantity SMALLINT DEFAULT NULL,
  quantity_sold SMALLINT DEFAULT NULL,
  price REAL DEFAULT NULL,
  sales SMALLINT DEFAULT NULL,
  created_timestamp TIMESTAMP DEFAULT NOW()
);