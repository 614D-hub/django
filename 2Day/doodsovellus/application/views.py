from flask import render_template, request, redirect, url_for

from application import app, db # 这里的from ... import ...可以直接引用 函数 、类和变量
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())


@app.route("/tasks/<task_id>/", methods=["POST"])
def tasks_set_done(task_id):
    
    t = Task.query.get(task_id)
    t.done = True
    db.session().commit()
    
    return redirect(url_for("tasks_index")) # 重定向到task_index这个路由 或者直接写具体的html也可以

@app.route("/tasks/", methods=["POST"])
def tasks_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)
    
    t = Task(form.name.data)
    t.done = form.done.data

    db.session().add(t)
    db.session().commit()
    
    return redirect(url_for("tasks_index"))

@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html" , form = TaskForm())    
