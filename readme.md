# 100 Days App
## Purpose
A community where people strive to become more consistent, more disciplined, and more driven than ever before. Takes inspiration from Mark Manson's "Atomic Habits" and provides users with a system to better drive discipline.

## Tech Stack
- Django (Python 3.10)
- VueJS Integration
- TypeScript
- CSS Libary undecided
- SQLite3 (Postgres planned in the future)


# Things to Include in MVP

- drag up to reload page
- show top 20 posts on front page
- allow commenting like reddit-style
- clicking into one of the top 20 posts goes to the post view page

# Developers - environment setup instructions
Language and version:
- Python 3.10.5

Formatter and linter:
- Black

# Installing Dependencies (as of 1/15/2023)

- install Python 3.10.5
- create a virtual environment `python -m venv venv`
- install dependencies `pip install -r requirements.txt`
- make migrations
`python manage.py makemigrations`
`python manage.py migrate`
- run the server
`python manage.py runserver`
- test an endpoint
`http://127.0.0.1:8000/posts/`

If the above page is viewable, you have configured the project successfully.
