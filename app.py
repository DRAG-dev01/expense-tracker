from database import init_db, view_expenses, add_expense, guess_description, generate_pie_chart, delete_expense
from flask import Flask, render_template, request, redirect, url_for

init_db()

app = Flask(__name__)


@app.route("/")
def view():
    generate_pie_chart()
    data = view_expenses()
    print(data)
    return render_template("index.html", expenses=data)


@app.route("/add", methods=["POST"])
def add():
    date = request.form["date"]
    amount = int(request.form["amount"])
    description = request.form["description"]
    category = request.form["category"]
    if not category:
        category = guess_description(description)
    add_expense(date, amount, description, category)
    return redirect(url_for("view"))

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete(expense_id):
    delete_expense(expense_id)
    return redirect(url_for('view'))

    
app.run()
