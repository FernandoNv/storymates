from datetime import date
import src.service.article_service as article_service
import src.repository.comment_repository as comment_repository

def to_dto(comment):
  updatedAt = None
  
  if(comment['updatedAt'] is not None):
    updatedAt = comment['updatedAt'].strftime("%c")
    
  return {
    'id': comment['id'],
    'content': comment['content'],
    'author': comment['author'],
    'idArticle': comment['idArticle'],
    'createdAt': comment['createdAt'].strftime("%c"),
    'updatedAt': updatedAt,
  }

def get_by_id(id_comment):
  return comment_repository.get_by_id(id_comment)

def get_all_by_id_article(id_article):
  comments = comment_repository.get_all_by_id_article(id_article)
  return comments

def create(author, new_comment_dto):
  if 'idArticle' not in new_comment_dto:
    raise Exception('Article invalid!')

  idArticle = new_comment_dto['idArticle']
  article = article_service.get_by_id(idArticle)

  if article is None: 
    raise Exception('Article Not found!')

  new_comment_dto = {
    'title': new_comment_dto['title'],
    'content': new_comment_dto['content'],
    'author': author,
    'idArticle': idArticle,
  }
  article = comment_repository.save(new_comment_dto)

  return to_dto(article)


def update(author, id_comment, update_comment_dto):
  if 'idArticle' not in update_comment_dto:
    raise Exception('Article invalid!')

  idArticle = update_comment_dto['idArticle']
  article = article_service.get_by_id(idArticle)

  if article is None: 
    raise Exception('Article Not found!')
  
  if article['id'] != update_comment_dto['idArticle']:
    raise Exception('Article invalid!')

  comment = comment_repository.get_by_id(id_comment)

  if comment is None:
    raise Exception('Comment invalid!')
  
  if comment['id'] != id_comment:
    raise Exception('Comment not Found!')
  
  update_comment_dto = {
    'id': update_comment_dto['id'],
    'title': update_comment_dto['title'],
    'content': update_comment_dto['content'],
    'author': author,
    'idArticle': idArticle,
  }
  article = comment_repository.update(update_comment_dto)

  return to_dto(article)


def delete(author, id_comment, delete_comment_dto):
  if 'idArticle' not in delete_comment_dto:
    raise Exception('Article invalid!')

  idArticle = delete_comment_dto['idArticle']
  article = article_service.get_by_id(idArticle)

  if article is None: 
    raise Exception('Article Not found!')
  
  if article['id'] != delete_comment_dto['idArticle']:
    raise Exception('Article invalid!')

  comment = comment_repository.get_by_id(id_comment)

  if comment is None:
    raise Exception('Comment invalid!')
  
  if comment['id'] != id_comment:
    raise Exception('Comment not Found!')

  if author == comment['author'] or author == article['author']:
    comment_repository.delete_by_id(id_comment)
    return

  raise Exception('Author invalid!')