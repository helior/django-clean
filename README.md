## 🧼 Django Clean

This is a clean install of **Django**, with an example "project" that gets you a model, API crud endpoint, CMS-features, API documentation, etc. This is the starting point that **I enjoy using**, and maybe you will too!

Happy coding 👋🏼🔥

## What is Django?
**[Django](https://www.djangoproject.com/)** is a basic, but very useful CMS/framework written in **[Python](https://www.python.org/)**.

## ⬛️ Install
1) Download the repository `git clone git@github.com:helior/django-clean.git`
2) Read **"[How it was done](https://github.com/helior/django-clean#how-it-was-done)"** below, and run the the steps marked with a "⬛️"


> ## How it was done (my notes to self):
> 1. Make directory
> 2. `cd` into directory
> 3. Create basic files
>     1. requirements.txt
>     2. .gitignore
> 4. Create manage.py
> 5. Run ⬛️ `virtualenv venv`
> 6. Run ⬛️ `pa` to activate virtualenv
> 7. Run ⬛️ `pi` tp install dependencies
> 8. Run `django-admin startproject service .`
> 9. Run 🔁 ⬛️ `pm migrate` to create database records
> 10. Run 🔁 ⬛️ `pm createsuperuser --noinput --username=admin --email=me@helior.info`
> 11. Run 🔁 ⬛️ `pm changepassword admin` (set to admin)
> 12. Run 🔁 ⬛️ `open http://localhost:8000/admin/login/ && pm runserver`
>
> *And so, this repo is a reflection of the above steps.*


## 🔁 Start over:
1. ⬛️ `git checkout -b my-experimental-branch`
2. Run ⬛️ `rm -rf db.sqlite3`
3. Run every step with a 🔁 above.


## My aliases and functions:
```
#aliases
pa='source venv/bin/activate && echo '\''🐍 Python Virtualenv Activated!!'\'
pd='deactivate && echo '\''🐍 Python Deactivated ❌'\'
pi='python -m pip install -r requirements.txt'

# bash/zsh functions
pm() {
  python3 manage.py $@
}
```
