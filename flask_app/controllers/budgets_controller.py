from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.transaction_models import Transaction
from flask_app.models.budget_models import Budget
from flask_app.models.user_models import User

#renders the input page for users to add budgets or transactions
@app.route('/input')
def input_page():
  if 'uid' not in session:
    return redirect('/')
  data = {
    'id': session['uid']
  }
  user = User.get_one_by_id(data)
  return render_template('input.html', user = user)

#allows users to add budgets to the database
@app.route('/insert_budget', methods = ['POST'])
def insert_budget():
  if 'uid' not in session:
    return redirect('/')
  
  data = {
  **request.form,
  'user_id': session['uid']
  }

  if not Budget.validate_budget(data):
    return redirect(request.referrer)

  Budget.insert_budget(data)
  return redirect('/input')

# updates the budgets table
@app.route('/update')
def update():
  if 'uid'not in session:
    return redirect('/')
  data = {
    'id': session['uid']
  }
  user = User.get_one_by_id(data)
  return render_template('update.html', user = user)
