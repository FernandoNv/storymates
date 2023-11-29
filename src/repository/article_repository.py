from datetime import datetime
from flask import Flask, request
from src.repository.db import db_article
from flask_mysqldb import MySQL
from src.server.instance import server

app, api = server.app, server.api
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'storymates'
 
mysql = MySQL(app)

def get_all():
  cursor = mysql.connection.cursor()
  cursor.execute('SELECT * FROM article ORDER BY createdAt DESC LIMIT 100')
  #https://stackoverflow.com/questions/5010042/mysql-get-column-name-or-alias-from-query
  fields = [field_md[0] for field_md in cursor.description]
  result = [dict(zip(fields,row)) for row in cursor.fetchall()]  
  cursor.close()

  return result


def get_all_by_author(username):
  return list(filter(lambda item: item["author"] == username, db_article))


def get_by_id(id_article):
  try:
    index_article = __findById(id_article)
    
    return db_article[index_article]
  except Exception as e:
    raise e


def save(new_article_dto):
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


def delete(id_article):
  try:
    index_article = __findById(id_article)
    db_article.pop(index_article)
  except Exception as e:
    raise e


def update(article, update_article_dto):
  try:
    return __updateValues(article, update_article_dto)
  except Exception as e:
    raise e


def __updateValues(article, update_article_dto):
  if('title' in update_article_dto):
    article['title'] = update_article_dto['title']

  if('content' in update_article_dto):
    article['content'] = update_article_dto['content']

  article['updatedAt'] = datetime.now()

  return article
    

def __findById(id_article):
  index_article = next((i for i, article in enumerate(db_article) if article['id'] == id_article), None)
  
  if index_article is None:
    raise Exception('Not found!')
  
  return index_article