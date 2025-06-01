# Week 3 Workshop: Secrets Management with Python & Google Cloud SQL

## Overview

This project demonstrates how to securely manage secrets in a Python application using:
- `.env` files
- `python-dotenv`
- `psycopg2-binary`
- Google Cloud SQL (PostgreSQL)

## Environment Variables

Secrets are loaded from a `.env` file using `load_dotenv()`:

```env
DB_HOST=your-cloud-sql-ip  
DB_NAME=your-database-name  
DB_USER=your-db-user  
DB_PASSWORD=your-password  
```



## Running the Scripts

1. Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Run the test script:

```bash
python3 test_env.py
```

3. Run the DB connection script:
```bash
python3 db_connect.py
```

4. Install all dependencies:
```bash
pip install -r requirements.txt
```

5. Prepare your project for GitHub:
```bash
echo "venv/" >> .gitignore
git init
git add .
git commit -m "Week 3 Secrets Workshop Complete"
git remote add origin https://github.com/YOUR_USERNAME/week3_workshop_secrets_project.git
git push -u origin main
```

If successful, you’ll see:
```bash
✅ Connected to the database!
🧠 PostgreSQL version: ...
```
