# from flask_app import app
# from flask_app.controllers import transactions_controller, users_controller

# if __name__ == '__main__':
#   app.run(debug = True)

from flask_app import app
from flask_app.controllers import users_controller, transactions_controller

if __name__ == '__main__':
  app.run(debug = True)