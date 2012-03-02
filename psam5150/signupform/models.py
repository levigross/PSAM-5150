from django.db import models


class HelloWorld(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    message = models.TextField()

    def __unicode__(self):
        return self.name


class Signup(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reason_for_joining = models.TextField()
    picture = models.ImageField(upload_to='signupform/pics/')
    url = models.URLField(verify_exists=True)
    is_accepted = models.BooleanField(default=False)
    admin_comments = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField()

    def __unicode__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey('country', related_name='cities')
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class House(models.Model):
    city = models.ManyToManyField('City', related_name='houses')
    street = models.CharField(max_length=300)

    def __unicode__(self):
        return self.street

class Mayor(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey('City', related_name='mayor', unique=True)
    house = models.ForeignKey('House')
    has_kids = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
