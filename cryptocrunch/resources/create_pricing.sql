CREATE TABLE IF NOT EXISTS pricing (
    exchange TEXT,
    pair TEXT,
    price NUMERIC,
    write_timestamp INTEGER,
    source TEXT
)
;

CREATE INDEX IF NOT EXISTS idx_pricing_market_pair ON pricing (exchange, pair)
;

CREATE INDEX IF NOT EXISTS idx_pricing_write_time ON pricing (write_timestamp)
;
