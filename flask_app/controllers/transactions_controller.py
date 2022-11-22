from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.transaction_models import Transaction
from flask_app.models.user_models import User

#dashboard page, access once user is logged in
@app.route('/dashboard')
def dashboard():
  if 'uid' not in session:
    return render_template('/')
  
  data = {
    'id': session['uid']
  }
  user = User.get_one_by_id(data)
  transactions = Transaction.get_transaction(data)
  return render_template('dashboard.html', user = user, transactions = transactions)

#insert transaction data into database
@app.route('/insert_transaction', methods = ['POST'])
def insert_transaction():
  if 'uid' not in session:
    return redirect('/')
  
  data = {
    **request.form,
    'user_id': session['uid']
  }
  Transaction.insert_transaction(data)
  return redirect('/dashboard')

#used to delete a transaction from the database
@app.route('/delete_transaction/<int:num>')
def delete_transaction(num):
  if 'uid' not in session:
    return redirect('/')
  
  data = {
    'id': num
  }
  Transaction.delete_transaction(data)
  return redirect('/dashboard')
