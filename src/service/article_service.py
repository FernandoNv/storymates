from datetime import date
import src.repository.article_repository as article_repository
import src.service.comment_service as comment_service

def get_all():
  articles = article_repository.get_all()
  articles = list(map(lambda article: to_dto(article), articles))

  return articles


def get_all_by_author(username):
  articles = article_repository.get_all_by_author(username)
  articles = list(map(lambda article: to_dto(article), articles)) 

  return articles


def create(author, new_article_dto):
  new_article_dto = {
    'title': new_article_dto['title'],
    'content': new_article_dto['content'],
    'author': author
  }
  article = article_repository.save(new_article_dto)

  return to_dto(article)


def delete(author, id_article):
  try:
    article = article_repository.get_by_id(id_article)

    if(article["author"] != author):
      raise Exception('Invalid author')

    article = article_repository.delete(id_article)
  except Exception as e:
    raise e


def get_by_id(id_article):
  try:
    article = article_repository.get_by_id(id_article)
    article = to_dto_with_comments(article)

    return article
  except Exception as e:
    raise e


def update(author, id_article, update_article_dto):
  try:
    article = article_repository.get_by_id(id_article)

    if(article["author"] != author):
      raise Exception('Invalid author')

    article = article_repository.update(article, update_article_dto)
    
    return to_dto(article)
  except Exception as e:
    raise e


def to_dto(article):
  updatedAt = None
  if(article['updatedAt'] is not None):
    updatedAt = article['updatedAt'].strftime("%c")
    
  return {
    'id': article['id'],
    'title': article['title'],
    'content': article['content'],
    'author': article['author'],
    'createdAt': article['createdAt'].strftime("%c"),
    'updatedAt': updatedAt
  }

def to_dto_with_comments(article):
  updatedAt = None
  if(article['updatedAt'] is not None):
    updatedAt = article['updatedAt'].strftime("%c")

  comments = comment_service.get_all_by_id_article(article['id'])
    
  return {
    'id': article['id'],
    'title': article['title'],
    'content': article['content'],
    'author': article['author'],
    'createdAt': article['createdAt'].strftime("%c"),
    'updatedAt': updatedAt,
    'comments': list(map(lambda comment: comment_service.to_dto(comment), comments))
  }