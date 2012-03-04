from django.views.generic import TemplateView
from django.shortcuts import redirect
from models import Game, Player
from forms import GameScore
from django.contrib import messages

class GameMain(TemplateView):
    template_name = 'gameshow/main.html'

    def get_context_data(self, **kwargs):
        return {
            'num_games': Game.objects.all().count(),
            'num_players': Player.objects.all().count(),

            }


class GameView(TemplateView):
    template_name = 'gameshow/game.html'

    def _start_game(self):
        player = Player.objects.create(name="Some Name", score=0)
        self.thegame = Game()
        self.thegame.players = player
        self.thegame.title = 'My Game Title'
        self.thegame.description = "Blah Blah Blah"
        self.thegame.save()

    def post(self, request, *args, **kwargs):
        form = GameScore(request.POST)
        if form.is_valid():
            messages.add_message(self.request, messages.INFO, message="Enjoy your game!")
            return redirect('game_main')
        else:
            return self.get(request, form=form)

    def get_context_data(self, **kwargs):
        self._start_game()
        return {
            'form': GameScore() if not kwargs.get('form') else kwargs['form'],
            'game': self.thegame,
            }

