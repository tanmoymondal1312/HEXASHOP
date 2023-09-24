from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser





@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(CustomUser, id=receiver_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            message = Message(sender=request.user, receiver=receiver, content=content)
            message.save()
            return redirect('message_list')  # Redirect to a message list view
    else:
        form = MessageForm()
    
    return render(request, 'message/send_message.html', {'form': form, 'receiver': receiver})

@login_required
def message_list(request):
    # Get the user's sent and received messages
    sent_messages = Message.objects.filter(sender=request.user)
    received_messages = Message.objects.filter(receiver=request.user)
    
    return render(request, 'message/message_list.html', {'sent_messages': sent_messages, 'received_messages': received_messages})

