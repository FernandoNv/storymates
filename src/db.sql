CREATE DATABASE storymates;

CREATE TABLE article(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  content TEXT NOT NULL,
  author VARCHAR(100) NOT NULL,
  createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
);

CREATE TABLE comment(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  content TEXT NOT NULL,
  author VARCHAR(100) NOT NULL,
  createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  idArticle INT NOT NULL,
  CONSTRAINT id_article_fk FOREIGN KEY(idArticle)
    REFERENCES article(id)
    ON DELETE CASCADE
);

INSERT INTO article(id, title, content, author) values(null, 'What is Lorem Ipsum?', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has Ipsum.', 'fernando');
INSERT INTO article(id, title, content, author) values(null, 'What is Ipsum?', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has Ipsum.', 'henrique');
INSERT INTO article(id, title, content, author) values(null, 'What is Lorem?', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has Ipsum.', 'marcos');
INSERT INTO article(id, title, content, author) values(null, 'What is it?', 'Lorem the printing and typesetting industry. Lorem Ipsum has Ipsum.', 'fernando');
