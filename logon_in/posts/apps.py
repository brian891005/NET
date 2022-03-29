from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'

class UploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upload'
