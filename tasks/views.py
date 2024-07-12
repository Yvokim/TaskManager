from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Subtask
from .forms import TaskForm, SubTaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    subtasks = task.subtasks.all()
    return render(request, 'tasks/task_detail.html', {'task': task, 'subtasks': subtasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)

    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)

    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})


def task_confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return redirect('task_confirm_delete', pk=pk)


def subtask_create(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
            return redirect('task_detail', pk=task.pk)

    else:
        form = SubTaskForm()
    return render(request, 'tasks/subtask_form.html', {'form': form, 'task': task})


def subtask_detail(request, task_pk, subtask_pk):
    subtask = get_object_or_404(Subtask, pk=subtask_pk)
    return render(request, 'tasks/subtask_detail.html', {'subtask': subtask})


def subtask_edit(request, task_pk, subtask_pk):
    subtask = get_object_or_404(Subtask, pk=subtask_pk, task_id=task_pk)
    if request.method == 'POST':
        form = SubTaskForm(request.POST, instance=subtask)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task_pk)

    else:
        form = SubTaskForm(instance=subtask)
    return render(request, 'tasks/subtask_form.html', {'form': form, 'task': subtask.task})


def subtask_confirm_delete(request, task_pk, subtask_pk):
    task = get_object_or_404(Task, pk=task_pk)
    subtask = get_object_or_404(Subtask, pk=subtask_pk)
    return render(request, 'tasks/subtask_confirm_delete.html', {'task': task, 'subtask': subtask})


def subtask_delete(request, task_pk, subtask_pk):
    subtask = get_object_or_404(Subtask, pk=subtask_pk, task_id=task_pk)
    if request.method == 'POST':
        task = subtask.task
        subtask.delete()
        return redirect('task_detail', pk=task_pk)
    return render(request, 'tasks/subtask_confirm_delete.html', {'subtask': subtask})
