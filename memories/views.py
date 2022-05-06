from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MemoriesForm
from .models import Memories


@login_required
def my_memories(request):
    memories = Memories.objects.filter(user=request.user)
    return render(request, 'memories/my_memories.html', {'memories': memories})


@login_required
def new_memory(request):
    error = ''
    if request.method == 'POST':
        user_memory = MemoriesForm(request.POST)
        if user_memory.is_valid():
            instance = user_memory.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('my_memories')
        else:
            error = 'Форма была заполнена некорректно. Заполните данные правильно и попробуйте еще раз'

    form = MemoriesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'memories/new_memory.html', data)
