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
APP: Holt Laury Risk Elicitation (Risk Aversion)
"""


class Constants(BaseConstants):
    name_in_url = 'lottery'
    players_per_group = None
    num_rounds = 1
    dollar_per_ecu = 0.05


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    d1 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d2 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d3 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d4 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d5 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d6 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d7 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d8 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d9 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d10 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d11 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d12 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d13 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d14 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    d15 = models.IntegerField(
        blank=True,
        choices=[
            [1, "Lottery"],
            [2, "Fixed Payoff"]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    picked_d = models.IntegerField()
    decision = models.IntegerField()

    def set_payoff(self):
        import random
        self.picked_d = random.randint(1, 15)
        print("Computer picked decision:", self.picked_d)
        if self.picked_d == 1:
            d = self.d1
        elif self.picked_d == 2:
            d = self.d2
        elif self.picked_d == 3:
            d = self.d3
        elif self.picked_d == 4:
            d = self.d4
        elif self.picked_d == 5:
            d = self.d5
        elif self.picked_d == 6:
            d = self.d6
        elif self.picked_d == 7:
            d = self.d7
        elif self.picked_d == 8:
            d = self.d8
        elif self.picked_d == 9:
            d = self.d9
        elif self.picked_d == 10:
            d = self.d10
        elif self.picked_d == 11:
            d = self.d11
        elif self.picked_d == 12:
            d = self.d12
        elif self.picked_d == 13:
            d = self.d13
        elif self.picked_d == 14:
            d = self.d14
        elif self.picked_d == 15:
            d = self.d15
        self.decision = d

        if d == 1:
            coin_toss = random.randint(1, 100)
            print("Lottery coin toss", coin_toss)
            if coin_toss <= 50:
                self.payoff = 40 * Constants.dollar_per_ecu
            elif coin_toss >= 51:
                self.payoff = 0 * Constants.dollar_per_ecu
        else:
            self.payoff = self.picked_d * 2.5 * Constants.dollar_per_ecu

        # self.participant.payoff = self.payoff + self.participant.vars['game1_payoff']
        self.participant.vars['holt_payoff'] = self.payoff
