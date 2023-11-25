from flask import Flask
from flask_restx import Api

class Server():
  def __init__(self):
    self.app = Flask(__name__)
    self.api = Api(
      self.app,
      version=1.0,
      title="Storymate",
      description="A simple articles API",
      doc="/docs"
    )
    

  def run(self):
    print("APLICATION CREATED...")
    self.app.run(debug=True)


server = Server()