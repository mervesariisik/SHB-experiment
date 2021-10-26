from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    def before_next_page(self):
        sesh = self.session
        # nbr_players = sesh.num_participants
        p = self.player
        attendance = []
        for p in self.subsession.get_players():
            if p.participant.label is not None:
                print("this is participant label:", p.participant.label)
                p.in_session = True
                # if p.in_session:
                attendance.append(p.id_in_group)
        print("attendance list:", attendance)
        nbr_players = len(attendance)
        print("nbr_players:", nbr_players)

        if nbr_players >= 20:
            print("in 'nbr_players >= 20'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 6, 11, 16]:
                    room_p = 1
                elif p.id_in_group in [2, 7, 12, 17]:
                    room_p = 2
                elif p.id_in_group in [3, 8, 13, 18]:
                    room_p = 3
                elif p.id_in_group in [4, 9, 14, 19]:
                    room_p = 4
                elif p.id_in_group in [5, 10, 15, 20]:
                    room_p = 5
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        elif 20 > nbr_players >= 16:
            print("in '20 > nbr_players >= 16'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 5, 9, 13]:
                    room_p = 1
                elif p.id_in_group in [2, 6, 10, 14]:
                    room_p = 2
                elif p.id_in_group in [3, 7, 11, 15]:
                    room_p = 3
                elif p.id_in_group in [4, 8, 12, 16]:
                    room_p = 4
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        elif 16 > nbr_players >= 12:
            print("in '16 > nbr_players >= 12'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 4, 7, 10]:
                    room_p = 1
                elif p.id_in_group in [2, 5, 8, 11]:
                    room_p = 2
                elif p.id_in_group in [3, 6, 9, 12]:
                    room_p = 3
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        elif 12 > nbr_players >= 8:
            print("in '12 > nbr_players >= 8'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 3, 5, 7]:
                    room_p = 1
                elif p.id_in_group in [2, 4, 6, 8]:
                    room_p = 2
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        elif 8 > nbr_players >= 4:
            print("in '8 > nbr_players >= 4' ")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 2, 3, 4]:
                    room_p = 1
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        else:
            print("in '4 > nbr_players'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)


class EntryToZoom(Page):
    def is_displayed(self):
        return self.player.room_organizer == 1 or self.player.room_organizer == 2 or self.player.room_organizer == 3 or \
               self.player.room_organizer == 4 or self.player.room_organizer == 5

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        # z_link = ""
        for key in Zoom_dict:
            if key == p_id:
                z_link = Zoom_dict[key]
                print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return dict(
            zoom_link=z_link
        )

    def vars_for_template(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        z_link = Zoom_dict[p_id]
        # for key in Zoom_dict:
        # if key == p_id:
        # z_link = Zoom_dict[key]
        # print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return {
            'zoom_link': z_link
        }


class EntryToZoomNew(Page):
    def is_displayed(self):
        return self.player.participant.label is not None

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        # z_link = ""
        for key in Zoom_dict:
            if key == p_id:
                z_link = Zoom_dict[key]
                print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return dict(
            zoom_link=z_link
        )

    def vars_for_template(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        z_link = Zoom_dict[p_id]
        # for key in Zoom_dict:
        # if key == p_id:
        # z_link = Zoom_dict[key]
        # print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return {
            'zoom_link': z_link
        }

    def before_next_page(self):
        sesh = self.session
        # nbr_players = sesh.num_participants
        p = self.player
        attendance = []
        for p in self.subsession.get_players():
            if p.participant.label is not None:
                print("this is participant label:", p.participant.label)
                p.in_session = True
                # if p.in_session:
                attendance.append(p.id_in_group)
        print("attendance list:", attendance)
        nbr_players = len(attendance)
        print("nbr_players:", nbr_players)

        if nbr_players >= 20:
            print("in 'nbr_players >= 20'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 6, 11, 16]:
                    room_p = 1
                elif p.id_in_group in [2, 7, 12, 17]:
                    room_p = 2
                elif p.id_in_group in [3, 8, 13, 18]:
                    room_p = 3
                elif p.id_in_group in [4, 9, 14, 19]:
                    room_p = 4
                elif p.id_in_group in [5, 10, 15, 20]:
                    room_p = 5
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        elif 20 > nbr_players >= 16:
            print("in '20 > nbr_players >= 16'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 5, 9, 13]:
                    room_p = 1
                elif p.id_in_group in [2, 6, 10, 14]:
                    room_p = 2
                elif p.id_in_group in [3, 7, 11, 15]:
                    room_p = 3
                elif p.id_in_group in [4, 8, 12, 16]:
                    room_p = 4
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        elif 16 > nbr_players >= 12:
            print("in '16 > nbr_players >= 12'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 4, 7, 10]:
                    room_p = 1
                elif p.id_in_group in [2, 5, 8, 11]:
                    room_p = 2
                elif p.id_in_group in [3, 6, 9, 12]:
                    room_p = 3
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        elif 12 > nbr_players >= 8:
            print("in '12 > nbr_players >= 8'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 3, 5, 7]:
                    room_p = 1
                elif p.id_in_group in [2, 4, 6, 8]:
                    room_p = 2
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        elif 8 > nbr_players >= 4:
            print("in '8 > nbr_players >= 4' ")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                if p.id_in_group in [1, 2, 3, 4]:
                    room_p = 1
                else:
                    room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)
        else:
            print("in '4 > nbr_players'")
            for p in self.subsession.get_players():
                print("this is p:", p)
                print("this is p.id_in_group:", p.id_in_group)
                room_p = 0
                p.room_organizer = room_p
                print("this is p.room_organizer:", p.room_organizer)


class NoShowEntryPage(Page):
    def is_displayed(self):
        return self.participant.label is None


class ExperimentRedirectR1New(Page):
    def is_displayed(self):
        return self.player.participant.label is not None and self.player.room_organizer == 1

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class ExperimentRedirectR2New(Page):
    def is_displayed(self):
        return self.player.participant.label is not None and self.player.room_organizer == 2

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class ExperimentRedirectR3New(Page):
    def is_displayed(self):
        return self.player.participant.label is not None and self.player.room_organizer == 3

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class ExperimentRedirectR4New(Page):
    def is_displayed(self):
        return self.player.participant.label is not None and self.player.room_organizer == 4

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class ExperimentRedirectR5New(Page):
    def is_displayed(self):
        return self.player.participant.label is not None and self.player.room_organizer == 5

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class QuotaNew(Page):
    def is_displayed(self):
        return self.player.participant.label is not None and self.player.room_organizer == 0

    #def before_next_page(self):
        #order = 0
        #extras = []
        #player = self.player
        #for p in self.subsession.get_players():
            #if p.participant.label is not None and self.player.room_organizer == 0:
                #extras.append(p.id_in_group)
                #order = extras.index(p.id_in_group) + 1
            #player.extras_order = order
            #print("this is extras list:", extras, "this is extras.index(p):", extras.index(p.id_in_group))


class QuotaMinus1ToZoomNew(Page):
    def is_displayed(self):
        return self.player.participant.label is not None and self.player.extras_order == 1

# class TestPage(Page):
# form_model = 'player'
# form_fields = ['R_guess']

class Quota(Page):
    def is_displayed(self):
        return self.player.room_organizer == 0

    def before_next_page(self):
        extras = []
        player = self.player
        for p in self.subsession.get_players():
            order = 0
            print("this is p in self.subsession.get_players():", p)
            if p.room_organizer == 0 and p.participant.label is not None:
                extras.append(p.id_in_group)
                print("this is extras list:", extras, "this is extras.index(p):", extras.index(p.id_in_group))
                order = extras.index(p.id_in_group) + 1
            p.extras_order = order
            print("p.id_in_group:", p.id_in_group, "p.extras_order:", p.extras_order)
            # player.extras_order == order


class QuotaMinus1ToZoom(Page):
    def is_displayed(self):
        return self.player.extras_order == 1

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        # z_link = ""
        for key in Zoom_dict:
            if key == p_id:
                z_link = Zoom_dict[key]
                print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return dict(
            zoom_link=z_link
        )

    def vars_for_template(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        z_link = Zoom_dict[p_id]
        # for key in Zoom_dict:
        # if key == p_id:
        # z_link = Zoom_dict[key]
        # print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return {
            'zoom_link': z_link
        }


class QuotaDup1(Page):
    def is_displayed(self):
        return self.player.extras_order != 1 and self.player.room_organizer == 0


class QuotaMinus2ToZoom(Page):
    def is_displayed(self):
        return self.player.extras_order == 2

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        # z_link = ""
        for key in Zoom_dict:
            if key == p_id:
                z_link = Zoom_dict[key]
                print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return dict(
            zoom_link=z_link
        )

    def vars_for_template(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        z_link = Zoom_dict[p_id]
        # for key in Zoom_dict:
        # if key == p_id:
        # z_link = Zoom_dict[key]
        # print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return {
            'zoom_link': z_link
        }


class QuotaDup2(Page):
    def is_displayed(self):
        return self.player.extras_order != 1 and self.player.extras_order != 2 and self.player.room_organizer == 0


class QuotaMinus3ToZoom(Page):
    def is_displayed(self):
        return self.player.extras_order == 3

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        # z_link = ""
        for key in Zoom_dict:
            if key == p_id:
                z_link = Zoom_dict[key]
                print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return dict(
            zoom_link=z_link
        )

    def vars_for_template(self):
        player = self.player
        p_id = player.participant.label
        Zoom_dict = {self.session.config['Prolific_ID_1']: self.session.config['ZOOM_Regis_Link_1'],
                     self.session.config['Prolific_ID_2']: self.session.config['ZOOM_Regis_Link_2'],
                     self.session.config['Prolific_ID_3']: self.session.config['ZOOM_Regis_Link_3'],
                     self.session.config['Prolific_ID_4']: self.session.config['ZOOM_Regis_Link_4'],
                     self.session.config['Prolific_ID_5']: self.session.config['ZOOM_Regis_Link_5'],
                     self.session.config['Prolific_ID_6']: self.session.config['ZOOM_Regis_Link_6'],
                     self.session.config['Prolific_ID_7']: self.session.config['ZOOM_Regis_Link_7'],
                     self.session.config['Prolific_ID_8']: self.session.config['ZOOM_Regis_Link_8'],
                     self.session.config['Prolific_ID_9']: self.session.config['ZOOM_Regis_Link_9'],
                     self.session.config['Prolific_ID_10']: self.session.config['ZOOM_Regis_Link_10'],
                     self.session.config['Prolific_ID_11']: self.session.config['ZOOM_Regis_Link_11'],
                     self.session.config['Prolific_ID_12']: self.session.config['ZOOM_Regis_Link_12'],
                     self.session.config['Prolific_ID_13']: self.session.config['ZOOM_Regis_Link_13'],
                     self.session.config['Prolific_ID_14']: self.session.config['ZOOM_Regis_Link_14'],
                     self.session.config['Prolific_ID_15']: self.session.config['ZOOM_Regis_Link_15'],
                     self.session.config['Prolific_ID_16']: self.session.config['ZOOM_Regis_Link_16'],
                     self.session.config['Prolific_ID_17']: self.session.config['ZOOM_Regis_Link_17'],
                     self.session.config['Prolific_ID_18']: self.session.config['ZOOM_Regis_Link_18'],
                     self.session.config['Prolific_ID_19']: self.session.config['ZOOM_Regis_Link_19'],
                     self.session.config['Prolific_ID_20']: self.session.config['ZOOM_Regis_Link_20'],
                     self.session.config['Prolific_ID_21']: self.session.config['ZOOM_Regis_Link_21'],
                     self.session.config['Prolific_ID_22']: self.session.config['ZOOM_Regis_Link_22'],
                     self.session.config['Prolific_ID_23']: self.session.config['ZOOM_Regis_Link_23'],
                     self.session.config['Prolific_ID_24']: self.session.config['ZOOM_Regis_Link_24'],
                     self.session.config['Prolific_ID_25']: self.session.config['ZOOM_Regis_Link_25'],
                     self.session.config['Prolific_ID_26']: self.session.config['ZOOM_Regis_Link_26'],
                     self.session.config['Prolific_ID_27']: self.session.config['ZOOM_Regis_Link_27'],
                     self.session.config['Prolific_ID_28']: self.session.config['ZOOM_Regis_Link_28'],
                     self.session.config['Prolific_ID_29']: self.session.config['ZOOM_Regis_Link_29'],
                     self.session.config['Prolific_ID_30']: self.session.config['ZOOM_Regis_Link_30'],
                     self.session.config['Prolific_ID_31']: self.session.config['ZOOM_Regis_Link_31'],
                     self.session.config['Prolific_ID_32']: self.session.config['ZOOM_Regis_Link_32'],
                     self.session.config['Prolific_ID_33']: self.session.config['ZOOM_Regis_Link_33'],
                     }

        z_link = Zoom_dict[p_id]
        # for key in Zoom_dict:
        # if key == p_id:
        # z_link = Zoom_dict[key]
        # print("Zoom_dict[key]:", Zoom_dict[key], "z_link:", z_link)
        return {
            'zoom_link': z_link
        }


class QuotaDup3(Page):
    def is_displayed(self):
        return self.player.extras_order != 1 and self.player.extras_order != 2 and self.player.extras_order != 3 and \
               self.player.room_organizer == 0


class ExperimentRedirectR1(Page):
    def is_displayed(self):
        return self.player.room_organizer == 1

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class ExperimentRedirectR2(Page):
    def is_displayed(self):
        return self.player.room_organizer == 2

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class ExperimentRedirectR3(Page):
    def is_displayed(self):
        return self.player.room_organizer == 3

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class ExperimentRedirectR4(Page):
    def is_displayed(self):
        return self.player.room_organizer == 4

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


class ExperimentRedirectR5(Page):
    def is_displayed(self):
        return self.player.room_organizer == 5

    def js_vars(self):
        player = self.player
        p_id = player.participant.label
        return dict(
            prolific_id=p_id
        )


page_sequence = [EntryToZoomNew,
                 NoShowEntryPage,
                 QuotaNew,
                 ExperimentRedirectR1New,
                 ExperimentRedirectR2New,
                 ExperimentRedirectR3New,
                 ExperimentRedirectR4New,
                 ExperimentRedirectR5New
                 #Welcome,
                 #EntryToZoom,
                 # TestPage,
                 #Quota,
                 #ExperimentRedirectR1,
                 #ExperimentRedirectR2,
                 #ExperimentRedirectR3,
                 #ExperimentRedirectR4,
                 #ExperimentRedirectR5,
                 #QuotaMinus1ToZoom,
                 #QuotaDup1,
                 #QuotaMinus2ToZoom,
                 #QuotaDup2,
                 #QuotaMinus3ToZoom,
                 #QuotaDup3
                 ]
