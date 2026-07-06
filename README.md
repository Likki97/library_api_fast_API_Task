```markdown
# Library Management API

A simple backend API to manage books in a library — add, view, update, and delete books. Built to practice FastAPI properly with a real database, without any frontend involved.

## What this project does

This API lets you:
- Add a new book
- View all books (with an option to filter by author)
- View a single book by its ID
- Update a book's details
- Delete a book

Every book has a title, author, ISBN, published year, total copies, and available copies. Data is validated before it's saved, so things like a wrong published year or a missing title get rejected automatically.

## Tech used

- **FastAPI** – handles the API routes and validation
- **Uvicorn** – runs the app
- **PostgreSQL** – the actual database
- **SQLAlchemy** – lets Python talk to PostgreSQL
- **Pydantic** – validates incoming data before it reaches the database

## Project structure

```
library_api/
├── main.py        - all the API endpoints
├── database.py     - database connection setup
├── models.py        - the books table structure
├── schemas.py        - defines valid input and output formats
└── requirements.txt
```

## How to run this on your machine

1. Install PostgreSQL if you don't have it already.

2. Create a database:
```sql
CREATE DATABASE library_db;
```

3. Clone this repo and go into the folder:
```
git clone <your-repo-link>
cd library_api
```

4. Create a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

5. Install the required packages:
```
pip install -r requirements.txt
```

6. Open `database.py` and update the database URL with your own PostgreSQL password:
```python
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/library_db"
```

7. Run the app:
```
uvicorn main:app --reload
```

8. Open your browser and go to:
```
http://127.0.0.1:8000/docs
```

This opens an interactive page where you can test every endpoint directly, no separate frontend or tool needed.

## Testing it

- Add a book using `POST /books`
- See all books using `GET /books`
- Filter by author using `GET /books?author=somename`
- Update a book using `PUT /books/{id}`
- Delete a book using `DELETE /books/{id}`

You can also check the data directly in PostgreSQL using pgAdmin's Query Tool:
```sql
SELECT * FROM books;
```

## What I learned building this

- How to connect a FastAPI app to a real PostgreSQL database using SQLAlchemy
- How Pydantic validates data automatically before it's saved
- Why request format and response format should be kept separate
- How to check and confirm database data directly, instead of just trusting the API

## What's next

- Add a members table so users can borrow and return books
- Add login so only registered users can add or edit books
- Add basic tests
- Connect a simple React frontend
```

Just paste this into a file called `README.md` in your project folder and push it — GitHub will render it automatically with the headings and code blocks formatted properly. Replace `<your-repo-link>` with your actual repo URL.
