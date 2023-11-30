from flask import Flask, request
from flask_mysqldb import MySQL
from src.server.instance import server

app, api = server.app, server.api
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'storymates'
 
mysql = MySQL(app)