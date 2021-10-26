from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class BE_Intro_Guesser(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

class BE_Intro_Observer(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Observer'

class BE_Avg_Observer_Sky(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Observer' and self.participant.vars['S_dist'] == 'Sky'

    form_model = 'player'
    form_fields = ['w2_avg_guess_o_0', 'w2_avg_guess_o_1', 'w2_avg_guess_o_2', 'w2_avg_guess_o_3', 'w2_avg_guess_o_4',
                   'w2_avg_guess_o_5', 'w2_avg_guess_o_6', 'w2_avg_guess_o_7', 'w2_avg_guess_o_8', 'w2_avg_guess_o_9',
                   'w2_avg_guess_o_10', 'w2_avg_guess_o_11', 'w2_avg_guess_o_12', 'w2_avg_guess_o_13',
                   'w2_avg_guess_o_14', 'w2_avg_guess_o_15']

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        o_observer_loss = 0
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.w2_avg_guess_o_0 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_1 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_2 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_3 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_4 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_5 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_6 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_7 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_8 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_9 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_10 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_11 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_12 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_13 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_14 = round(random.uniform(5,10),2)
            p.w2_avg_guess_o_15 = round(random.uniform(5,10),2)

            print("<Time Out on Page:'BE_Avg_Observer_Sky'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_avg_guess_o_0, p.w2_avg_guess_o_1, p.w2_avg_guess_o_2, p.w2_avg_guess_o_3, p.w2_avg_guess_o_4,
                  p.w2_avg_guess_o_5, p.w2_avg_guess_o_6, p.w2_avg_guess_o_7, p.w2_avg_guess_o_8, p.w2_avg_guess_o_9,
                  p.w2_avg_guess_o_10, p.w2_avg_guess_o_11, p.w2_avg_guess_o_12, p.w2_avg_guess_o_13,
                  p.w2_avg_guess_o_14, p.w2_avg_guess_o_15)

        ############################## AVERAGES ##############################

        if Constants.w2_prvs_avg_guess_o_0 - 0.05 <= p.w2_avg_guess_o_0 <= Constants.w2_prvs_avg_guess_o_0 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_1 - 0.05 <= p.w2_avg_guess_o_1 <= Constants.w2_prvs_avg_guess_o_1 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_2 - 0.05 <= p.w2_avg_guess_o_2 <= Constants.w2_prvs_avg_guess_o_2 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_3 - 0.05 <= p.w2_avg_guess_o_3 <= Constants.w2_prvs_avg_guess_o_3 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_4 - 0.05 <= p.w2_avg_guess_o_4 <= Constants.w2_prvs_avg_guess_o_4 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_5 - 0.05 <= p.w2_avg_guess_o_5 <= Constants.w2_prvs_avg_guess_o_5 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_6 - 0.05 <= p.w2_avg_guess_o_6 <= Constants.w2_prvs_avg_guess_o_6 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_7 - 0.05 <= p.w2_avg_guess_o_7 <= Constants.w2_prvs_avg_guess_o_7 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_8 - 0.05 <= p.w2_avg_guess_o_8 <= Constants.w2_prvs_avg_guess_o_8 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_9 - 0.05 <= p.w2_avg_guess_o_9 <= Constants.w2_prvs_avg_guess_o_9 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_10 - 0.05 <= p.w2_avg_guess_o_10 <= Constants.w2_prvs_avg_guess_o_10 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_11 - 0.05 <= p.w2_avg_guess_o_11 <= Constants.w2_prvs_avg_guess_o_11 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_12 - 0.05 <= p.w2_avg_guess_o_12 <= Constants.w2_prvs_avg_guess_o_12 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_13 - 0.05 <= p.w2_avg_guess_o_13 <= Constants.w2_prvs_avg_guess_o_13 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_14 - 0.05 <= p.w2_avg_guess_o_14 <= Constants.w2_prvs_avg_guess_o_14 + 0.05:
            pass
        else:
            o_observer_loss += 1

        if Constants.w2_prvs_avg_guess_o_15 - 0.05 <= p.w2_avg_guess_o_15 <= Constants.w2_prvs_avg_guess_o_15 + 0.05:
            pass
        else:
            o_observer_loss += 1

        be_p = 2 - Constants.dollar_per_ecu_observer * o_observer_loss

        if be_p < 0:
            p.payoff = 0
        else:
            p.payoff = be_p


class BE_Avg_Guesser_Sky(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

    form_model = 'player'
    form_fields = ['w2_avg_s_n_o_1_5', 'w2_avg_s_n_o_6_9', 'w2_avg_s_n_o_10_14']

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.w2_avg_s_n_o_1_5 = round(random.uniform(5,10),2)
            p.w2_avg_s_n_o_6_9 = round(random.uniform(5,10),2)
            p.w2_avg_s_n_o_10_14 = round(random.uniform(5,10),2)

            print("<Time Out on Page:'BE_Avg_Guesser_Sky'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_avg_s_n_o_1_5, p.w2_avg_s_n_o_6_9, p.w2_avg_s_n_o_10_14)


class BE_Avg_Msg_Sky(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

    form_model = 'player'
    form_fields = ['w2_avg_msg_o']
    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        guesser_loss = 0
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.w2_avg_msg_o = round(random.uniform(0,15),2)

            print("<Time Out on Page:'BE_Avg_Msg_Sky'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_avg_msg_o)

        ############################## AVERAGES ##############################
        # Sky Secret Number
        if Constants.w2_prvs_avg_s_n_o_1_5 - 0.05 <= p.w2_avg_s_n_o_1_5 <= Constants.w2_prvs_avg_s_n_o_1_5 + 0.05:
            pass
        else:
            guesser_loss += 1

        if Constants.w2_prvs_avg_s_n_o_6_9 - 0.05 <= p.w2_avg_s_n_o_6_9 <= Constants.w2_prvs_avg_s_n_o_6_9 + 0.05:
            pass
        else:
            guesser_loss += 1

        if Constants.w2_prvs_avg_s_n_o_10_14 - 0.05 <= p.w2_avg_s_n_o_10_14 <= Constants.w2_prvs_avg_s_n_o_10_14 + 0.05:
            pass
        else:
            guesser_loss += 1

        ############################## MESSAGES ##############################
        # Sky Message
        if Constants.w2_prvs_avg_msg_o - 0.05 <= p.w2_avg_msg_o <= Constants.w2_prvs_avg_msg_o + 0.05:
            pass
        else:
            guesser_loss += 1

        be_p = 2 - Constants.dollar_per_ecu_guesser * guesser_loss

        if be_p < 0:
            p.payoff = 0
        else:
            p.payoff = be_p

class BE_Results(Page):
    def vars_for_template(self):
        return{
            'belief_payoff': self.player.payoff
        }

    def before_next_page(self):
        self.participant.vars['belief_payoff'] = self.player.payoff


page_sequence = [BE_Intro_Guesser,
                 BE_Intro_Observer,
                 BE_Avg_Observer_Sky,
                 BE_Avg_Guesser_Sky,
                 BE_Avg_Msg_Sky,
                 BE_Results
                 ]