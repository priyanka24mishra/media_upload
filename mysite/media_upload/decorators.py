from django.core.exceptions import ValidationError
from rest_framework.response import Response
from functools import wraps
from rest_framework import status
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from functools import wraps
from media_upload.models import MediaUpload


def validate_media_file(function):
    """
    Decorator to check if media upload is valid or not
    :param function:
    :type function:
    :return:
    :rtype:
    """
    @wraps(function)
    def wrap(*args, **kwargs):
        if not MediaUpload.objects.filter(id=kwargs['upload_type_id']).exists():
            return Response({'message':"Data not fuond", 'status_code': status.HTTP_403_FORBIDDEN})
        return function(*args, **kwargs)

    return wrap
