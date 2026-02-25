from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        date = datetime.strptime(request.form["date"], "%Y-%m-%d")

        new_expense = Expense(title=title, amount=amount, category=category, date=date)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for("index"))

    filter_category = request.args.get("category")
    filter_date = request.args.get("date")

    query = Expense.query

    if filter_category:
        query = query.filter_by(category=filter_category)
    if filter_date:
        query = query.filter_by(date=datetime.strptime(filter_date, "%Y-%m-%d"))

    expenses = query.all()

    # Get Current Month and Year
    now = datetime.now()
    current_month = now.month
    current_year = now.year

    # Get Salary for Current Month
    salary_record = Salary.query.filter_by(month=current_month, year=current_year).first()
    monthly_salary = salary_record.amount if salary_record else 0.0

    # Total Spending (All time)
    total_spending = db.session.query(func.sum(Expense.amount)).scalar() or 0

    # Current Month Spending
    monthly_spending = db.session.query(func.sum(Expense.amount)).filter(
        func.extract('month', Expense.date) == current_month,
        func.extract('year', Expense.date) == current_year
    ).scalar() or 0

    savings = monthly_salary - monthly_spending

    category_data = db.session.query(
        Expense.category,
        func.sum(Expense.amount)
    ).group_by(Expense.category).all()

    return render_template(
        "index.html",
        expenses=expenses,
        total_spending=total_spending,
        monthly_salary=monthly_salary,
        monthly_spending=monthly_spending,
        savings=savings,
        category_data=category_data
    )

@app.route("/set_salary", methods=["POST"])
def set_salary():
    amount = float(request.form["salary"])
    now = datetime.now()
    current_month = now.month
    current_year = now.year

    salary_record = Salary.query.filter_by(month=current_month, year=current_year).first()
    if salary_record:
        salary_record.amount = amount
    else:
        salary_record = Salary(amount=amount, month=current_month, year=current_year)
        db.session.add(salary_record)
    
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)