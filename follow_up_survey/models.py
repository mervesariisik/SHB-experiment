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
APP: Follow-up Survey (Demographics, Preferred Payment Method, and Contact Information)
"""


class Constants(BaseConstants):
    name_in_url = 'follow_up_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        label="Age"
    )
    gender_radio = models.IntegerField(
        label="Gender",
        choices=[
            [1, "Woman"],
            [2, "Man"],
            [3, "Transgender woman"],
            [4, "Transgender man"],
            [5, "Non-binary"],
            [6, "I prefer not to answer"]],
        widget=widgets.RadioSelect
    )

    english_first = models.IntegerField(
        label="Is English your first language?",
        choices=[[1, "Yes"],
                 [2, "No"],
                 [3, "I prefer not to answer"]
                 ],
        widget=widgets.RadioSelect
    )

    ethnicity_radio = models.IntegerField(
        label="Do you closely identify yourself as having Hispanic, Latino or Spanish origin?",
        choices=[
            [1, "Yes"],
            [2, "No"],
            [3, "I prefer not to answer."]],
        widget=widgets.RadioSelect
    )
    race_radio = models.IntegerField(
        label="How would you best describe yourself?",
        choices=[
            [1, "American Indian or Alaska Native"],
            [2, "Asian or Asian American"],
            [3, "Black or African American"],
            [4, "Native Hawaiian or Other Pacific Islander"],
            [5, "Middle Eastern or North African"],
            [6, "White"],
            [7, "Mixed"],
            [8, "I prefer not to answer"]
        ],
        widget=widgets.RadioSelect

    )

    educ_level = models.IntegerField(
        label="What is the highest degree or "
              "level of school you have completed?",
        choices=[
            [1, "No schooling completed"],
            [2, "Grades 1 through 11"],
            [3, "12th grade -  no diploma"],
            [4, "Regular high school diploma"],
            [5, "GED or alternative credential"],
            [6, "Some college credit, no degree"],
            [7, "1 or more years of college credit, no degree"],
            [8, "Associates degree (for example: AA, AS)"],
            [9, "Bachelor's degree (for example: BA, BS"],
            [10, "Master's degree (for example: MA, MS, MEng, MEd, MSW, MBA"],
            [11, "Professional degree beyond bachelor's degree (for example: MD, DDS, DVM, LLB, JD"],
            [12, "Doctorate degree (for example: PhD, EdD)"],
            [13, "I prefer not to answer"]

        ],
        widget=widgets.RadioSelect
    )

    color_reading = models.BooleanField(
        label='Did you have difficulty reading color group wheels?',
        choices=[[True, "Yes"],
                 [False, "No"]
                 ]
    )

    instructions = models.BooleanField(
        label='Did you have difficulty understanding instructions?',
        choices=[[True, "Yes"],
                 [False, "No"]
        ]
    )



    payment = models.CurrencyField()

    shb_length = models.IntegerField(
        label='What did you think of the length of the "Guessing the Secret Number Game"? (please only consider the total'
              ' rounds played, i.e. do not take into consideration the "End of the Game Questions")',
        choices=[
            [1, "I wouldn't have difficulty playing if there were more rounds"],
            [2, "the length of the game was just right"],
            [3, "it was too long, I got bored/distracted"]],
        widget=widgets.RadioSelect
    )

    belief_length = models.IntegerField(
        label='What did you think of the length of the "End of the Game Questions" (right after "Guessing the Secret '
              'Number Game")?',
        choices=[
            [1, "I wouldn't have difficulty if there were more questions"],
            [2, "the length of the questions was just right"],
            [3, "it was too long, I got bored/distracted"]],
        widget=widgets.RadioSelect
    )

    experiment_length = models.IntegerField(
        label='What did you think of the length of the entire experiment session?',
        choices=[
            [1, "I wouldn't have difficulty if it was longer"],
            [2, "the length of the experiment was just right"],
            [3, "it was too long, I got bored/distracted"]],
        widget=widgets.RadioSelect
    )



    open_feedback = models.LongStringField(
        label="Any other feedback about the experiment. (Put N/A if you don't have any.)"
    )
