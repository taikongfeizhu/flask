# Developing web blog applications with flask & backbone


## About

Flask一个基于**python**开发的**轻量级快速开发web框架**,也被称为 “microframework” ，因为它使用简单的核心，用 extension 增加其他功能。Flask没有默认使用的数据库、窗体验证工具。然而，Flask保留了扩增的弹性，可以用Flask-extension加入这些功能：ORM、窗体验证工具、文件上传、各种开放式身份验证技术,Flask具有简单易学,功能强大等特点,搭配经典的前端mvc框架**backbone**能非常方便的创建各种web服务和应用.

> 如果对Python和web框架先有些了解，但理解不深的，可阅读经典python开发文档 <br>
> backbone等经典前端mvc化已经成为前端应用开发的主流模式[详细请参考](https://github.com/tastejs/todomvc)

## Requirements

本项目中的应用程序开发需要设置安装所需并依赖一组类库来满足工作要求,需要安装的依赖组件如下(建议在python的venv下安装):

* Flask==0.10.1
* Flask-Bootstrap==3.3.5.6
* Flask-Mail==0.9.1
* Flask-Migrate==1.6.0
* Flask-Moment==0.5.1
* Flask-Script==2.0.5
* Flask-SQLAlchemy==2.0.post20151008
* Flask-WTF==0.12
* Jinja2==2.7.3
* Mako==1.0.2
* MarkupSafe==0.23
* SQLAlchemy==1.0.8
* WTForms==2.0.2
* Werkzeug==0.10.4
* alembic==0.8.2
* blinker==1.4
* itsdangerous==0.24

可执行：<code>pip install -r requirements.txt</code>
 
Check out our [requirements docs](requirements.txt) for more info. 

## Run site
1. <code>python index.py runserver -h 0.0.0.0 -p 3001 -r</code>
2. <code>python manage.py db init</code>
3. <code>python manage.py db migrate -m 'initial migration'</code>
4. <code>python manage.py db upgrade</code>
5. <code>pip freeze > requirements.txt</code>

## Code version control ##
git常用使用命令

### git initialize
* git init
* git add README.md
* git commit -m "first commit"
* git status

### git push ###
* git remote add origin git@github.com:taikongfeizhu/flask.git
* git push -u origin master

### git rebase ###
* git rebase -i (git rebase --continue , git rebase --abort)
* git pull --rebase
  
  
## License

Everything in this repo is GNU License unless otherwise specified.

Coder Jenking.Wong ©2015