from datetime import date

class CommentService():
  def to_dto(self, comment):
    updatedAt = None
    
    if(comment['updatedAt'] is not None):
      updatedAt = comment['updatedAt'].strftime("%c")
      
    return {
      'id': comment['id'],
      'content': comment['content'],
      'author': comment['author'],
      'createdAt': comment['createdAt'].strftime("%c"),
      'updatedAt': updatedAt,
    }

  def get_by_id(self, id_comment):
    pass

  def create(self, id_article, new_comment_dto):
    pass


  def update(self, id_article, id_comment):
    pass


  def delete(self, id_article, id_comment):
    pass
  

comment_service = CommentService()