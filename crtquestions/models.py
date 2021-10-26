from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Merve Sariisik'

doc = """
SALARY HISTORY BAN EXPERIMENT
TREATMENT: Any
APP: Cognitive Reflection Test
"""


class Constants(BaseConstants):
    name_in_url = 'crtquestions'
    players_per_group = None
    num_rounds = 1

    dollar_per_ecu = 0.33


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question1 = models.FloatField(
        label='A hot dog bun and a sausage together cost 110 cents. The hot dog bun costs 100 cents more than the '
              'sausage. How much does the sausage cost? (Please enter your answer in cents)'
    )
    question2 = models.FloatField(
        label='If it takes 5 nurses 5 minutes to measure the blood pressure of 5 patients, how long would it take 100 '
              'nurses to measure the blood pressure of 100 patients? (Please enter your answer in minutes)'
    )
    question3 = models.FloatField(
        label='In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for '
              'the patch to cover the entire lake, how long would it take for the patch to cover half of the lake? '
              '(Please enter your answer in days)'
    )
    nbr_correct_answers = models.IntegerField()

    def set_payoff(self):
        self.nbr_correct_answers = 0
        if self.question1 == 5:
            self.nbr_correct_answers = self.nbr_correct_answers + 1
        else:
            pass
        if self.question2 == 5:
            self.nbr_correct_answers = self.nbr_correct_answers + 1
        else:
            pass
        if self.question3 == 47:
            self.nbr_correct_answers = self.nbr_correct_answers + 1

        total_points = self.nbr_correct_answers
        self.payoff = total_points * Constants.dollar_per_ecu

