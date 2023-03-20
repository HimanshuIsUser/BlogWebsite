from django.utils.text import slugify
from .models import *
import random
import string
def random_string(n):
    text = "".join(random.choices(string.ascii_uppercase + string.digits,k=n))
    return text


def generate_slug(text):
    new_slug = slugify(text)
    from .models import BlogModel

    if BlogModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + random_string(5))
    
    return new_slug
