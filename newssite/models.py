from django.db import models


STATUS_CHOICES = (
    (1, 'pendding'),
    (2, 'publish'),
    (3, 'delete'),
    (4, 'archive'),
)

from taggit.managers import TaggableManager
# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.IntegerField()
    long = models.IntegerField()

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, max_length=255)
    parent=models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


class File(models.Model):
    file_name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    type = models.CharField(max_length=5)
    size = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    slug = models.SlugField(unique=True, max_length=255)



class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_day = models.DateField()
    slug = models.SlugField(unique=True, max_length=255)


class Post(models.Model):

    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    body = models.TextField()
    keywords = models.TextField()
    publish_time = models.DateTimeField()
    status=models.IntegerField(choices=STATUS_CHOICES)
    priority=models.IntegerField()
    count_view=models.IntegerField(default=0)
    code=models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True, blank=True)
    tags = TaggableManager()
    category = models.ManyToManyField(Category, null=True, blank=True)
    file = models.ManyToManyField(File, null=True, blank=True)
    author = models.ManyToManyField(Author, null=True, blank=True)

    def first_category(self):
        return self.category.first()


