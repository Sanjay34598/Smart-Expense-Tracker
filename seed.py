from app import app, db, Expense, Salary
from datetime import datetime, timedelta

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        now = datetime.now()
        
        # Helper to get specific months
        def get_month_date(months_back):
            target_date = now.replace(day=1)
            for _ in range(months_back):
                target_date = (target_date - timedelta(days=1)).replace(day=1)
            return target_date

        categories = ["Food", "Housing", "Bills", "Entertainment", "Health", "Shopping", "Travel", "Misc"]
        
        for i in range(3): # Current month and 2 months back
            month_start = get_month_date(i)
            month = month_start.month
            year = month_start.year
            
            # Add Salary
            salary = Salary(amount=60000.0, month=month, year=year)
            db.session.add(salary)
            
            # Add diverse expenses
            expenses = [
                Expense(title="Rent", amount=15000.0, category="Housing", date=month_start.replace(day=1)),
                Expense(title="Electricity Bill", amount=2500.0, category="Bills", date=month_start.replace(day=5)),
                Expense(title="Water Bill", amount=500.0, category="Bills", date=month_start.replace(day=5)),
                Expense(title="Internet", amount=1000.0, category="Bills", date=month_start.replace(day=2)),
                Expense(title="Groceries", amount=4000.0, category="Food", date=month_start.replace(day=7)),
                Expense(title="Dining Out", amount=2000.0, category="Food", date=month_start.replace(day=15)),
                Expense(title="Cinema", amount=800.0, category="Entertainment", date=month_start.replace(day=12)),
                Expense(title="Gym", amount=1500.0, category="Health", date=month_start.replace(day=1)),
                Expense(title="Amazon Shopping", amount=3500.0, category="Shopping", date=month_start.replace(day=20)),
                Expense(title="Petrol/Fuel", amount=3000.0, category="Travel", date=month_start.replace(day=10)),
                Expense(title="Pharmacy", amount=400.0, category="Health", date=month_start.replace(day=18)),
                Expense(title="Netflix", amount=499.0, category="Entertainment", date=month_start.replace(day=10)),
            ]
            
            for e in expenses:
                db.session.add(e)

        db.session.commit()
        print("Database seeded with 3 months of diverse data successfully!")

if __name__ == "__main__":
    seed_data()
