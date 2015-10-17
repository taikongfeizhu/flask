### run site ###
>1. python index.py runserver -h 0.0.0.0 -p 3001 -r
>1. python manage.py db init
>1. python manage.py db migrate -m 'initial migration'
>1. python manage.py db upgrade

### dependencies plugin ###
>1. flask.ext.script
>1. flask.ext.moment
>1. flask.ext.wtf
>1. flask.ext.bootstrap
>1. flask.ext.sqlalchemy
>1. flask-mail
>1. flask-migrate

### git init ###
>1. echo "# flask" >> README.md
>1. git init
>1. git add README.md
>1. git commit -m "first commit"
>1. git remote add origin git@github.com:taikongfeizhu/flask.git
>1. git push -u origin master

### git push ###
>1. git remote add origin git@github.com:taikongfeizhu/flask.git
>1. git push -u origin master

### git rebase ###
>1. git rebase -i (git rebase --continue , git rebase --abort)
>1. git pull --rebase