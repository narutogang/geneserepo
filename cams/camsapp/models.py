from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,User

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo=models.FileField(blank=True, null=True)
    DOB=models.DateField()
    tenth_marks=models.FloatField(default=0)
    inter_marks=models.FloatField(default=0)
    current_marks=models.FloatField(default=0)
    branch = models.CharField(max_length=100,
        choices=(('Computer Science & Engineering','Computer Science & Engineering'),('Electrical Engineering','Electrical Engineering'),('Civil Engineering','Civil Engineering'),('Others','Others')),
        default='Computer Science & Engineering',
        )

    year = models.IntegerField(
        choices=((1,'Ist Year'),(2,'IInd Year'),(3,'IIIrd Year'),(4,'IVth Year')),
        default=1,
        )
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.user.username})


class Faculty(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo=models.FileField()
    specialization=models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.user.username})

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE,)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserProfileInfo(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE,)
    #additional classes
    member= models.CharField(max_length=264)
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
