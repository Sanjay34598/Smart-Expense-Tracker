from app import app, db, Expense, Salary
from datetime import datetime, timedelta

def seed_data():
    with app.app_context():
        # Clear existing data to avoid duplicates if needed
        # db.drop_all()
        # db.create_all()

        now = datetime.now()
        current_month = now.month
        current_year = now.year

        # Previous month
        prev_date = now.replace(day=1) - timedelta(days=1)
        prev_month = prev_date.month
        prev_year = prev_date.year

        # Add Salaries
        salaries = [
            Salary(amount=50000.0, month=current_month, year=current_year),
            Salary(amount=50000.0, month=prev_month, year=prev_year)
        ]

        # Add Expenses for Current Month
        current_expenses = [
            Expense(title="Groceries", amount=2500.0, category="Food", date=now.replace(day=5)),
            Expense(title="Internet Bill", amount=1200.0, category="Bills", date=now.replace(day=2)),
            Expense(title="Netflix Subscription", amount=499.0, category="Entertainment", date=now.replace(day=10)),
            Expense(title="Gym Membership", amount=2000.0, category="Health", date=now.replace(day=1))
        ]

        # Add Expenses for Previous Month
        prev_expenses = [
            Expense(title="Rent", amount=15000.0, category="Housing", date=prev_date.replace(day=1)),
            Expense(title="Electricity Bill", amount=3500.0, category="Bills", date=prev_date.replace(day=5)),
            Expense(title="Dining Out", amount=4000.0, category="Food", date=prev_date.replace(day=15))
        ]

        # Add to session
        for s in salaries:
            db.session.add(s)
        for e in current_expenses + prev_expenses:
            db.session.add(e)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
