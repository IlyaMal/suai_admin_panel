import requests
import base64
from django.core.files.storage import FileSystemStorage
from lab_bot.settings import MEDIA_ROOT


def _save_image(request_file):
    fs = FileSystemStorage(location=MEDIA_ROOT)
    filename = fs.save(request_file.name, request_file)
    print(MEDIA_ROOT + filename)
    return MEDIA_ROOT + '\\' + filename


def _image_to_byte_code(image_path):
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

    return image_base64


def send(url, request_data, request_file, ids=None):
    image_path = _save_image(request_file)
    print(image_path + 'asd')
    image_base64 = _image_to_byte_code(image_path)

    data = {
        'id': ids,
        'message': request_data.get('message'),
        'photo': image_base64
    }

    response = requests.post(url, json=data)

    return  response.status_code
