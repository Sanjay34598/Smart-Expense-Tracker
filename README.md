# 💰 Smart Expense Tracker

A lightweight web application built with **Flask** and **SQLite** to help you track your daily expenses, manage your monthly salary, and monitor your savings — all in one place.

---

## ✨ Features

- 📋 **Add & Manage Expenses** — Log expenses with title, amount, category, and date
- 🗑️ **Delete Expenses** — Remove individual expense entries
- 🔍 **Filter Expenses** — Filter by category or date
- 💵 **Salary Tracker** — Set your monthly salary for the current month
- 📊 **Spending Summary** — View total all-time spending and current month spending
- 💾 **Savings Calculator** — Automatically calculates savings (Salary − Monthly Expenses)
- 🍩 **Category Chart** — Visual doughnut chart showing expense breakdown by category
- 🌱 **Sample Data Seeder** — Quickly populate the database with sample data for testing

---

## 🗂️ Project Structure

```
Smart-Expense-Tracker/
│
├── app.py              # Main Flask application
├── seed.py             # Script to seed the database with sample data
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── templates/
    └── index.html      # Frontend HTML template
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sanjay34598/Smart-Expense-Tracker.git
   cd Smart-Expense-Tracker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

---

## 🌱 Seed Sample Data

To populate the database with sample expenses and salary data for testing:

```bash
python seed.py
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python / Flask | Backend web framework |
| SQLite | Lightweight database |
| Flask-SQLAlchemy | ORM for database interaction |
| HTML / CSS / JavaScript | Frontend |
| Chart.js | Expense category donut chart |

---

## 📦 Dependencies

See [`requirements.txt`](requirements.txt) for the full list of Python packages.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
