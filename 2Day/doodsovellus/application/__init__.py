"""
Python 将每个文件夹视为一个模块，
其行为有点像 Java 中的包。
每个模块（包）必须有一个名为 的文件__init__.py，
该文件告诉 Python 相关文件夹包含与项目相关的源代码。

该文件__init__.py还可以包含应用程序初始化时执行的源代码。
我们的应用程序是 Flask 应用程序——我们启动 Flask 作为__init__.py文件执行的一部分。
文件夹application中文件的内容__init__.py
"""
from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)




from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
# 打印所有查询
app.config["SQLALCHEMY_ECHO"] = True
# 创建了一个数据库对象 自动读取flask的配置
db = SQLAlchemy(app)
from application import views

from application.tasks import models

from application.auth import models
from application.auth import views

from application.auth.models import User
from os import urandom
app.config['SECRET_KEY'] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'auth_login'
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# 必须开启上下文
with app.app_context():
    db.create_all()