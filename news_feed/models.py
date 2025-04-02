from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status= News.Status.Published)



class Category(models.Model):
    objects = None
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):



    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')

    #category bilan newsni bog'laymiz
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)

    publish_time = models.DateTimeField(timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    upload_time =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default = Status.Draft)


    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish_time'] #Yangilikni oxirgisini eng yuqorida  chiqaradi

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])




#
# Draft = qoralama
# published = jo'natilgan'



class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    massage = models.TextField()

    def __str__(self):
        return self.email



