from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from accounts.models import CustomUser
from django.db import models

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser  # Import CustomUser
from .models import Message
from .forms import MessageForm

@login_required
def chat(request, receiver_id):
    receiver = get_object_or_404(CustomUser, id=receiver_id)  # Use CustomUser
    messages = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=receiver)) |
        (models.Q(sender=receiver) & models.Q(receiver=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.save()
            return JsonResponse({'success': True, 'message': message.content})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = MessageForm()

    return render(request, 'messaging/chat.html', {'receiver': receiver, 'messages': messages, 'form': form})



@login_required
def get_messages(request, receiver_id):
    receiver = get_object_or_404(CustomUser, id=receiver_id)
    messages = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=receiver)) |
        (models.Q(sender=receiver) & models.Q(receiver=request.user))
    ).order_by('timestamp')
    message_data = [{'sender': msg.sender.username, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages]
    return JsonResponse({'messages': message_data})
