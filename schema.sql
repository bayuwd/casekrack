CREATE TABLE challenges (
    id UUID PRIMARY KEY,
    user_id UUID,
    day_number INT,
    industry TEXT,
    discipline TEXT,
    link_url TEXT,
    completed_at TIMESTAMP
);
