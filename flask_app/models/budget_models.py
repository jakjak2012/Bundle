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
    
    
    
    
      # displaying budget on the page
  @classmethod
  def display_budget(cls):
    query = 'SELECT budget_amt FROM budget WHERE user_id = %(id)s'
    results = connectToMySQL('Bundle').query_db(query)
    return results
  
  
  # Inserting Budget from the user Input
  @classmethod
  def insert_budget(cls,data):
    query = 'INSERT INTO budget(budget_amt, budget_cat, created_at, updated_at, user_id) VALUES (%(budget_amt)s, %(budget_cat)s, %(created_at)s, %(updated_at)s, %(user_id)s)'
    results = connectToMySQL('Bundle').query_db(query, data)
    return results