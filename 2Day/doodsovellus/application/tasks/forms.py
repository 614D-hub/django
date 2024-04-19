from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, validators

# 自定义表单字段 传参为label 
class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.length(min=2)])
    done = BooleanField("Done")

    class Meta:
        csrf = False