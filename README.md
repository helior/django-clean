## Django Clean

#### How it was done:
1. Make directory
2. CD into directory
3. Create basic files
    1. requirements.txt
    2. .gitignore
4. Create manage.py
5. Create virtualenv venv
6. Install dependencies: run pi
7. Run django-admin startproject service .
8. Run pm migrate
9. Run pm createsuperuser --noinput --username=admin --email=me@helior.info
10. Run pm changepassword admin (set to admin)
11. Run pm runserver


#### How to keep clean:

Run git status and just like, git reset --hard to wipe everything out.

#### How to start-over:
Delete `db.sqlite3`. Run pm migrate, and every next step after that (see above).

