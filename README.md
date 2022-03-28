## 🧼 Django Clean

## What is this?
This is a clean install of Django, with an example "project" that gets you a model, api endpoint, CMS-features, basic auth, etc. This is the starting point that **I enjoy using**, and maybe you will too!

Happy coding 👋🏼🔥

## What is Django?
**[Django](https://www.djangoproject.com/)** is a basic, but very useful CMS/framework written in **[Python](https://www.python.org/)**.


> ## How it was done (if you're curious):
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

## Install
1) download the repository `git clone git@github.com:helior/django-clean.git`
2) Read **"[How it was done](https://github.com/helior/django-clean#how-it-was-done)"** above, and run the the steps marked with a "⬛️"


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
