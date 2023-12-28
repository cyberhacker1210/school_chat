from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse , JsonResponse

def home(request):
    return render(request, 'chat/home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = 'chat_room'
    username = request.POST['username']
    return redirect('/' + room + '/?username=' + username)



def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message envoyé avec succès')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id).order_by('date')
    return JsonResponse({"messages": list(messages.values())})
