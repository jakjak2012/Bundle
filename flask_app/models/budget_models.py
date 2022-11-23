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
  def display_budget(cls, data):
    query = 'SELECT budget_amt FROM budget WHERE user_id = %(id)s'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]
  
  
  
#  Selecting budget based on user_id
# got this code to work for deducting the budget, feel free to make changes if needed
  @classmethod
  def grab_budget_amount(cls,data):
    query = "SELECT budget_amt FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s;"
    results = connectToMySQL('Bundle').query_db(query,data)
    if len(results) < 1:
      return False
    return results[0]
  
  
  
  
  # Inserting Budget from the user Input
  @classmethod
  def insert_budget(cls,data):
    query = 'INSERT INTO budget(budget_amt, budget_cat, created_at, updated_at, user_id) VALUES (%(budget_amt)s, %(budget_cat)s, %(created_at)s, %(updated_at)s, %(user_id)s)'
    results = connectToMySQL('Bundle').query_db(query, data)
    return results

#getting budgets by the specific categories 
  @classmethod
  def get_budget_by_Transportation(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "transportation";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Groceries(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "groceries";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Clothing(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "clothing";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Doctor(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "doctor";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Cosmetics(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "cosmetics";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Housing(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "housing";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Internet(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "internet";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Phone(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "phone";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Subscriptions(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "subscriptions";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def get_budget_by_Miscellaneous(cls, data):
    query = 'SELECT budget_amt, budget_cat FROM budget JOIN users on users.id = user_id WHERE users.id = %(id)s AND budget_cat = "miscellaneous";'
    results = connectToMySQL('Bundle').query_db(query, data)
    if len(results) < 1:
      return False
    return results[0]

