from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class BE_Intro_Guesser(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

class BE_Intro_Observer(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Observer'

class BE_ND_Observer_Sky(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Observer' and self.participant.vars['S_dist'] == 'Sky'

    form_model = 'player'
    form_fields = ['w2_guess_perc_o_ND_leftover', 'w2_guess_perc_o_ND_5', 'w2_guess_perc_o_ND_55',
                   'w2_guess_perc_o_ND_6', 'w2_guess_perc_o_ND_65', 'w2_guess_perc_o_ND_7', 'w2_guess_perc_o_ND_75',
                   'w2_guess_perc_o_ND_8', 'w2_guess_perc_o_ND_85', 'w2_guess_perc_o_ND_9', 'w2_guess_perc_o_ND_95',
                   'w2_guess_perc_o_ND_10']

    def error_message(self, values):
        if values['w2_guess_perc_o_ND_5'] + values['w2_guess_perc_o_ND_55'] + values['w2_guess_perc_o_ND_6'] + \
                values['w2_guess_perc_o_ND_65'] + values['w2_guess_perc_o_ND_7'] + values['w2_guess_perc_o_ND_75'] + \
                values['w2_guess_perc_o_ND_8'] + values['w2_guess_perc_o_ND_85'] + values['w2_guess_perc_o_ND_9'] + \
                values['w2_guess_perc_o_ND_95'] + values['w2_guess_perc_o_ND_10'] > 100:
            return "Please try again. Your percentage entries cannot exceed 100."
        elif values['w2_guess_perc_o_ND_5'] + values['w2_guess_perc_o_ND_55'] + values['w2_guess_perc_o_ND_6'] + \
                values['w2_guess_perc_o_ND_65'] + values['w2_guess_perc_o_ND_7'] + values['w2_guess_perc_o_ND_75'] + \
                values['w2_guess_perc_o_ND_8'] + values['w2_guess_perc_o_ND_85'] + values['w2_guess_perc_o_ND_9'] + \
                values['w2_guess_perc_o_ND_95'] + values['w2_guess_perc_o_ND_10'] < 100:
            return "Please try again. Your percentage entries must add up to 100."

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            # generating random 11 random numbers that sum up to 100
            # https://math.stackexchange.com/questions/1276206/method-of-generating-random-numbers-that-sum-to-100-is-this-truly-random
            # https://en.wikipedia.org/wiki/Stars_and_bars_%28combinatorics%29
            # https://stackoverflow.com/questions/42999093/generate-random-number-in-range-excluding-some-numbers
            random1 = random.randint(1,110)
            random2 = random.choice([i for i in range(1,110) if i not in [random1]])
            random3 = random.choice([i for i in range(1, 110) if i not in [random1, random2]])
            random4 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3]])
            random5 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4]])
            random6 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5]])
            random7 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5, random6]])
            random8 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5, random6, random7]])
            random9 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5, random6, random7, random8]])
            random10 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5, random6, random7, random8,
                                                                            random9]])

            randoms = [random1, random2, random3, random4, random5, random6, random7, random8, random9, random10]
            randoms.sort()

            p.w2_guess_perc_o_ND_5 = randoms[0] - 1
            p.w2_guess_perc_o_ND_55 = randoms[1] - randoms[0] - 1
            p.w2_guess_perc_o_ND_6 = randoms[2] - randoms[1] - 1
            p.w2_guess_perc_o_ND_65 = randoms[3] - randoms[2] - 1
            p.w2_guess_perc_o_ND_7 = randoms[4] - randoms[3] - 1
            p.w2_guess_perc_o_ND_75 = randoms[5] - randoms[4] - 1
            p.w2_guess_perc_o_ND_8 = randoms[6] - randoms[5] - 1
            p.w2_guess_perc_o_ND_85 = randoms[7] - randoms[6] - 1
            p.w2_guess_perc_o_ND_9 = randoms[8] - randoms[7] - 1
            p.w2_guess_perc_o_ND_95 = randoms[9] - randoms[8] - 1
            p.w2_guess_perc_o_ND_10 = 110 - randoms[9]

            print("<Time Out on Page:'BE_ND_Observer_Sky'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                   p.w2_guess_perc_o_ND_5, p.w2_guess_perc_o_ND_55, p.w2_guess_perc_o_ND_6, p.w2_guess_perc_o_ND_65,
                   p.w2_guess_perc_o_ND_7, p.w2_guess_perc_o_ND_75, p.w2_guess_perc_o_ND_8, p.w2_guess_perc_o_ND_85,
                   p.w2_guess_perc_o_ND_9, p.w2_guess_perc_o_ND_95, p.w2_guess_perc_o_ND_10)


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

        if p.w2_guess_perc_o_ND_5 in range(Constants.w2_prvs_guess_perc_o_ND_5 - 5,
                                           Constants.w2_prvs_guess_perc_o_ND_5 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_55 in range(Constants.w2_prvs_guess_perc_o_ND_55 - 5,
                                            Constants.w2_prvs_guess_perc_o_ND_55 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_6 in range(Constants.w2_prvs_guess_perc_o_ND_6 - 5,
                                           Constants.w2_prvs_guess_perc_o_ND_6 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_65 in range(Constants.w2_prvs_guess_perc_o_ND_65 - 5,
                                            Constants.w2_prvs_guess_perc_o_ND_65 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_7 in range(Constants.w2_prvs_guess_perc_o_ND_7 - 5,
                                           Constants.w2_prvs_guess_perc_o_ND_7 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_75 in range(Constants.w2_prvs_guess_perc_o_ND_75 - 5,
                                            Constants.w2_prvs_guess_perc_o_ND_75 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_8 in range(Constants.w2_prvs_guess_perc_o_ND_8 - 5,
                                           Constants.w2_prvs_guess_perc_o_ND_8 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_85 in range(Constants.w2_prvs_guess_perc_o_ND_85 - 5,
                                            Constants.w2_prvs_guess_perc_o_ND_85 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_9 in range(Constants.w2_prvs_guess_perc_o_ND_9 - 5,
                                           Constants.w2_prvs_guess_perc_o_ND_9 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_95 in range(Constants.w2_prvs_guess_perc_o_ND_95 - 5,
                                            Constants.w2_prvs_guess_perc_o_ND_95 + 6):
            pass
        else:
            o_observer_loss += 1

        if p.w2_guess_perc_o_ND_10 in range(Constants.w2_prvs_guess_perc_o_ND_10 - 5,
                                            Constants.w2_prvs_guess_perc_o_ND_10 + 6):
            pass
        else:
            o_observer_loss += 1

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

class BE_ND_Observer_Forest(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Observer' and self.participant.vars['S_dist'] == 'Forest'

    form_model = 'player'
    form_fields = ['w2_guess_perc_p_ND_leftover', 'w2_guess_perc_p_ND_5', 'w2_guess_perc_p_ND_55',
                   'w2_guess_perc_p_ND_6', 'w2_guess_perc_p_ND_65', 'w2_guess_perc_p_ND_7', 'w2_guess_perc_p_ND_75',
                   'w2_guess_perc_p_ND_8', 'w2_guess_perc_p_ND_85', 'w2_guess_perc_p_ND_9', 'w2_guess_perc_p_ND_95',
                   'w2_guess_perc_p_ND_10']

    def error_message(self, values):
        if values['w2_guess_perc_p_ND_5'] + values['w2_guess_perc_p_ND_55'] + values['w2_guess_perc_p_ND_6'] + \
                values['w2_guess_perc_p_ND_65'] + values['w2_guess_perc_p_ND_7'] + values['w2_guess_perc_p_ND_75'] + \
                values['w2_guess_perc_p_ND_8'] + values['w2_guess_perc_p_ND_85'] + values['w2_guess_perc_p_ND_9'] + \
                values['w2_guess_perc_p_ND_95'] + values['w2_guess_perc_p_ND_10'] > 100:
            return "Please try again. Your percentage entries cannot exceed 100."
        elif values['w2_guess_perc_p_ND_5'] + values['w2_guess_perc_p_ND_55'] + values['w2_guess_perc_p_ND_6'] + \
                values['w2_guess_perc_p_ND_65'] + values['w2_guess_perc_p_ND_7'] + values['w2_guess_perc_p_ND_75'] + \
                values['w2_guess_perc_p_ND_8'] + values['w2_guess_perc_p_ND_85'] + values['w2_guess_perc_p_ND_9'] + \
                values['w2_guess_perc_p_ND_95'] + values['w2_guess_perc_p_ND_10'] < 100:
            return "Please try again. Your percentage entries must add up to 100."

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            # generating random 11 random numbers that sum up to 100
            # https://math.stackexchange.com/questions/1276206/method-of-generating-random-numbers-that-sum-to-100-is-this-truly-random
            # https://en.wikipedia.org/wiki/Stars_and_bars_%28combinatorics%29
            # https://stackoverflow.com/questions/42999093/generate-random-number-in-range-excluding-some-numbers
            random1 = random.randint(1, 110)
            random2 = random.choice([i for i in range(1, 110) if i not in [random1]])
            random3 = random.choice([i for i in range(1, 110) if i not in [random1, random2]])
            random4 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3]])
            random5 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4]])
            random6 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5]])
            random7 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5, random6]])
            random8 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5, random6, random7]])
            random9 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                           random5, random6, random7, random8]])
            random10 = random.choice([i for i in range(1, 110) if i not in [random1, random2, random3, random4,
                                                                            random5, random6, random7, random8,
                                                                            random9]])

            randoms = [random1, random2, random3, random4, random5, random6, random7, random8, random9, random10]
            randoms.sort()

            p.w2_guess_perc_p_ND_5 = randoms[0] - 1
            p.w2_guess_perc_p_ND_55 = randoms[1] - randoms[0] - 1
            p.w2_guess_perc_p_ND_6 = randoms[2] - randoms[1] - 1
            p.w2_guess_perc_p_ND_65 = randoms[3] - randoms[2] - 1
            p.w2_guess_perc_p_ND_7 = randoms[4] - randoms[3] - 1
            p.w2_guess_perc_p_ND_75 = randoms[5] - randoms[4] - 1
            p.w2_guess_perc_p_ND_8 = randoms[6] - randoms[5] - 1
            p.w2_guess_perc_p_ND_85 = randoms[7] - randoms[6] - 1
            p.w2_guess_perc_p_ND_9 = randoms[8] - randoms[7] - 1
            p.w2_guess_perc_p_ND_95 = randoms[9] - randoms[8] - 1
            p.w2_guess_perc_p_ND_10 = 110 - randoms[9]

            print("<Time Out on Page:'BE_ND_Observer_Forest'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_guess_perc_p_ND_5, p.w2_guess_perc_p_ND_55, p.w2_guess_perc_p_ND_6, p.w2_guess_perc_p_ND_65,
                  p.w2_guess_perc_p_ND_7, p.w2_guess_perc_p_ND_75, p.w2_guess_perc_p_ND_8, p.w2_guess_perc_p_ND_85,
                  p.w2_guess_perc_p_ND_9, p.w2_guess_perc_p_ND_95, p.w2_guess_perc_p_ND_10)

