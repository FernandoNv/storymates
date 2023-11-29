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
  pass


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
  pass


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
