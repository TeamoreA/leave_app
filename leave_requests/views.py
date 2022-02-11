from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Leave
from .forms import LeaveForm

def leave_index_view(request):
    latest_leaves_list = Leave.objects.order_by('-created_at')[:40]
    context = {'latest_question_list': latest_leaves_list}
    return render(request, 'leave_requests/index.html', context)

def update_leave_view(request, leave_id):
    leave = get_object_or_404(Leave, pk=leave_id)
    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        form = LeaveForm(instance=leave)
    
    return render(request, 'leave_requests/update_leave.html', {'form': form, 'leave': leave})
        


def create_leave_view(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LeaveForm()

    return render(request, 'leave_requests/create_leave.html', {'form': form})


def create_user_view(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LeaveForm()

    return render(request, 'leave_requests/create.html', {'form': form})
