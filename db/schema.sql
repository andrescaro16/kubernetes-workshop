BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> a3cff50d71f8

CREATE TABLE film (
    id SERIAL NOT NULL, 
    title VARCHAR, 
    length INTEGER, 
    year INTEGER, 
    director VARCHAR, 
    PRIMARY KEY (id)
);

CREATE TABLE actor (
    id SERIAL NOT NULL, 
    name VARCHAR, 
    film_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(film_id) REFERENCES film (id)
);

INSERT INTO alembic_version (version_num) VALUES ('a3cff50d71f8') RETURNING alembic_version.version_num;

COMMIT;