import json
import tempfile

from channels.generic.websocket import WebsocketConsumer
from django.core.files.storage import default_storage


class FileDownloadConsumer(WebsocketConsumer):

    def connect(self) -> None:
        self.accept()

    def disconnect(self, close_code: int) -> None:
        pass

    def receive(self, text_data=None, bytes_data=None) -> None:
        with tempfile.TemporaryFile() as f:
            f.write(b'Hi')
            file_name = default_storage.save(f.name, f)
            self.send(text_data=json.dumps({'url': default_storage.url(file_name)}))
