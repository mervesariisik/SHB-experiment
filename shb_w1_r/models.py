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
TREATMENT: W1.right (Mandatory Disclosure, Right Skewed Error)
APP: Mandatory Disclosure Game
"""


class Constants(BaseConstants):
    name_in_url = 'shb_w1_r'
    players_per_group = 2
    num_rounds = 15
    K = 0.5
    types = [5, 6, 7, 8, 9, 10]
    errors = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    K_inv = (1 - K) / (len(errors) - 1)
    role_sender = 'Observer'
    role_receiver = 'Guesser'
    # session_seed = 5

    dollar_per_ecu_observer = 1/250
    dollar_per_ecu_guesser = 1/430

class Subsession(BaseSubsession):
    def creating_session(self):
        # setting seed per session to have the type and error selection replicable across treatments
        import random
        if self.round_number == 1:
            random.seed(self.session.config['session_seed'])
            print("session seed", self.session.config['session_seed'])
            self.session.vars['random_state'] = random.getstate()
            print("Session random state:", self.session.vars['random_state'])

            # dividing senders (observers) into two groups
            for p in self.get_players():
                if p.participant.id_in_session in list(range(1, self.session.num_participants + 1, 2)):
                    p.participant.vars['S_dist'] = 'Sky'
                    print("player", p, "is", p.role, "id_in_session is:", p.participant.id_in_session, "S_dist is",
                          p.participant.vars['S_dist'])

        # grouping players randomly each round, keeping roles fixed
        self.group_randomly(fixed_id_in_group=True)

        # each group is assigned a different type and error term each round
        for g in self.get_groups():
            g.S_type = random.choice(Constants.types)
            sender_of_group = g.get_player_by_id(1)
            g.S_dist = sender_of_group.participant.vars['S_dist']
            right_error = random.choices(Constants.errors, cum_weights=(Constants.K, Constants.K + Constants.K_inv,
                                                                        Constants.K + 2 * Constants.K_inv,
                                                                        Constants.K + 3 * Constants.K_inv,
                                                                        Constants.K + 4 * Constants.K_inv,
                                                                        Constants.K + 5 * Constants.K_inv,
                                                                        Constants.K + 6 * Constants.K_inv,
                                                                        Constants.K + 7 * Constants.K_inv,
                                                                        Constants.K + 8 * Constants.K_inv,
                                                                        Constants.K + 9 * Constants.K_inv,
                                                                        Constants.K + 10 * Constants.K_inv), k=1)[0]
            # random.choices creates a list, indexing it to extract an integer value
            g.S_error = right_error
            g.S_signal = g.S_type + g.S_error


class Group(BaseGroup):
    S_type = models.IntegerField()
    S_error = models.IntegerField()
    S_signal = models.IntegerField()
    S_dist = models.StringField()
    S_disclose = models.BooleanField(
        initial=True
    )

    def S_disclose_choices(self):
        import random
        choices = [
            [True, "Yes, I want to send the message."],
            [False, "No, I don't want to send the message."]
        ]
        random.shuffle(choices)
        return choices

    R_guess = models.FloatField(
        label="",
        choices=[5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10],
        widget=widgets.RadioSelect
    )

    def set_round_payoffs(self):
        s_p = round(110 - 15 * abs(10 - self.R_guess) ** 1.4)
        r_p = round(110 - 15 * abs(self.S_type - self.R_guess) ** 1.4)
        for p in self.get_players():
            if p.role == 'Observer':
                p.shb_round_points = s_p
                p.payoff = s_p * Constants.dollar_per_ecu_observer
                print("participant id in sesh:", p.participant.id_in_session, "round:", self.round_number,
                      "sender points:", s_p, "sender earning:", p.payoff)
            elif p.role == 'Guesser':
                p.shb_round_points = r_p
                p.payoff = r_p * Constants.dollar_per_ecu_guesser
                print("participant id in sesh:", p.participant.id_in_session, "round:", self.round_number,
                      "receiver points:", r_p, "receiver earning:", p.payoff)

    def set_final_payoffs(self):
        for p in self.get_players():
            print("participant id in sesh:", p.participant.id_in_session, "participant's payoff initial",
                  p.participant.payoff)
            if p.participant.payoff < 0:
                p.participant.payoff = 0
            else:
                pass
            print("participant id in sesh:", p.participant.id_in_session, "participant's payoff final",
                  p.participant.payoff)


class Player(BasePlayer):
# example 1
    ex1_msg = models.IntegerField(
        min=0, max=15,
        label='What is the Message?'
    )
    ex1_s_n_5 = models.BooleanField(
        label="5",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex1_s_n_6 = models.BooleanField(
        label="6",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex1_s_n_7 = models.BooleanField(
        label="7",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex1_s_n_8 = models.BooleanField(
        label="8",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex1_s_n_9 = models.BooleanField(
        label="9",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex1_s_n_10 = models.BooleanField(
        label="10",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex1_observer_p = models.IntegerField(
        label="What is Observer's payoff? (Scroll down for payoff table)"
    )
    ex1_guesser_p = models.IntegerField(
        label="What is Guesser's payoff? (Scroll down for payoff table)"
    )

    ex1_observer_pref = models.BooleanField(
        label="Which would give the Observer a higher payoff?",
        choices=[
            [True, "GUESS 8.5"],
            [False, "GUESS 9"]
        ],
        widget=widgets.RadioSelect
    )

    ex1_guesser_pref = models.BooleanField(
        label="Which would give the Guesser a higher payoff?",
        choices=[
            [True, "GUESS 8.5"],
            [False, "GUESS 9"]
        ],
        widget=widgets.RadioSelect
    )

# example 2
    ex2_msg = models.IntegerField(
        min=0, max=15,
        label='What is the Message?'
    )
    ex2_s_n_5 = models.BooleanField(
        label="5",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex2_s_n_6 = models.BooleanField(
        label="6",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex2_s_n_7 = models.BooleanField(
        label="7",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex2_s_n_8 = models.BooleanField(
        label="8",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex2_s_n_9 = models.BooleanField(
        label="9",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex2_s_n_10 = models.BooleanField(
        label="10",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex2_observer_p = models.IntegerField(
        label="What is Observer's payoff? (Scroll down for payoff table)"
    )
    ex2_guesser_p = models.IntegerField(
        label="What is Guesser's payoff? (Scroll down for payoff table)"
    )

# example 3
    ex3_msg = models.IntegerField(
        min=0, max=15,
        label='What is the Message?'
    )
    ex3_s_n_5 = models.BooleanField(
        label="5",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex3_s_n_6 = models.BooleanField(
        label="6",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex3_s_n_7 = models.BooleanField(
        label="7",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex3_s_n_8 = models.BooleanField(
        label="8",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex3_s_n_9 = models.BooleanField(
        label="9",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex3_s_n_10 = models.BooleanField(
        label="10",
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    ex3_observer_p = models.IntegerField(
        label="What is Observer's payoff? (Scroll down for payoff table)"
    )
    ex3_guesser_p = models.IntegerField(
        label="What is Guesser's payoff? (Scroll down for payoff table)"
    )

    shb_round_points = models.IntegerField()