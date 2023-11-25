from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.service.article_service import article_service

app, api = server.app, server.api


@api.route('/articles')
class ArticleListController(Resource):
  def get(self):
    response = article_service.get_all()
    return response, 200


@api.route('/articles/<int:id_article>')
class ArticleController(Resource):
  def get(self, id_article):
    try:
      response = article_service.get_by_id(id_article)
      
      return response, 200
    except Exception as e:
      status_code = 400
      
      if(str(e) == 'Not found!'):
          status_code = 404

      response = { 'message': str(e) }
      return response, status_code


@api.route('/authors/<string:author>/articles')
class AuthorArticleController(Resource):
  def get(self, author):
    try:
      response = article_service.get_all_by_author(author)
      return response, 200
    except Exception as e:
      response = { 'message': str(e) }
      return response, 400


  def put(self, author, id_article):
    update_article_dto = api.payload
    try:
      response = article_service.update(author, id_article, update_article_dto)

      return response, 200
    except Exception as e:
      status_code = 400
      
      if(str(e) == 'Not found!'):
          status_code = 404

      response = { 'message': str(e) }
      return response, status_code


  def post(self, author):
    new_article_dto = api.payload
    response = article_service.create(author, new_article_dto)

    return response, 201


  def delete(self, author, id_article):
    try:
      article_service.delete(author, id_article)

      return None, 204
    except Exception as e:
      status_code = 400

      if(str(e) == 'Not found!'):
          status_code = 404
      response = { 'message': str(e) }

      return response, status_code

api.add_resource(AuthorArticleController, '/authors/<string:author>/articles/<int:id_article>')
