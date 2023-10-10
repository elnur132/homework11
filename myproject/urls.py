
from django.contrib import admin
from django.urls import path, re_path
from myapp.views import tasks, add_tasks

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^$", tasks, name="tasks"),
    # task выводит лист задач
    re_path(r"^add", add_tasks, name="add_tasks"),
    # add_tasks выводит форму
]
