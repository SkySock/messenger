from django.core.exceptions import ValidationError


def get_path_upload_profile_image(instance, file):
    return f'profile-images/{instance.id}/{file}'


def get_default_profile_image():
    return 'images/defaults/default_profile_image.png'


def validate_image_size(file_obg):
    megabyte_limit = 2
    if file_obg.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max file size should be {megabyte_limit} MB")

