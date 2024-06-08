CREATE SCHEMA SCHEMA airquality_db;


CREATE TABLE IF NOT EXISTS airquality_db.airquality_data(
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    overall_aqi INTEGER,
    date DATE,
    time TIME
);