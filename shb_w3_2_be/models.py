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
TREATMENT: W3.2 (Voluntary Disclosure, Right & Left Skewed Error)
APP: Belief Elicitation
"""


class Constants(BaseConstants):
    name_in_url = 'shb_w3_2_be'
    players_per_group = None
    num_rounds = 1

    dollar_per_ecu_observer = 0.08  # = $2/27 = 0.074
    dollar_per_ecu_guesser = 0.1  # = $2/20 = 0.1


# PREVIOUS SESSION TRUE PERCENTAGES FOR ND
# for PURPLE/FOREST SENDERS (Purple ND "GUESS" Percentages)
    w2_prvs_guess_perc_p_ND_5 = 7
    w2_prvs_guess_perc_p_ND_55 = 0
    w2_prvs_guess_perc_p_ND_6 = 3
    w2_prvs_guess_perc_p_ND_65 = 10
    w2_prvs_guess_perc_p_ND_7 = 10
    w2_prvs_guess_perc_p_ND_75 = 40
    w2_prvs_guess_perc_p_ND_8 = 10
    w2_prvs_guess_perc_p_ND_85 = 10
    w2_prvs_guess_perc_p_ND_9 = 3
    w2_prvs_guess_perc_p_ND_95 = 7
    w2_prvs_guess_perc_p_ND_10 = 0

# for ORANGE/SKY SENDERS (Orange ND "GUESS" Percentages)
    w2_prvs_guess_perc_o_ND_5 = 13
    w2_prvs_guess_perc_o_ND_55 = 5
    w2_prvs_guess_perc_o_ND_6 = 11
    w2_prvs_guess_perc_o_ND_65 = 5
    w2_prvs_guess_perc_o_ND_7 = 13
    w2_prvs_guess_perc_o_ND_75 = 37
    w2_prvs_guess_perc_o_ND_8 = 5
    w2_prvs_guess_perc_o_ND_85 = 5
    w2_prvs_guess_perc_o_ND_9 = 5
    w2_prvs_guess_perc_o_ND_95 = 0
    w2_prvs_guess_perc_o_ND_10 = 0

# for RECEIVERS - PURPLE/FOREST (Purple/Forest ND "SECRET NUMBER" Percentages)
    w2_prvs_s_n_perc_p_ND_5 = 20
    w2_prvs_s_n_perc_p_ND_6 = 25
    w2_prvs_s_n_perc_p_ND_7 = 10
    w2_prvs_s_n_perc_p_ND_8 = 15
    w2_prvs_s_n_perc_p_ND_9 = 20
    w2_prvs_s_n_perc_p_ND_10 = 10

# for RECEIVERS - ORANGE/SKY (Orange/Sky ND "SECRET NUMBER" Percentages)
    w2_prvs_s_n_perc_o_ND_5 = 19
    w2_prvs_s_n_perc_o_ND_6 = 29
    w2_prvs_s_n_perc_o_ND_7 = 26
    w2_prvs_s_n_perc_o_ND_8 = 7
    w2_prvs_s_n_perc_o_ND_9 = 2
    w2_prvs_s_n_perc_o_ND_10 = 17

############################################################################
# PREVIOUS SESSION TRUE PERCENTAGES FOR AVERAGES
# for PURPLE/FOREST SENDERS (Purple "GUESS" Averages)
    w2_prvs_avg_guess_p_0 = 5
    w2_prvs_avg_guess_p_1 = 6
    w2_prvs_avg_guess_p_2 = 5
    w2_prvs_avg_guess_p_3 = 6.67
    w2_prvs_avg_guess_p_4 = 7
    w2_prvs_avg_guess_p_5 = 5.5
    w2_prvs_avg_guess_p_6 = 6
    w2_prvs_avg_guess_p_7 = 7.5
    w2_prvs_avg_guess_p_8 = 6.93
    w2_prvs_avg_guess_p_9 = 5
    w2_prvs_avg_guess_p_10 = 6.1
    w2_prvs_avg_guess_p_11 = 7.1
    w2_prvs_avg_guess_p_12 = 7.43
    w2_prvs_avg_guess_p_13 = 8.92
    w2_prvs_avg_guess_p_14 = 9.57
    w2_prvs_avg_guess_p_15 = 10

# for ORANGE/SKY SENDERS (Orange "GUESS" Averages)
    w2_prvs_avg_guess_o_0 = 5
    w2_prvs_avg_guess_o_1 = 6
    w2_prvs_avg_guess_o_2 = 6.36
    w2_prvs_avg_guess_o_3 = 6.96
    w2_prvs_avg_guess_o_4 = 7.1
    w2_prvs_avg_guess_o_5 = 7.4
    w2_prvs_avg_guess_o_6 = 7.5
    w2_prvs_avg_guess_o_7 = 5
    w2_prvs_avg_guess_o_8 = 7
    w2_prvs_avg_guess_o_9 = 8
    w2_prvs_avg_guess_o_10 = 10
    w2_prvs_avg_guess_o_11 = 8.33
    w2_prvs_avg_guess_o_12 = 8.5
    w2_prvs_avg_guess_o_13 = 9
    w2_prvs_avg_guess_o_14 = 9.38
    w2_prvs_avg_guess_o_15 = 9.8

# for RECEIVERS - PURPLE/FOREST (Purple/Forest "SECRET NUMBER" Averages)
    w2_prvs_avg_s_n_p_1_5 = 6.83
    w2_prvs_avg_s_n_p_6_9 = 7.71
    w2_prvs_avg_s_n_p_10_14 = 7.59

# for RECEIVERS - ORANGE/SKY (Orange/Sky "SECRET NUMBER" Averages)
    w2_prvs_avg_s_n_o_1_5 = 7.58
    w2_prvs_avg_s_n_o_6_9 = 6.73
    w2_prvs_avg_s_n_o_10_14 = 8.2

# for RECEIVERS - PURPLE/FOREST PREVIOUS SESSION TRU AVG MESSAGE
    w2_prvs_avg_msg_p = 10

# for RECEIVERS - ORANGE/SKY PREVIOUS SESSION TRU AVG MESSAGE
    w2_prvs_avg_msg_o = 5.4

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
## PURPLE/FOREST SENDERS
# Purple/Forest Sender: ND
    w2_guess_perc_p_ND_5 = models.IntegerField(
        label="5:"
    )
    w2_guess_perc_p_ND_55 = models.IntegerField(
        label="5.5:"
    )
    w2_guess_perc_p_ND_6 = models.IntegerField(
        label="6:"
    )
    w2_guess_perc_p_ND_65 = models.IntegerField(
        label="6.5:"
    )
    w2_guess_perc_p_ND_7 = models.IntegerField(
        label="7:"
    )
    w2_guess_perc_p_ND_75 = models.IntegerField(
        label="7.5:"
    )
    w2_guess_perc_p_ND_8 = models.IntegerField(
        label="8:"
    )
    w2_guess_perc_p_ND_85 = models.IntegerField(
        label="8.5:"
    )
    w2_guess_perc_p_ND_9 = models.IntegerField(
        label="9:"
    )
    w2_guess_perc_p_ND_95 = models.IntegerField(
        label="9.5:"
    )
    w2_guess_perc_p_ND_10 = models.IntegerField(
        label="10:"
    )
    w2_guess_perc_p_ND_leftover = models.IntegerField(
        initial=100,
        label="Percentage left to allocate:"
    )

# Purple/Forest Sender: Avg guess per message
    w2_avg_guess_p_0 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_1 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_2 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_3 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_4 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_5 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_6 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_7 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_8 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_9 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_10 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_11 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_12 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_13 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_14 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_p_15 = models.FloatField(
        min=5, max=10,
        label=""
    )

## ORANGE/SKY SENDERS

# Orange/Sky Sender: ND
    w2_guess_perc_o_ND_5 = models.IntegerField(
        label="5:"
    )
    w2_guess_perc_o_ND_55 = models.IntegerField(
        label="5.5:"
    )
    w2_guess_perc_o_ND_6 = models.IntegerField(
        label="6:"
    )
    w2_guess_perc_o_ND_65 = models.IntegerField(
        label="6.5:"
    )
    w2_guess_perc_o_ND_7 = models.IntegerField(
        label="7:"
    )
    w2_guess_perc_o_ND_75 = models.IntegerField(
        label="7.5:"
    )
    w2_guess_perc_o_ND_8 = models.IntegerField(
        label="8:"
    )
    w2_guess_perc_o_ND_85 = models.IntegerField(
        label="8.5:"
    )
    w2_guess_perc_o_ND_9 = models.IntegerField(
        label="9:"
    )
    w2_guess_perc_o_ND_95 = models.IntegerField(
        label="9.5:"
    )
    w2_guess_perc_o_ND_10 = models.IntegerField(
        label="10:"
    )
    w2_guess_perc_o_ND_leftover = models.IntegerField(
        initial=100,
        label="Percentage left to allocate:"
    )

# Orange/Sky Senders: Avg guess per message
    w2_avg_guess_o_0 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_1 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_2 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_3 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_4 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_5 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_6 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_7 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_8 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_9 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_10 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_11 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_12 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_13 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_14 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_guess_o_15 = models.FloatField(
        min=5, max=10,
        label=""
    )

## RECEIVERS:
# Receivers: Purple/Forest ND
    w2_s_n_perc_p_ND_5 = models.IntegerField(
        label="5:"
    )

    w2_s_n_perc_p_ND_6 = models.IntegerField(
        label="6:"
    )

    w2_s_n_perc_p_ND_7 = models.IntegerField(
        label="7:"
    )

    w2_s_n_perc_p_ND_8 = models.IntegerField(
        label="8:"
    )

    w2_s_n_perc_p_ND_9 = models.IntegerField(
        label="9:"
    )

    w2_s_n_perc_p_ND_10 = models.IntegerField(
        label="10:"
    )
    w2_s_n_perc_p_ND_leftover = models.IntegerField(
        initial=100,
        label="Percentage left to allocate:"
    )

# Receivers Orange/Sky ND
    w2_s_n_perc_o_ND_5 = models.IntegerField(
        label="5:"
    )

    w2_s_n_perc_o_ND_6 = models.IntegerField(
        label="6:"
    )

    w2_s_n_perc_o_ND_7 = models.IntegerField(
        label="7:"
    )

    w2_s_n_perc_o_ND_8 = models.IntegerField(
        label="8:"
    )

    w2_s_n_perc_o_ND_9 = models.IntegerField(
        label="9:"
    )

    w2_s_n_perc_o_ND_10 = models.IntegerField(
        label="10:"
    )
    w2_s_n_perc_o_ND_leftover = models.IntegerField(
        initial=100,
        label="Percentage left to allocate:"
    )

# Receivers: Avg secret nbr per Purple/Forest Message
    w2_avg_s_n_p_1_5 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_s_n_p_6_9 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_s_n_p_10_14 = models.FloatField(
        min=5, max=10,
        label=""
    )

# Receivers: Avg secret number per Orange/Sky Message
    w2_avg_s_n_o_1_5 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_s_n_o_6_9 = models.FloatField(
        min=5, max=10,
        label=""
    )
    w2_avg_s_n_o_10_14 = models.FloatField(
        min=5, max=10,
        label=""
    )

# Receivers: Avg message Purple/Forest
    w2_avg_msg_p = models.FloatField(
        min=0, max=15,
        label=""
    )

# Receivers: Avg message Orange/Sky
    w2_avg_msg_o = models.FloatField(
        min=0, max=15,
        label=""
    )