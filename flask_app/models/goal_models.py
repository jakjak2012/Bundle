from flask_app.config.mysqlconnection import connectToMySQL

class Goal:
  def __init__(self, data):
    self.id = data['id']
    self.goal_amt = data['goal_amt']
    self.goal_cat = data['goal_cat']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']