from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_models import User

class Budget:
  def __init__(self, data):
    self.id = data['id']
    self.budget_amt = data['budget_amt']
    self.budget_cat = data['budget_cat']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']