## 🧼 Django Clean

## What is this?
**Django** is a basic CMS framework written in Python. This project will install it quickly.


> ## How it was done:
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
> 12.Run 🔁 ⬛️ `open http://localhost:8000/admin/login/ && pm runserver`
> 
> *And so, this repo is a reflection of the above steps.*

## Install
**⬛️ run these after you first download the repository `git clone git@github.com:helior/django-clean.git`**

**🔁 run these when you're starting a new branch.**

## How to keep clean:
(0) ⬛️ `git checkout -b dirty-stuff`

(1) Run ⬛️ `rm -rf db.sqlite3` 

(2) Run every step with a 🔁 above.

###### Note
If you make changes to main that you don't intend to maintain, run `git status` and just like, `git reset --hard` to wipe everything clean again.


## My aliases and functions:
```
#aliases
pa='source venv/bin/activate && echo '\''🐍 Python Virtualenv Activated!!'\'
pi='python -m pip install -r requirements.txt'

# bash/zsh functions
pm() {
  python3 manage.py $@
}
```
