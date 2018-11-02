CREATE TABLE IF NOT EXISTS sales (
  sale_id TEXT NOT NULL PRIMARY KEY,
  attendant VARCHAR(255) DEFAULT NULL,
  total_product VARCHAR(255) DEFAULT NULL,
  total_amount VARCHAR(255) DEFAULT NULL,
  quantity_sold SMALLINT DEFAULT NULL,
  created_timestamp TIMESTAMP DEFAULT NOW()
);