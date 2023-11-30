from datetime import datetime
from src.repository.config import mysql
from src.repository.util import format_row_to_dict

def get_all():
  query = """
    SELECT * FROM article 
    ORDER BY createdAt DESC 
    LIMIT 100
  """
  
  cursor = mysql.connection.cursor()
  cursor.execute(query)

  result = format_row_to_dict(cursor)
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
  
  result = format_row_to_dict(cursor)
  cursor.close()
  
  return result


def get_by_id(id_article):
  query_article = """
    SELECT * FROM article 
    WHERE id='{id_article}'
  """
  cursor = mysql.connection.cursor()
  cursor.execute(query_article.format(id_article=id_article))

  article = format_row_to_dict(cursor)

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
  query = """
    DELETE FROM article WHERE id = {id_article};
  """
  cursor = mysql.connection.cursor()
  cursor.execute(query.format(id_article=id_article))

  mysql.connection.commit()
  cursor.close()


def update(article, update_article_dto):
  query = """
  UPDATE article 
  SET title = '{title}', content = '{content}'
  WHERE id = {id}
  """

  cursor = mysql.connection.cursor()
  cursor.execute(
    query.format(
      title=update_article_dto['title'], 
      content=update_article_dto['content'], 
      id=article["id"]
    )
  )
  
  mysql.connection.commit()
  cursor.close()

  return get_by_id(article["id"])
