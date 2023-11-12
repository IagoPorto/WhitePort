CREATE TABLE USER(
    ID SERIAL PRIMARY KEY,
    USER_NAME VARCHAR(40),
    PASS VARCHAR(100)
);

CREATE TABLE WhitePort (
    ID serial PRIMARY KEY,
    FILE_TYPE varchar(20),
    MODIFICATION_DATE timestamp NOT NULL,
    PATH_FILE varchar(255),
    USER_NAME VARCHAR(40),  -- Debe coincidir con el tamaño de tu_tabla_principal.user_name
    FOREIGN KEY (USER_NAME) REFERENCES USER(USER_NAME)
);