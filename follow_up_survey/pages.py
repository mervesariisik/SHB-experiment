from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Last_Part_Intro(Page):
    pass

class Last_Part_Experiment_Results(Page):
    def vars_for_template(self):
        return{
            'shb_payoff': self.player.participant.vars['shb_payoff'] + self.player.participant.vars['belief_payoff'],
            'lottery_payoff': self.player.participant.vars['lottery_payoff'],
            'crt_payoff': self.player.participant.vars['crt_payoff'],
            'total_payoff': self.player.participant.payoff_plus_participation_fee()
        }


class Last_Part_Questions(Page):
    form_model = 'player'
    form_fields = ['age', 'gender_radio', 'english_first','ethnicity_radio', 'race_radio', 'educ_level']

#class Last_Part_Payment_Questions(Page):
    #form_model = 'player'
    #form_fields = ['amazon', 'name', 'e_mail', 'country', 'state', 'city',  'zipcode', 'address1', 'address2']

    #def before_next_page(self):
        #p = self.player
        #p.payment = p.participant.payoff_plus_participation_fee()

class Last_Part_Feedback(Page):
    form_model = 'player'
    form_fields = ['instructions', 'color_reading', 'shb_length', 'belief_length', 'experiment_length', 'open_feedback']

class Last_Part_Thank_You(Page):
    pass

class RedirectProlific(Page):
    def js_vars(self):
        comp_url = self.session.config['Completion_URL']
        return dict(
            prolific_redirect=comp_url
        )



page_sequence = [Last_Part_Intro,
                 Last_Part_Experiment_Results,
                 Last_Part_Questions,
                 Last_Part_Feedback,
                 #Last_Part_Payment_Questions,
                 Last_Part_Thank_You,
                 RedirectProlific
                 ]

