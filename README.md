Library Management System (Django)

Purpose

This project is a minimal, focused Library Management System that demonstrates how to build a clean CRUD web app with Django. It emphasizes clarity of structure, pragmatic Django patterns, and approachable UI using Bootstrap and Font Awesome.

What this project showcases (techniques)

- Django MVC (MTV) patterns: models for data, views for orchestration, templates for presentation
- CRUD with server‑rendered forms: add, edit, delete, list books
- CSRF protection and semantic forms using Bootstrap classes
- Template composition: shared `base.html` layout, per‑page templates extending it
- Context-driven UI: home page aggregates statistics (books count, unique authors, total value)
- QuerySet usage: ordering, slicing (recent books), distinct author set
- Safe defaults in templates using Django filters like `|default` and `|length`
- Simple, readable styling via a custom theme plus Bootstrap utilities
- Small, testable, maintainable view functions that do one thing well

Core features

- Add a new book (title, author, price)
- View all books and navigate to edit/delete
- Edit an existing book inline via prefilled form
- Delete a book with a confirmation
- Home dashboard showing:
  - Total Books
  - Authors (unique count)
  - Collection Value (sum of prices)
  - Recent books grid

Architecture overview

- App: `bmapp`
- Project: `bmproject`
- Model: `Book` (`title`, `author`, `price`)
- Views:
  - `homeView` – builds dashboard context (`books`, `recent_books`, unique `authors`, `total_value`)
  - `helloView` – lists all books
  - `addBookView` and `addBook` – render/handle add form
  - `editBookView` and `editBook` – render/handle edit form
  - `deleteBookView` – removes a book and redirects home
- Templates:
  - `base.html` – sitewide layout and footer
  - `home.html` – hero, stats, features, recent books
  - `addbook.html`, `edit-book.html`, `viewbook.html` – CRUD pages
- Static:
  - `static/css/library-theme.css` – theme and utilities layered on Bootstrap

Data model

- `Book`
  - `title: CharField`
  - `author: CharField`
  - `price: IntegerField`

Key implementation details

- Recent books: `books = Book.objects.all().order_by('-id')[:6]`
- Unique authors: `values_list('author', flat=True).distinct()` with null/empty filtering
- Total value: `sum(book.price for book in books if book.price)`
- Defensive templating with `|default` for missing values

Why server-rendered Django?

- Great defaults (security, CSRF, templating) and fast iteration
- Predictable performance with minimal client JavaScript
- Easier SEO and accessibility from HTML-first rendering

Local setup

1) Prerequisites
- Python 3.10+

2) Install & run
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install django
python manage.py migrate
python manage.py runserver
```

3) Use the app
- Home: http://127.0.0.1:8000/
- Add Book: `/add-book`
- View Books: `/view-book`
- Edit/Delete via actions on book cards or list

Conventions and style

- Keep view functions small and explicit; avoid unnecessary try/except blocks
- Prefer expressive variable names and early returns
- Use Bootstrap grid/utility classes for consistent spacing and layout
- Keep comments for non-obvious rationale, not for narrating code

Extending the project (next steps)

- Validation and user messages (flash/alerts)
- Pagination and search on the books list
- Per-book ratings and an average rating on the dashboard
- Price as DecimalField with currency formatting
- Django admin customization for quick back-office management
- Basic authentication and per-user collections

License

This project is for learning and demonstration purposes.


