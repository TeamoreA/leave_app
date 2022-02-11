from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Leave
from .forms import LeaveForm, UserForm

def leave_index_view(request):
    latest_leaves_list = Leave.objects.order_by('-created_at')[:40]
    context = {'latest_question_list': latest_leaves_list}
    return render(request, 'leave_requests/index_view.html', context)

def update_leave_view(request, leave_id):
    leave = get_object_or_404(Leave, pk=leave_id)
    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        form = LeaveForm(instance=leave)
    
    return render(request, 'leave_requests/update_leave_view.html', {'form': form, 'leave': leave})
        


def create_leave_view(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LeaveForm()

    return render(request, 'leave_requests/create_leave_view.html', {'form': form})

def delete_leave_view(request, leave_id):
    leave = get_object_or_404(Leave, pk=leave_id)
    if request.method == 'POST':
        leave.delete()

    return HttpResponseRedirect(reverse('index'))


def create_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserForm()

    return render(request, 'leave_requests/create_user_view.html', {'form': form})
