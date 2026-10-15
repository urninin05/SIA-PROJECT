from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-date_created')
    return render(request, 'alfaye/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        Task.objects.create(
            task_title=request.POST['task_title'],
            description=request.POST['description'],
            subject=request.POST['subject'],
            deadline=request.POST['deadline'],
            status=request.POST['status']
        )

        return redirect('task_list')

    return render(request, 'alfaye/task_form.html')


def task_update(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.task_title = request.POST['task_title']
        task.description = request.POST['description']
        task.subject = request.POST['subject']
        task.deadline = request.POST['deadline']
        task.status = request.POST['status']
        task.save()

        return redirect('task_list')

    return render(request, 'alfaye/task_form.html', {'task': task})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(
        request,
        'alfaye/task_confirm_delete.html',
        {'task': task}
    )