class BE_Avg_Observer_Forest(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Observer' and self.participant.vars['S_dist'] == 'Forest'

    form_model = 'player'
    form_fields = ['w2_avg_guess_p_0', 'w2_avg_guess_p_1', 'w2_avg_guess_p_2', 'w2_avg_guess_p_3', 'w2_avg_guess_p_4',
                   'w2_avg_guess_p_5', 'w2_avg_guess_p_6', 'w2_avg_guess_p_7', 'w2_avg_guess_p_8', 'w2_avg_guess_p_9',
                   'w2_avg_guess_p_10', 'w2_avg_guess_p_11', 'w2_avg_guess_p_12', 'w2_avg_guess_p_13',
                   'w2_avg_guess_p_14', 'w2_avg_guess_p_15']

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        p_observer_loss = 0
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.w2_avg_guess_p_0 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_1 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_2 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_3 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_4 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_5 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_6 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_7 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_8 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_9 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_10 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_11 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_12 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_13 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_14 = round(random.uniform(5,10),2)
            p.w2_avg_guess_p_15 = round(random.uniform(5,10),2)

            print("<Time Out on Page:'BE_Avg_Observer_Forest'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_avg_guess_p_0, p.w2_avg_guess_p_1, p.w2_avg_guess_p_2, p.w2_avg_guess_p_3, p.w2_avg_guess_p_4,
                  p.w2_avg_guess_p_5, p.w2_avg_guess_p_6, p.w2_avg_guess_p_7, p.w2_avg_guess_p_8, p.w2_avg_guess_p_9,
                  p.w2_avg_guess_p_10, p.w2_avg_guess_p_11, p.w2_avg_guess_p_12, p.w2_avg_guess_p_13,
                  p.w2_avg_guess_p_14, p.w2_avg_guess_p_15)

        if p.w2_guess_perc_p_ND_5 in range(Constants.w2_prvs_guess_perc_p_ND_5 - 5,
                                           Constants.w2_prvs_guess_perc_p_ND_5 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_55 in range(Constants.w2_prvs_guess_perc_p_ND_55 - 5,
                                            Constants.w2_prvs_guess_perc_p_ND_55 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_6 in range(Constants.w2_prvs_guess_perc_p_ND_6 - 5,
                                           Constants.w2_prvs_guess_perc_p_ND_6 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_65 in range(Constants.w2_prvs_guess_perc_p_ND_65 - 5,
                                            Constants.w2_prvs_guess_perc_p_ND_65 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_7 in range(Constants.w2_prvs_guess_perc_p_ND_7 - 5,
                                           Constants.w2_prvs_guess_perc_p_ND_7 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_75 in range(Constants.w2_prvs_guess_perc_p_ND_75 - 5,
                                            Constants.w2_prvs_guess_perc_p_ND_75 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_8 in range(Constants.w2_prvs_guess_perc_p_ND_8 - 5,
                                           Constants.w2_prvs_guess_perc_p_ND_8 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_85 in range(Constants.w2_prvs_guess_perc_p_ND_85 - 5,
                                            Constants.w2_prvs_guess_perc_p_ND_85 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_9 in range(Constants.w2_prvs_guess_perc_p_ND_9 - 5,
                                           Constants.w2_prvs_guess_perc_p_ND_9 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_95 in range(Constants.w2_prvs_guess_perc_p_ND_95 - 5,
                                            Constants.w2_prvs_guess_perc_p_ND_95 + 6):
            pass
        else:
            p_observer_loss += 1

        if p.w2_guess_perc_p_ND_10 in range(Constants.w2_prvs_guess_perc_p_ND_10 - 5,
                                            Constants.w2_prvs_guess_perc_p_ND_10 + 6):
            pass
        else:
            p_observer_loss += 1

############################## AVERAGES ##############################

        if Constants.w2_prvs_avg_guess_p_0 - 0.05 <= p.w2_avg_guess_p_0 <= Constants.w2_prvs_avg_guess_p_0 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_1 - 0.05 <= p.w2_avg_guess_p_1 <= Constants.w2_prvs_avg_guess_p_1 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_2 - 0.05 <= p.w2_avg_guess_p_2 <= Constants.w2_prvs_avg_guess_p_2 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_3 - 0.05 <= p.w2_avg_guess_p_3 <= Constants.w2_prvs_avg_guess_p_3 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_4 - 0.05 <= p.w2_avg_guess_p_4 <= Constants.w2_prvs_avg_guess_p_4 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_5 - 0.05 <= p.w2_avg_guess_p_5 <= Constants.w2_prvs_avg_guess_p_5 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_6 - 0.05 <= p.w2_avg_guess_p_6 <= Constants.w2_prvs_avg_guess_p_6 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_7 - 0.05 <= p.w2_avg_guess_p_7 <= Constants.w2_prvs_avg_guess_p_7 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_8 - 0.05 <= p.w2_avg_guess_p_8 <= Constants.w2_prvs_avg_guess_p_8 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_9 - 0.05 <= p.w2_avg_guess_p_9 <= Constants.w2_prvs_avg_guess_p_9 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_10 - 0.05 <= p.w2_avg_guess_p_10 <= Constants.w2_prvs_avg_guess_p_10 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_11 - 0.05 <= p.w2_avg_guess_p_11 <= Constants.w2_prvs_avg_guess_p_11 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_12 - 0.05 <= p.w2_avg_guess_p_12 <= Constants.w2_prvs_avg_guess_p_12 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_13 - 0.05 <= p.w2_avg_guess_p_13 <= Constants.w2_prvs_avg_guess_p_13 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_14 - 0.05 <= p.w2_avg_guess_p_14 <= Constants.w2_prvs_avg_guess_p_14 + 0.05:
            pass
        else:
            p_observer_loss += 1

        if Constants.w2_prvs_avg_guess_p_15 - 0.05 <= p.w2_avg_guess_p_15 <= Constants.w2_prvs_avg_guess_p_15 + 0.05:
            pass
        else:
            p_observer_loss += 1

        be_p = 2 - Constants.dollar_per_ecu_observer * p_observer_loss

        if be_p < 0:
            p.payoff = 0
        else:
            p.payoff = be_p

class BE_ND_Guesser_Sky(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

    form_model = 'player'
    form_fields = ['w2_s_n_perc_o_ND_leftover', 'w2_s_n_perc_o_ND_5', 'w2_s_n_perc_o_ND_6', 'w2_s_n_perc_o_ND_7',
                   'w2_s_n_perc_o_ND_8', 'w2_s_n_perc_o_ND_9', 'w2_s_n_perc_o_ND_10']

    def error_message(self, values):
        if values['w2_s_n_perc_o_ND_5'] + values['w2_s_n_perc_o_ND_6'] +  values['w2_s_n_perc_o_ND_7'] + \
                values['w2_s_n_perc_o_ND_8'] + values['w2_s_n_perc_o_ND_9'] +  values['w2_s_n_perc_o_ND_10'] > 100:
            return "Please try again. Your percentage entries cannot exceed 100."
        elif values['w2_s_n_perc_o_ND_5'] + values['w2_s_n_perc_o_ND_6'] +  values['w2_s_n_perc_o_ND_7'] + \
                values['w2_s_n_perc_o_ND_8'] + values['w2_s_n_perc_o_ND_9'] +  values['w2_s_n_perc_o_ND_10'] < 100:
            return "Please try again. Your percentage entries must add up to 100."
        if values['w2_s_n_perc_o_ND_5'] is None or values['w2_s_n_perc_o_ND_6'] is None or \
                values['w2_s_n_perc_o_ND_7'] is None or values['w2_s_n_perc_o_ND_8'] is None or \
                values['w2_s_n_perc_o_ND_9'] is None or values['w2_s_n_perc_o_ND_10'] is None:
            return "Please enter enter a percentage for every secret number. Your entries can be any value including and between 0 and 100. "

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            # generating random 11 random numbers that sum up to 100
            # https://math.stackexchange.com/questions/1276206/method-of-generating-random-numbers-that-sum-to-100-is-this-truly-random
            # https://en.wikipedia.org/wiki/Stars_and_bars_%28combinatorics%29
            # https://stackoverflow.com/questions/42999093/generate-random-number-in-range-excluding-some-numbers
            random1 = random.randint(1, 105)
            random2 = random.choice([i for i in range(1, 105) if i not in [random1]])
            random3 = random.choice([i for i in range(1, 105) if i not in [random1, random2]])
            random4 = random.choice([i for i in range(1, 105) if i not in [random1, random2, random3]])
            random5 = random.choice([i for i in range(1, 105) if i not in [random1, random2, random3, random4]])

            randoms = [random1, random2, random3, random4, random5]
            randoms.sort()

            p.w2_s_n_perc_o_ND_5 = randoms[0] - 1
            p.w2_s_n_perc_o_ND_6 = randoms[1] - randoms[0] - 1
            p.w2_s_n_perc_o_ND_7 = randoms[2] - randoms[1] - 1
            p.w2_s_n_perc_o_ND_8 = randoms[3] - randoms[2] - 1
            p.w2_s_n_perc_o_ND_9 = randoms[4] - randoms[3] - 1
            p.w2_s_n_perc_o_ND_10 = 105 - randoms[4]

            print("<Time Out on Page:'BE_ND_Guesser_Sky'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_s_n_perc_o_ND_5, p.w2_s_n_perc_o_ND_6, p.w2_s_n_perc_o_ND_7, p.w2_s_n_perc_o_ND_8,
                  p.w2_s_n_perc_o_ND_9, p.w2_s_n_perc_o_ND_10)

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

class BE_ND_Guesser_Forest(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

    form_model = 'player'
    form_fields = ['w2_s_n_perc_p_ND_leftover', 'w2_s_n_perc_p_ND_5', 'w2_s_n_perc_p_ND_6', 'w2_s_n_perc_p_ND_7',
                   'w2_s_n_perc_p_ND_8', 'w2_s_n_perc_p_ND_9', 'w2_s_n_perc_p_ND_10']

    def error_message(self, values):
        if values['w2_s_n_perc_p_ND_5'] + values['w2_s_n_perc_p_ND_6'] + values['w2_s_n_perc_p_ND_7'] + \
                values['w2_s_n_perc_p_ND_8'] + values['w2_s_n_perc_p_ND_9'] + values['w2_s_n_perc_p_ND_10'] > 100:
            return "Please try again. Your percentage entries cannot exceed 100."
        elif values['w2_s_n_perc_p_ND_5'] + values['w2_s_n_perc_p_ND_6'] + values['w2_s_n_perc_p_ND_7'] + \
                values['w2_s_n_perc_p_ND_8'] + values['w2_s_n_perc_p_ND_9'] + values['w2_s_n_perc_p_ND_10'] < 100:
            return "Please try again. Your percentage entries must add up to 100."

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            # generating random 11 random numbers that sum up to 100
            # https://math.stackexchange.com/questions/1276206/method-of-generating-random-numbers-that-sum-to-100-is-this-truly-random
            # https://en.wikipedia.org/wiki/Stars_and_bars_%28combinatorics%29
            # https://stackoverflow.com/questions/42999093/generate-random-number-in-range-excluding-some-numbers
            random1 = random.randint(1, 105)
            random2 = random.choice([i for i in range(1, 105) if i not in [random1]])
            random3 = random.choice([i for i in range(1, 105) if i not in [random1, random2]])
            random4 = random.choice([i for i in range(1, 105) if i not in [random1, random2, random3]])
            random5 = random.choice([i for i in range(1, 105) if i not in [random1, random2, random3, random4]])

            randoms = [random1, random2, random3, random4, random5]
            randoms.sort()

            p.w2_s_n_perc_p_ND_5 = randoms[0] - 1
            p.w2_s_n_perc_p_ND_6 = randoms[1] - randoms[0] - 1
            p.w2_s_n_perc_p_ND_7 = randoms[2] - randoms[1] - 1
            p.w2_s_n_perc_p_ND_8 = randoms[3] - randoms[2] - 1
            p.w2_s_n_perc_p_ND_9 = randoms[4] - randoms[3] - 1
            p.w2_s_n_perc_p_ND_10 = 105 - randoms[4]

            print("<Time Out on Page:'BE_ND_Guesser_Forest'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_s_n_perc_p_ND_5, p.w2_s_n_perc_p_ND_6, p.w2_s_n_perc_p_ND_7, p.w2_s_n_perc_p_ND_8,
                  p.w2_s_n_perc_p_ND_9, p.w2_s_n_perc_p_ND_10)

class BE_Avg_Guesser_Forest(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

    form_model = 'player'
    form_fields = ['w2_avg_s_n_p_1_5', 'w2_avg_s_n_p_6_9', 'w2_avg_s_n_p_10_14']

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        guesser_loss = 0
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.w2_avg_s_n_p_1_5 = round(random.uniform(5,10),2)
            p.w2_avg_s_n_p_6_9 = round(random.uniform(5,10),2)
            p.w2_avg_s_n_p_10_14 = round(random.uniform(5,10),2)

            print("<Time Out on Page:'BE_Avg_Guesser_Forest'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_avg_s_n_p_1_5, p.w2_avg_s_n_p_6_9, p.w2_avg_s_n_p_10_14)


class BE_Avg_Msg_Sky(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

    form_model = 'player'
    form_fields = ['w2_avg_msg_o']
    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.w2_avg_msg_o = round(random.uniform(0,15),2)

            print("<Time Out on Page:'BE_Avg_Msg_Sky'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_avg_msg_o)


class BE_Avg_Msg_Forest(Page):
    def is_displayed(self):
        return self.participant.vars['shb_role'] == 'Guesser'

    form_model = 'player'
    form_fields = ['w2_avg_msg_p']

    timeout_seconds = 210

    def before_next_page(self):
        p = self.player
        timeout_happened = self.timeout_happened
        guesser_loss = 0
        import random
        if timeout_happened:  # we use "timeout_happened" to decide what value gets submitted on user's behalf
            p.w2_avg_msg_p = round(random.uniform(0, 15), 2)

            print("<Time Out on Page:'BE_Avg_Msg_Forest'>", "participant label:", p.participant.label,
                  "participant id in sesh:", p.participant.id_in_session, "automated random answers:",
                  p.w2_avg_msg_p)

        # Sky Secret Numbers
        if p.w2_s_n_perc_o_ND_5 in range(Constants.w2_prvs_s_n_perc_o_ND_5 - 5,
                                         Constants.w2_prvs_s_n_perc_o_ND_5 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_o_ND_6 in range(Constants.w2_prvs_s_n_perc_o_ND_6 - 5,
                                         Constants.w2_prvs_s_n_perc_o_ND_6 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_o_ND_7 in range(Constants.w2_prvs_s_n_perc_o_ND_7 - 5,
                                         Constants.w2_prvs_s_n_perc_o_ND_7 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_o_ND_8 in range(Constants.w2_prvs_s_n_perc_o_ND_8 - 5,
                                         Constants.w2_prvs_s_n_perc_o_ND_8 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_o_ND_9 in range(Constants.w2_prvs_s_n_perc_o_ND_9 - 5,
                                         Constants.w2_prvs_s_n_perc_o_ND_9 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_o_ND_10 in range(Constants.w2_prvs_s_n_perc_o_ND_10 - 5,
                                          Constants.w2_prvs_s_n_perc_o_ND_10 + 6):
            pass
        else:
            guesser_loss += 1

        # Forest Secret Numbers
        if p.w2_s_n_perc_p_ND_5 in range(Constants.w2_prvs_s_n_perc_p_ND_5 - 5,
                                         Constants.w2_prvs_s_n_perc_p_ND_5 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_p_ND_6 in range(Constants.w2_prvs_s_n_perc_p_ND_6 - 5,
                                         Constants.w2_prvs_s_n_perc_p_ND_6 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_p_ND_7 in range(Constants.w2_prvs_s_n_perc_p_ND_7 - 5,
                                         Constants.w2_prvs_s_n_perc_p_ND_7 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_p_ND_8 in range(Constants.w2_prvs_s_n_perc_p_ND_8 - 5,
                                         Constants.w2_prvs_s_n_perc_p_ND_8 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_p_ND_9 in range(Constants.w2_prvs_s_n_perc_p_ND_9 - 5,
                                         Constants.w2_prvs_s_n_perc_p_ND_9 + 6):
            pass
        else:
            guesser_loss += 1

        if p.w2_s_n_perc_p_ND_10 in range(Constants.w2_prvs_s_n_perc_p_ND_10 - 5,
                                          Constants.w2_prvs_s_n_perc_p_ND_10 + 6):
            pass
        else:
            guesser_loss += 1
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

        # Forest Secret Number
        if Constants.w2_prvs_avg_s_n_p_1_5 - 0.05 <= p.w2_avg_s_n_p_1_5 <= Constants.w2_prvs_avg_s_n_p_1_5 + 0.05:
            pass
        else:
            guesser_loss += 1

        if Constants.w2_prvs_avg_s_n_p_6_9 - 0.05 <= p.w2_avg_s_n_p_6_9 <= Constants.w2_prvs_avg_s_n_p_6_9 + 0.05:
            pass
        else:
            guesser_loss += 1

        if Constants.w2_prvs_avg_s_n_p_10_14 - 0.05 <= p.w2_avg_s_n_p_10_14 <= Constants.w2_prvs_avg_s_n_p_10_14 + 0.05:
            pass
        else:
            guesser_loss += 1

        ############################## MESSAGES ##############################
        # Sky Message
        if Constants.w2_prvs_avg_msg_o - 0.05 <= p.w2_avg_msg_o <= Constants.w2_prvs_avg_msg_o + 0.05:
            pass
        else:
            guesser_loss += 1
        # Forest Message
        if Constants.w2_prvs_avg_msg_p - 0.05 <= p.w2_avg_msg_p <= Constants.w2_prvs_avg_msg_p + 0.05:
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
                 BE_ND_Observer_Sky,
                 BE_Avg_Observer_Sky,
                 BE_ND_Observer_Forest,
                 BE_Avg_Observer_Forest,
                 BE_ND_Guesser_Sky,
                 BE_ND_Guesser_Forest,
                 BE_Avg_Guesser_Sky,
                 BE_Avg_Guesser_Forest,
                 BE_Avg_Msg_Sky,
                 BE_Avg_Msg_Forest,
                 BE_Results
                 ]