import os
import datetime
import random, string

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f'products/{year}/{month}/{instance.title}/{final_name}'


def random_string(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))


def uniqe_slug_gen(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = instance.title.replace(' ', '-')
    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{random_string}".format(slug=slug, random_string=random_string(size=3))
        return uniqe_slug_gen(instance, new_slug=new_slug)
    return slug

