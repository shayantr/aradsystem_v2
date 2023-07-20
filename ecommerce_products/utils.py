import os
import datetime

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

