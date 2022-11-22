from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_models import User

class Transaction:
  def __init__(self, data):
    self.id = data['id']
    self.amount = data['amount']
    self.category = data['category']
    self.comment = data['comment']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']