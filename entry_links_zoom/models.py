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
This is the study posted on Prolific to collect Prolific IDs.
Gives participants their Zoom unique link (pre-registered)
and
Redirects them to the Main Session Rooms

Version 2 (groups/distributes across rooms w.r.t. my attendance entries)

Note: Admin (participant_label=merve) should be accounted for when
selecting the number of participants in the session (+1)
"""


class Constants(BaseConstants):
    name_in_url = 'entry_links_zoom'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    p1 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p2 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p3 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p4 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p5 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p6 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p7 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p8 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p9 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p10 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p11 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p12 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p13 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p14 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p15 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p16 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p17 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p18 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p19 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p20 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p21 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p22 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p23 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p24 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p25 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p26 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p27 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p28 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p29 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p30 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p31 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p32 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p33 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    p34 = models.BooleanField(
        initial=False,
        choices=[
            [True, "yes"],
            [False, "no"]
        ],
        widget=widgets.RadioSelectHorizontal
    )


class Player(BasePlayer):
    in_session = models.BooleanField(
        initial=False
    ) # probably don't need this, the loop can simply depend on p1, p2, p3, ..., p20

    room_organizer = models.IntegerField(
        initial=0
    )

