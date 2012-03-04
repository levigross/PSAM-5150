from datetime import datetime

from django.test import TestCase
from models import Game, Host, Player

class SimpleTest(TestCase):

    def setUp(self):
        self.host = "James"
        self.players = [Player.objects.create(name=player, score=0) for player in range(100)]

    def testGameCreation(self):
        football = Game()
        football.title = "The Big football game"
        football.description = "Blah Blah Blah"
        football.players = self.players[1]
        football.save()
        for player in self.players[1:]:
            football.players = player
            football.save()

    def testHost(self):
        raise NotImplementedError

    def testPlayer(self):
        raise NotImplementedError



