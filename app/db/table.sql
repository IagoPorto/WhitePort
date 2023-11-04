CREATE TABLE WhitePort (
    ID serial PRIMARY KEY,
    type varchar(20),
    date timestamp NOT NULL,
    file bytea
);