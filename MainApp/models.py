from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy
from django.conf import settings

# Create your models here.
HOST_NAME = settings.HOST_NAME
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
    ('Versioning-Control', 'Versioning-Control'),
    ('Web-Hosting', 'Web-Hosting'),
)


class TutList(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TUT_TYPES, default='Python')
    image = models.ImageField(upload_to='tut-icon/')
    link = models.URLField(default=HOST_NAME + "/")

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


class Blogs(TutCommon):
    image = models.ImageField(upload_to='blogs/', default='')

    class Meta:
        verbose_name_plural = 'Blogs'

    def get_absolute_url(self):
        return f'{reverse_lazy("w3c:blogdetail", kwargs={"slug": self.slug})}'


class BlogComments(Comments):
    ip_address = models.GenericIPAddressField(default="45.243.82.169")
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='BlogComments')
    class Meta:
        verbose_name_plural = 'BlogComments'
