from src.repository.config import mysql
from src.repository.util import format_row_to_dict


def create(new_comment_dto):
  query = """
  INSERT INTO comment(content, author, idArticle) 
  VALUES('{content}', '{author}', '{idArticle}')
  """

  cursor = mysql.connection.cursor()
  cursor.execute(
    query.format(
      content=new_comment_dto['content'], 
      author=new_comment_dto['author'],
      idArticle=new_comment_dto['idArticle']
    )
  )
  
  mysql.connection.commit()
  
  cursor.execute('SELECT LAST_INSERT_ID()')
  id_created = cursor.fetchone()[0]
  cursor.close()

  return get_by_id(id_created)


def update(update_comment_dto):
  query = """
  UPDATE comment 
  SET content = '{content}'
  WHERE id = {id}
  """

  cursor = mysql.connection.cursor()
  cursor.execute(
    query.format(
      content=update_comment_dto['content'], 
      id=update_comment_dto["id"]
    )
  )
  
  mysql.connection.commit()
  cursor.close()

  return get_by_id(update_comment_dto["id"])


def get_by_id(id_comment):
  query_comment = """
    SELECT * FROM comment 
    WHERE id='{id_comment}'
  """
  cursor = mysql.connection.cursor()
  cursor.execute(query_comment.format(id_comment=id_comment))

  comment = format_row_to_dict(cursor)

  if comment is None:
    raise Exception("Id invalid!")

  comment = comment[0]
  cursor.close()

  return comment


def delete_by_id(id_comment):
  query = """
    DELETE FROM comment WHERE id = {id_comment};
  """
  cursor = mysql.connection.cursor()
  cursor.execute(query.format(id_comment=id_comment))

  mysql.connection.commit()
  cursor.close()


def get_all_by_id_article(id_article):
  query = """
    SELECT * FROM comment 
    WHERE idArticle='{id_article}' 
    ORDER BY createdAt 
    LIMIT 100
  """

  cursor = mysql.connection.cursor()
  cursor.execute(query.format(id_article=id_article))
  
  result = format_row_to_dict(cursor)
  cursor.close()
  
  return result