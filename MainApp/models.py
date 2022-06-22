from django.db import models
from tinymce.models import HTMLField

# Create your models here.

HOST_NAME = 'http://127.0.0.1:8000'
TUT_TYPES = (
    ('Programming-Language', 'Programming-Language'),
    ('Preparation', 'Preparation'),
    ('Theory-Tutorial', 'Theory-Tutorial'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('Javascript', 'Javascript'),
    ('Database-Tutorial', 'Database-Tutorial'),
    ('Web-Technology', 'Web-Technology'),
    ('Microsoft-Office', 'Microsoft-Office'),
    ('Versioning-Control', 'Versioning-Control')
)


class TutList(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TUT_TYPES, default='Python')
    image = models.ImageField(upload_to='tut-icon/')
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tut-Lists'


class TutCommon(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    viewcounter = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Commented by {self.name}'
