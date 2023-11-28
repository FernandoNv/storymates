from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.service.comment_service import comment_service

app, api = server.app, server.api

@api.route('/authors/<string:author>/comments')
class ArticleCommentController(Resource):
  def post(self, author):
    new_comment_dto = api.payload
    response = comment_service.create(author, new_comment_dto)

    return response, 201

  def put(self, author, id_comment):
    update_comment_dto = api.payload
    try:
      response = comment_service.update(author, id_comment, update_comment_dto)

      return response, 200
    except Exception as e:
      status_code = 400
      
      if(str(e) == 'Article Not found!' or str(e) == 'Comment Not found!') or (str(e) == 'Article invalid!') or (str(e) == 'Comment invalid!'):
          status_code = 404

      response = { 'message': str(e) }
      return response, status_code


  def delete(self, author, id_comment):
    try:
      delete_comment_dto = api.payload
      comment_service.delete(author, id_comment, delete_comment_dto)
      return None, 204
    except Exception as e:
      status_code = 400

      if(str(e) == 'Article Not found!' or str(e) == 'Comment Not found!') or (str(e) == 'Article invalid!') or (str(e) == 'Comment invalid!'):
          status_code = 404
      response = { 'message': str(e) }

      return response, status_code


api.add_resource(ArticleCommentController, '/authors/<string:author>/comments/<int:id_comment>')
