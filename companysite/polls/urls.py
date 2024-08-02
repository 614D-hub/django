from django.urls import path
from . import views

# 添加命名空间 当服务越来越健壮 相同的detail django是分不清具体是那个应用的 
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/",views.vote, name="vote"),
]