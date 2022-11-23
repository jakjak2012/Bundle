from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.transaction_models import Transaction
from flask_app.models.user_models import User
from flask_app.models.budget_models import Budget

#dashboard page, access once user is logged in
@app.route('/dashboard')
def dashboard():
  if 'uid' not in session:
    return redirect('/')
  
  data = {
    'id': session['uid']
  }
  user = User.get_one_by_id(data)
  transactions = Transaction.get_transaction(data)
  budget = Budget.display_budget(data)
  
  #  For Testing purposes(can be moved elsewhere)
  # code for deducting amount from transactions 
  trans = Transaction.deduct_total(data)
  rem_budget = Budget.grab_budget_amount(data)
  total_Budget = rem_budget['budget_amt'] - trans[0]['amount']
  
  # an if statement if needed for displaying messages to the user??
  
  return render_template('dashboard.html', user = user, transactions = transactions, budget = budget, total_Budget = total_Budget)




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



# used to check if the user selected a category to sort by
@app.route('/sort_by_category', methods = ['POST'])
def sort_by_category():
  if 'uid' not in session:
    return redirect('/')
  
  session['category'] = request.form['category']
  if session['category'] == '':
    return redirect(request.referrer)
  return redirect('/sortted')




# displays sorted data by selected category
@app.route('/sortted')
def sortted():
  if 'uid' not in session:
    return redirect('/')
  
  user_id = {
    'id': session['uid']
  }

  data = {
    'id': session['uid'],
    'category': session['category']
  }
  user = User.get_one_by_id(user_id)
  transactions = Transaction.get_category(data)
  sort_by = session['category']
  session.pop('category')
  return render_template('', user = user, transactions = transactions, sort_by = sort_by)