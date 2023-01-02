from django.urls import re_path

from file_download import consumers

websocket_urlpatterns = [
    re_path(r'ws/file-download/$', consumers.FileDownloadConsumer.as_asgi()),
]
