from django.shortcuts import render, redirect
from myapp.models import Task

# Create your views here.
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/tasks.html', {'tasks': tasks})


def add_tasks(request):
    if request.method == "POST":
        task = request.POST
        add = Task.objects.create(title=task['title'], body=task['body'], deadline=task['deadline'])
        add.save()
        return redirect('tasks')
    else:
        return render(request, 'myapp/add_tasks.html')