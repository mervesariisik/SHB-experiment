from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Lottery_Intro(Page):
    pass

class Lottery(Page):
    form_model = 'player'
    form_fields = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15']

    def error_message(self, values):
        if values["d1"] is None or values["d2"] is None or values["d3"] is None or \
                values["d4"] is None or values["d5"] is None or values["d6"] is None or values["d7"] is None or \
                values["d8"] is None or values["d9"] is None or values["d10"] is None or values["d11"] is None or \
                values["d12"] is None or values["d13"] is None or values["d14"] is None or values["d15"] is None:
            return "Please make a choice for every Situation before proceeding."

    timeout_seconds = 180

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.d1 = random.randint(1,2)
            p.d2 = random.randint(1,2)
            p.d3 = random.randint(1,2)
            p.d4 = random.randint(1,2)
            p.d5 = random.randint(1,2)
            p.d6 = random.randint(1,2)
            p.d7 = random.randint(1,2)
            p.d8 = random.randint(1,2)
            p.d9 = random.randint(1,2)
            p.d10 = random.randint(1,2)
            p.d11 = random.randint(1,2)
            p.d12 = random.randint(1,2)
            p.d13 = random.randint(1,2)
            p.d14 = random.randint(1,2)
            p.d15 = random.randint(1,2)

            print("<Time Out on Page:'Lottery'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:", p.d1, p.d2, p.d3,
                  p.d4, p.d5, p.d6, p.d7, p.d8, p.d9, p.d10, p.d11, p.d12, p.d13, p.d14, p.d15)

        p.set_payoff()

class Lottery_Results(Page):
    def vars_for_template(self):
        return{
            'picked_line': self.player.picked_d,
            'decision': self.player.decision==1,
            'payoff': self.player.payoff,
        }

    def before_next_page(self):
        self.participant.vars['lottery_payoff'] = self.player.payoff


page_sequence = [Lottery_Intro,
                 Lottery,
                 Lottery_Results
                 ]
