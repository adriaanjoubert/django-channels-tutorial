from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name='chat/index.html',
    )


def room(request: HttpRequest, room_name: str) -> HttpResponse:
    return render(
        request=request,
        template_name='chat/room.html',
        context={
            'room_name': room_name,
        },
    )
