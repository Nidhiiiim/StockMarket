CREATE TABLE stocks (
    id        INTEGER     PRIMARY KEY,
    name      STRING (60),
    sector_id INTEGER     REFERENCES sectors (id) 
);
