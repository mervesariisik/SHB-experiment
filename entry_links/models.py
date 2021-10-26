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

Version 1 (groups/distributes across rooms w.r.t. id in session)
"""


class Constants(BaseConstants):
    name_in_url = 'entry_links'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    room_organizer = models.IntegerField()
    R_guess = models.FloatField(
        label="",
        choices=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        widget=widgets.RadioSelect
    )
    extras_order = models.IntegerField(
        initial=0
    )
    in_session = models.BooleanField(
        initial=False
    )
