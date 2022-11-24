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
  print(trans)
  print(rem_budget)
  if not trans:
    trans = 0
  if not rem_budget: 
    rem_budget = 0
  print(trans)
  print(rem_budget)
  if rem_budget != 0 and trans != 0: 
    total_Budget = rem_budget['budget_amt'] - trans[0]['amount']
  if rem_budget != 0 and trans == 0:
    total_Budget = rem_budget['budget_amt'] - trans
  if rem_budget == 0 and trans != 0:
    total_Budget = rem_budget - trans[0]['amount']
  if rem_budget == 0 and trans == 0:
    total_Budget = rem_budget - trans
  
  
    #data for the various budgets the user creates
  table_data = {
    'transportation_budget': Budget.get_budget_by_Transportation(data),
    'groceries_budget': Budget.get_budget_by_Groceries(data),
    'clothing_budget': Budget.get_budget_by_Clothing(data),
    'doctor_budget': Budget.get_budget_by_Doctor(data),
    'cosmetics_budget': Budget.get_budget_by_Cosmetics(data),
    'housing_budget': Budget.get_budget_by_Housing(data),
    'internet_budget': Budget.get_budget_by_Internet(data),
    'phone_budget': Budget.get_budget_by_Phone(data),
    'subscriptions_budget': Budget.get_budget_by_Subscriptions(data),
    'miscellaneous_budget': Budget.get_budget_by_Miscellaneous(data),
  }
  
  
  # Spent data for user spending inputs
  spent_data = {
    'transportation_spent' : Transaction.get_spent_by_transportaion(data),
    'groceries_spent' : Transaction.get_spent_by_groceries(data),
    'clothing_spent' : Transaction.get_spent_by_clothing(data),
    'doctor_spent' : Transaction.get_spent_by_doctor(data),
    'cosmetics_spent' : Transaction.get_spent_by_cosmetics(data),
    'housing_spent' : Transaction.get_spent_by_housing(data),
    'internet_spent' : Transaction.get_spent_by_internet(data),
    'phone_spent' : Transaction.get_spent_by_phone(data),
    'subscriptions_spent' : Transaction.get_spent_by_subscriptions(data),
    'miscellaneous_spent': Transaction.get_spent_by_miscellaneous(data)
  }
  
  return render_template('dashboard.html', user = user, transactions = transactions, budget = budget, total_Budget = total_Budget, table_data = table_data, spent_data = spent_data)




#insert transaction data into database
@app.route('/insert_transaction', methods = ['POST'])
def insert_transaction():
  if 'uid' not in session:
    return redirect('/')
  
  if not Transaction.validate_transactions(request.form):
    return redirect(request.referrer)
  
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