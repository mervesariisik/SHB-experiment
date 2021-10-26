from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class WaitforResearcher(Page):
    def is_displayed(self):
        return self.round_number == 1

class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1


class SHB_Instructions1(Page):
    def is_displayed(self):
        return self.round_number == 1


class SHB_Instructions2(Page):
    def is_displayed(self):
        return self.round_number == 1


class SHB_Instructions3(Page):
    def is_displayed(self):
        return self.round_number == 1


class SHB_Instructions4(Page):
    def is_displayed(self):
        return self.round_number == 1


class SHB_Instructions5(Page):
    def is_displayed(self):
        return self.round_number == 1


class SHB_Instructions6(Page):
    def is_displayed(self):
        return self.round_number == 1


class SHB_Example1_1(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['ex1_s_n_5', 'ex1_s_n_6', 'ex1_s_n_7', 'ex1_s_n_8', 'ex1_s_n_9', 'ex1_s_n_10']

    def error_message(self, values):
        if values['ex1_s_n_5'] is False or values['ex1_s_n_6'] is False or values['ex1_s_n_7'] is False or \
                values['ex1_s_n_8'] is False or values['ex1_s_n_9'] is False or values['ex1_s_n_10'] is False:
            return "The selected set of secret numbers is wrong! Please check again, remember to use " \
                   "the table."

class SHB_Example1_2(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['ex1_observer_pref', 'ex1_guesser_pref']

    # def ex2_observer_p_error_message(self, value):
    # if value != -33:
    # return "Observer's payoff is wrong!"

    def error_message(self, values):
        if values['ex1_observer_pref'] is True and values['ex1_guesser_pref'] is False:
            return "Both answers are wrong! Remember the Observer earns more when GUESS is higher and the Guesser " \
                   "earns more when the GUESS is closer to the secret number. (You can also use the payoff tables " \
                   "below)"
        elif values['ex1_observer_pref'] is True:
            return "You've picked the wrong answer for the Observer! Remember the Observer earns more when GUESS is " \
                   "higher. (You can also use the payoff table below)"
        elif values['ex1_guesser_pref'] is False:
            return "You've picked the wrong answer for the Guesser! Remember the Guesser earns more when the GUESS " \
                   "is closer to the secret number. (You can also use the payoff table below)."


class SHB_Example2_1(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['ex2_s_n_5', 'ex2_s_n_6', 'ex2_s_n_7', 'ex2_s_n_8', 'ex2_s_n_9', 'ex2_s_n_10']

    def error_message(self, values):
        if values['ex2_s_n_5'] is False or values['ex2_s_n_6'] is False or values['ex2_s_n_7'] is False or \
                values['ex2_s_n_8'] is True or values['ex2_s_n_9'] is True or values['ex2_s_n_10'] is True:
            return "The selected set of secret numbers is wrong! Please check again, remember to use " \
                   "the table."


class SHB_Example2_2(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['ex2_observer_p', 'ex2_guesser_p']

    def error_message(self, values):
        if values['ex2_guesser_p'] != 104 and values['ex2_observer_p'] != 23:
            return "Both payoffs are wrong! Remember to use the payoff tables."
        elif values['ex2_observer_p'] != 23:
            return "Observer's payoff is wrong! Remember to use the payoff table."
        elif values['ex2_guesser_p'] != 104:
            return "Guesser's payoff is wrong! Remember to use the payoff table."


class SHB_Example3_1(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['ex3_s_n_5', 'ex3_s_n_6', 'ex3_s_n_7', 'ex3_s_n_8', 'ex3_s_n_9', 'ex3_s_n_10']

    def error_message(self, values):
        if values['ex3_s_n_5'] is True or values['ex3_s_n_6'] is True or values['ex3_s_n_7'] is True or \
                values['ex3_s_n_8'] is True or values['ex3_s_n_9'] is False or values['ex3_s_n_10'] is False:
            return "The selected set of secret numbers is wrong! Please check again, remember to use " \
                   "the table."


class SHB_Example3_2(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['ex3_observer_p', 'ex3_guesser_p']

    def error_message(self, values):
        if values['ex3_observer_p'] != 110 and values['ex3_guesser_p'] != 110:
            return "Both payoffs are wrong! Remember to use the payoff tables."
        if values['ex3_observer_p'] != 110:
            return "Observer's payoff is wrong! Remember to use the payoff table."
        elif values['ex3_guesser_p'] != 110:
            return "Guesser's payoff is wrong! Remember to use the payoff table."


class LetsStart(Page):
    def is_displayed(self):
        return self.round_number == 1


class StartWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    wait_for_all_groups = True
    title_text = 'Please Wait'
    body_text = 'Waiting for other participants to finish going through the examples.'


class Observer(Page):
    def is_displayed(self):
        return self.player.role == 'Observer'

    timer_text = 'Time left to proceed to next round:'

    def get_timeout_seconds(self):
        if self.round_number <= 10:
            return 150
        elif self.round_number >= 11:
            return 90


class Guesser_Decision(Page):
    def is_displayed(self):
        return self.player.role == 'Guesser'

    form_model = 'group'
    form_fields = ['R_guess']

    def get_timeout_seconds(self):
        if self.round_number <= 10:
            return 120
        elif self.round_number >= 11:
            return 60

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened: # we use "timeout_happened" to decide what value gets submitted on user's behalf
            random_guess = random.randint(1,11)
            # if the player fails to submit the page on time...
            if random_guess == 1:
                p.group.R_guess = 5
            elif random_guess == 2:
                p.group.R_guess = 5.5
            elif random_guess == 3:
                p.group.R_guess = 6
            elif random_guess == 4:
                p.group.R_guess = 6.5
            elif random_guess == 5:
                p.group.R_guess = 7
            elif random_guess == 6:
                p.group.R_guess = 7.5
            elif random_guess == 7:
                p.group.R_guess = 8
            elif random_guess == 8:
                p.group.R_guess = 8.5
            elif random_guess == 9:
                p.group.R_guess = 9
            elif random_guess == 10:
                p.group.R_guess = 9.5
            elif random_guess == 11:
                p.group.R_guess = 10

            print("<Time Out on Page:'Guesser_Decision'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "round number:", self.round_number,
                  "automated random answer:", p.group.R_guess)


class SHB_1stRoundResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    after_all_players_arrive = 'set_round_payoffs'

    title_text = 'Please Wait for the other Participant'
    body_text = "The participant you are matched with hasn't proceeded yet."


class SHB_RoundResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number != 1
    after_all_players_arrive = 'set_round_payoffs'

    title_text = 'Please Wait for the other Participant'
    body_text = "Note that waiting briefly between rounds is normal as " \
                "you are randomly matched with participants each round. The participant you are matched with may be " \
                "finishing a previous round or may have not yet progressed on this round."


class SHB_FinalResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    after_all_players_arrive = 'set_final_payoffs'


class SHB_Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return{
            'total_point_payoff_guesser': int(self.participant.payoff / Constants.dollar_per_ecu_guesser),
            'total_point_payoff_observer': int(self.participant.payoff / Constants.dollar_per_ecu_observer)
        }

    def before_next_page(self):
        self.participant.vars['shb_role'] = self.player.role
        self.participant.vars['shb_payoff'] = self.participant.payoff


page_sequence = [Welcome,
                 SHB_Instructions1,
                 SHB_Instructions2,
                 SHB_Instructions3,
                 SHB_Instructions4,
                 SHB_Instructions5,
                 SHB_Instructions6,
                 SHB_Example1_1,
                 SHB_Example1_2,
                 SHB_Example2_1,
                 SHB_Example2_2,
                 SHB_Example3_1,
                 SHB_Example3_2,
                 LetsStart,
                 StartWaitPage,
                 Observer,
                 Guesser_Decision,
                 SHB_1stRoundResultsWaitPage,
                 SHB_RoundResultsWaitPage,
                 SHB_FinalResultsWaitPage,
                 SHB_Results]
