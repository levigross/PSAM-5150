from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=100)
    games = models.ForeignKey('Game', related_name='games')

    def __unicode__(self):
        return self.name


class Game(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    players = models.ForeignKey('Player', verbose_name='players')
    in_session = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.end:
            self.in_session = False
        super(Game, self).save(*args, **kwargs)


class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __unicode__(self):
        return self.name
