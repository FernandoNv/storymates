from datetime import datetime
from flask import Flask, request
from src.repository.db import db_article
# from flask_mysqldb import MySQL
# from src.server.instance import server

# app, api = server.app, server.api
 
# app.config['MYSQL_HOST'] = 'db:3306'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'storymates'
 
# mysql = MySQL(app)

class ArticleRepository():
  def get_all(self):
    # cursor = mysql.connection.cursor()
    # cursor.execute('SELECT * FROM articles;')
    # mysql.connection.commit()
    # cursor.close()

    return db_article


  def get_all_by_author(self, username):
    return list(filter(lambda item: item["author"] == username, db_article))


  def get_by_id(self, id_article):
    try:
      index_article = self.__findById(id_article)
      
      return db_article[index_article]
    except Exception as e:
      raise e


  def save(self, new_article_dto):
    new_article = {
      'id': len(db_article)+1,
      'title': new_article_dto['title'],
      'content': new_article_dto['content'],
      'author': new_article_dto['author'],
      'createdAt': datetime.now(),
      'updatedAt': None
    }
    db_article.append(new_article)

    return db_article[-1]


  def delete(self, id_article):
    try:
      index_article = self.__findById(id_article)
      db_article.pop(index_article)
    except Exception as e:
      raise e


  def update(self, article, update_article_dto):
    try:
      return self.__updateValues(article, update_article_dto)
    except Exception as e:
      raise e


  def __updateValues(self, article, update_article_dto):
    if('title' in update_article_dto):
      article['title'] = update_article_dto['title']

    if('content' in update_article_dto):
      article['content'] = update_article_dto['content']

    article['updatedAt'] = datetime.now()

    return article
      

  def __findById(self, id_article):
    index_article = next((i for i, article in enumerate(db_article) if article['id'] == id_article), None)
    
    if index_article is None:
      raise Exception('Not found!')
    
    return index_article


article_repository = ArticleRepository()
