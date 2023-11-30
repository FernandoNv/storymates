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
  query = """
    SELECT * FROM article 
    ORDER BY createdAt DESC 
    LIMIT 100
  """
  
  cursor = mysql.connection.cursor()
  cursor.execute(query)

  result = __format_row_to_dict(cursor)
  cursor.close()

  return result


def get_all_by_author(author):
  query = """
    SELECT * FROM article 
    WHERE author='{author}' 
    ORDER BY createdAt DESC 
    LIMIT 100
  """

  cursor = mysql.connection.cursor()
  cursor.execute(query.format(author=author))
  
  result = __format_row_to_dict(cursor)
  cursor.close()
  
  return result


def get_by_id(id_article):
  query_article = """
    SELECT * FROM article 
    WHERE id='{id_article}'
  """
  cursor = mysql.connection.cursor()
  cursor.execute(query_article.format(id_article=id_article))

  article = __format_row_to_dict(cursor)

  if article is None:
    raise Exception("Id invalid!")

  article = article[0]

  cursor.close()

  return article


def save(new_article_dto):
  query = """
  INSERT INTO article(id, title, content, author) 
  VALUES(null, '{title}', '{content}', '{author}')
  """

  cursor = mysql.connection.cursor()
  cursor.execute(
    query.format(
      title=new_article_dto['title'], 
      content=new_article_dto['content'], 
      author=new_article_dto['author']
    )
  )
  
  mysql.connection.commit()
  
  cursor.execute('SELECT LAST_INSERT_ID()')
  id_created = cursor.fetchone()[0]
  cursor.close()

  return get_by_id(id_created)


def delete(id_article):
  try:
    index_article = __find_by_id(id_article)
    db_article.pop(index_article)
  except Exception as e:
    raise e


def update(article, update_article_dto):
  query = """
  UPDATE article 
  SET title = '{title}', content = '{content}', author = '{author}'
  WHERE id = {id}
  """

  cursor = mysql.connection.cursor()
  cursor.execute(
    query.format(
      title=update_article_dto['title'], 
      content=update_article_dto['content'], 
      author=update_article_dto['author'],
      id=article["id"]
    )
  )
  
  mysql.connection.commit()
  cursor.close()

  return get_by_id(article["id"])


def __update_values(article, update_article_dto):
  if('title' in update_article_dto):
    article['title'] = update_article_dto['title']

  if('content' in update_article_dto):
    article['content'] = update_article_dto['content']

    

  return article
    

def __find_by_id(id_article):
  index_article = next((i for i, article in enumerate(db_article) if article['id'] == id_article), None)
  
  if index_article is None:
    raise Exception('Not found!')
  
  return index_article


#https://stackoverflow.com/questions/5010042/mysql-get-column-name-or-alias-from-query
def __format_row_to_dict(cursor):
  fields = [field_md[0] for field_md in cursor.description]
  result = [dict(zip(fields,row)) for row in cursor.fetchall()]

  return result
