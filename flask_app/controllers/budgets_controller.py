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
  return render_template('input.html')

#allows users to add budgets to the database
@app.route('/insert_budget', methods = ['POST'])
def insert_budget():
  if 'uid' not in session:
    return redirect('/')
  
  data = {
    **request.form,
    'user_id': session['uid']
  }
  Budget.insert_budget(data)
  return redirect('/input')

