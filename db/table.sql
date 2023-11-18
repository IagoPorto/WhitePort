CREATE TABLE USER_DATA(
    ID SERIAL PRIMARY KEY,
    USER_NAME VARCHAR(40) UNIQUE,
    PASS VARCHAR(100)
);

CREATE TABLE WhitePort (
    ID serial PRIMARY KEY,
    FILE_TYPE varchar(20),
    MODIFICATION_DATE timestamp NOT NULL,
    PATH_FILE varchar(255),
    USER_NAME VARCHAR(40),
    FOREIGN KEY (USER_NAME) REFERENCES USER_DATA(USER_NAME)
);

INSERT INTO USER_DATA (USER_NAME, PASS) VALUES 
  ('user1', 'password1'),
  ('user2', 'password2');

INSERT INTO WhitePort (FILE_TYPE, MODIFICATION_DATE, PATH_FILE, USER_NAME)
VALUES 
  ('json', NOW(), '/app/archivos/10.json', 'user1'),
  ('png', NOW(), '/app/archivos/10.png', 'user1'),
  ('yml', NOW(), '/app/archivos/10.yml', 'user1'),
  ('txt', NOW(), '/app/archivos/1.txt', 'user1'),
  ('java', NOW(), '/app/archivos/2.java', 'user2'),
  ('py', NOW(), '/app/archivos/3.py', 'user2'),
  ('c', NOW(), '/app/archivos/4.c', 'user2'),
  ('pp', NOW(), '/app/archivos/5.pp', 'user2'),
  ('js', NOW(), '/app/archivos/6.js', 'user2'),
  ('md', NOW(), '/app/archivos/7.md', 'user2'),
  ('jpg', NOW(), '/app/archivos/8.jpg', 'user2'),
  ('cpp', NOW(), '/app/archivos/9.cpp', 'user2');

  