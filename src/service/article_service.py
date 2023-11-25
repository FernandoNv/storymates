from datetime import date

from src.repository.article_repository import article_repository
from src.service.comment_service import comment_service


class ArticleService():
  def get_all(self):
    articles = article_repository.get_all()
    articles = list(map(lambda article: self.to_dto(article), articles))

    return articles


  def get_all_by_author(self, username):
    articles = article_repository.get_all_by_author(username)
    articles = list(map(lambda article: self.to_dto(article), articles)) 

    return articles


  def create(self, author, new_article_dto):
    new_article_dto = {
      'title': new_article_dto['title'],
      'content': new_article_dto['content'],
      'author': author
    }
    article = article_repository.save(new_article_dto)

    return self.to_dto(article)


  def delete(self, author, id_article):
    # if(author is None):
    #   raise Exception('Empty author')
    try:
      article = article_repository.get_by_id(id_article)

      if(article["author"] != author):
        raise Exception('Invalid author')

      article = article_repository.delete(id_article)
    except Exception as e:
      raise e


  def get_by_id(self, id_article):
    try:
      article = article_repository.get_by_id(id_article)
      article = self.to_dto_with_comments(article)

      return article
    except Exception as e:
      raise e


  def update(self, author, id_article, update_article_dto):
    # if(author is None):
    #   raise Exception('Empty author')

    try:
      article = article_repository.get_by_id(id_article)

      if(article["author"] != author):
        raise Exception('Invalid author')

      article = article_repository.update(article, update_article_dto)
      
      return self.to_dto(article)
    except Exception as e:
      raise e


  def to_dto(self, article):
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

  def to_dto_with_comments(self, article):
    updatedAt = None
    if(article['updatedAt'] is not None):
      updatedAt = article['updatedAt'].strftime("%c")
      
    return {
      'id': article['id'],
      'title': article['title'],
      'content': article['content'],
      'author': article['author'],
      'createdAt': article['createdAt'].strftime("%c"),
      'updatedAt': updatedAt,
      'comments': list(map(lambda comment: comment_service.to_dto(comment), article['comments']))
    }


article_service = ArticleService()