from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class C_Questions_Intro(Page):
    pass


class C_Questions(Page):
    form_model = 'player'
    form_fields = ['question1', 'question2', 'question3']

    timeout_seconds = 180

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.question1 = random.randint(1,100)
            p.question2 = random.randint(1,100)
            p.question3 = random.randint(1,100)

            print("<Time Out on Page:'C_Questions'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:", p.question1,
                  p.question2, p.question3)

        p.set_payoff()


class C_Questions_Results(Page):
    def before_next_page(self):
        self.participant.vars['crt_payoff'] = self.player.payoff


page_sequence = [C_Questions_Intro,
                 C_Questions,
                 C_Questions_Results
                 ]
