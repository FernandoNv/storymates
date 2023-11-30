from src.repository.config import mysql
from src.repository.util import format_row_to_dict

  #@param: new_comment_dto: {
  #   'title': string,
  #    'content': string,
  #    'author': string,
  #    'idArticle': int,
  # } 
  # return: {
  #   'id': int,
  #   'title': string,
  #   'content': string,
  #   'author': string,
  #   'idArticle': int,
  #   'createdAt': Date,
  #   'updatedAt': Date  
  # }
def create(self, new_comment_dto):
  query = """
  INSERT INTO comment( title, content, author) 
  VALUES('{title}', '{content}', '{author}', '{articleId}')
  """

  cursor = mysql.connection.cursor()
  cursor.execute(
    query.format(
      title=new_comment_dto['title'], 
      content=new_comment_dto['content'], 
      author=new_comment_dto['author'],
      articleId=new_comment_dto['articleId']
    )
  )
  
  mysql.connection.commit()
  
  cursor.execute('SELECT LAST_INSERT_ID()')
  id_created = cursor.fetchone()[0]
  cursor.close()

  return get_by_id(id_created)


#@param: update_comment_dto: {
#   'title': string,
#    'content': string,
#    'author': string,
#    'idArticle': int,
# } 
# return: {
#   'id': int,
#   'title': string,
#   'content': string,
#   'author': string,
#   'idArticle': int,
#   'createdAt': Date,
#   'updatedAt': Date  
# }
def update(self, update_comment_dto):
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


#@param: id: int
# return: {
#   'id': int,
#   'title': string,
#   'content': string,
#   'author': string,
#   'idArticle': int,
#   'createdAt': Date,
#   'updatedAt': Date  
# }
def get_by_id(self, id_comment):
  pass


#@param: id: int
def delete_by_id(self, id_comment):
  pass


def get_all_by_id_article(id_article):
  return []
