from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_models import User

class Transaction:
  def __init__(self, data):
    self.id = data['id']
    self.amount = data['amount']
    self.category = data['category']
    self.comment = data['comment']
    self.date = data['date']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']
    

    
    # Fetching all transactions from DB
    @classmethod
    def get_transaction(cls, data):
      query = "SELECT * FROM transactions JOIN users on users.id = user_id WHERE users.id = %(id)s;"
      results = connectToMySQL('Bundle').query_db(query,data)
      transactions = []
      for dict in results:
        transaction = cls(dict)
        user_data = {
          **dict,
          'id' : dict['users.id'],
          'created_at' : dict['users.created_at'],
          'updated_at' : dict['users.updated_at']
        }
        users = User(user_data)
        transaction.user = users
        transactions.append(transaction)
      return transactions
        
        
    # Insert transactions to DB
    @classmethod
    def insert_transaction(cls, data):
      query = "INSERT INTO transactions(amount, category, comment, date, created_at, updated_at, user_id) VALUES (%(amount)s, %(category)s, %(comment)s, %(date)s, NOW(), NOW(), %(user_id)s);"
      results = connectToMySQL('Bundle').query_db(query, data)
      return results
    
    
    
    # Deleting Specific transactions from the DB
    @classmethod
    def delete_transaction(cls, data):
      query = "DELETE FROM transactions WHERE id = %(id)s"
      results = connectToMySQL('Bundle').query_db(query, data)
      return results
    
    
    
    # Collecting the total amount from date range
    @classmethod
    def total_transactions(cls, data):
      query = "SELECT sum(amount) as amount, date FROM transactions where user_id = %(id)s and date BETWEEN %(date)s AND %(date)s"
      results = connectToMySQL('Bundle').query_db(query, data)
      totals = []
      for dict in results:
        total = cls(dict)
        total_data = {
          **dict,
          'id' : ['users.id'],
          'created_at' : ['users.created_at'],
          'updated_at' : ['users.updated_at']
        }
        users = User(total_data)
        total.user = users
        totals.append(total)
      return totals
      
      
      
    # Selecting information based on category
    @classmethod
    def get_category(cls, data):
      query = "SELECT * FROM transactions JOIN users on users.id = user_id WHERE users.id = %(id)s AND category = %(category)s;"
      results = connectToMySQL('Bundle').query_db(query,data)
      categories = []
      for dict in results:
        category = cls(dict)
        total_category = {
          **dict,
          'id' : dict['users.id'],
          'created_at' : ['users.created_at'],
          'updated_at' : ['users.updated_at']
        }
        users = User(total_category)
        category.user = users
        categories.append(category)
      return categories
