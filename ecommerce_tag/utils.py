import random
import string

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

