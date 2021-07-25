from .models import Place
from django.utils.crypto import get_random_string


def generate_unique_code():

    code = get_random_string(7)
    object_test = Place.objects.filter(code=code).exists()
    while object_test:
        code = get_random_string(9)
        object_test = Place.objects.filter(code=code).exists()

    return 'RW-'+code

