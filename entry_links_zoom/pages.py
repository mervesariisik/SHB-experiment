from otree.api import Currency as c, currency_range, BasePlayer
from ._builtin import Page, WaitPage
from .models import Constants


class EntryToZoomNew(Page):
    def is_displayed(self):
        return self.player.participant.label != 'merve' and self.player.participant.label is not None

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


class AdminPage1(Page):
    def is_displayed(self):
        return self.participant.label == "merve"

    def before_next_page(self):
        group = self.group

        #p1_prolific_id = group.get_player_by_id(1).participant.label
        #if p1_prolific_id != 'merve' and p1_prolific_id is not None:
            #group.p1 = True

        #p2_prolific_id = group.get_player_by_id(2).participant.label
        #if p2_prolific_id != 'merve' and p2_prolific_id is not None:
            #group.p2 = True

        #p3_prolific_id = group.get_player_by_id(3).participant.label
        #if p3_prolific_id != 'merve' and p3_prolific_id is not None:
            #group.p3 = True

        #p4_prolific_id = group.get_player_by_id(4).participant.label
        #if p4_prolific_id != 'merve' and p4_prolific_id is not None:
            #group.p4 = True

        #p5_prolific_id = group.get_player_by_id(5).participant.label
        #if p5_prolific_id != 'merve' and p5_prolific_id is not None:
            #group.p5 = True

        #p6_prolific_id = group.get_player_by_id(6).participant.label
        #if p6_prolific_id != 'merve' and p6_prolific_id is not None:
            #group.p6 = True

        #p7_prolific_id = group.get_player_by_id(7).participant.label
        #if p7_prolific_id != 'merve' and p7_prolific_id is not None:
            #group.p7 = True

        #p8_prolific_id = group.get_player_by_id(8).participant.label
        #if p8_prolific_id != 'merve' and p8_prolific_id is not None:
            #group.p8 = True

        #p9_prolific_id = group.get_player_by_id(9).participant.label
        #if p9_prolific_id != 'merve' and p9_prolific_id is not None:
            #group.p9 = True

        #p10_prolific_id = group.get_player_by_id(10).participant.label
        #if p10_prolific_id != 'merve' and p10_prolific_id is not None:
            #group.p10 = True

        #p11_prolific_id = group.get_player_by_id(11).participant.label
        #if p11_prolific_id != 'merve' and p11_prolific_id is not None:
            #group.p11 = True

        #p12_prolific_id = group.get_player_by_id(12).participant.label
        #if p12_prolific_id != 'merve' and p12_prolific_id is not None:
            #group.p12 = True

        #p13_prolific_id = group.get_player_by_id(13).participant.label
        #if p13_prolific_id != 'merve' and p13_prolific_id is not None:
            #group.p13 = True

        #p14_prolific_id = group.get_player_by_id(14).participant.label
        #if p14_prolific_id != 'merve' and p14_prolific_id is not None:
            #group.p14 = True

        #p15_prolific_id = group.get_player_by_id(15).participant.label
        #if p15_prolific_id != 'merve' and p15_prolific_id is not None:
            #group.p15 = True

        #p16_prolific_id = group.get_player_by_id(16).participant.label
        #if p16_prolific_id != 'merve' and p16_prolific_id is not None:
            #group.p16 = True

        #p17_prolific_id = group.get_player_by_id(17).participant.label
        #if p17_prolific_id != 'merve' and p17_prolific_id is not None:
            #group.p17 = True

        #p18_prolific_id = group.get_player_by_id(18).participant.label
        #if p18_prolific_id != 'merve' and p18_prolific_id is not None:
            #group.p18 = True

        #p19_prolific_id = group.get_player_by_id(19).participant.label
        #if p19_prolific_id != 'merve' and p19_prolific_id is not None:
            #group.p19 = True

        #p20_prolific_id = group.get_player_by_id(20).participant.label
        #if p20_prolific_id != 'merve' and p20_prolific_id is not None:
            #group.p20 = True

        #p21_prolific_id = group.get_player_by_id(21).participant.label
        #if p21_prolific_id != 'merve' and p21_prolific_id is not None:
            #group.p21 = True

        #p22_prolific_id = group.get_player_by_id(22).participant.label
        #if p22_prolific_id != 'merve' and p22_prolific_id is not None:
            #group.p22 = True

        #p23_prolific_id = group.get_player_by_id(23).participant.label
        #if p23_prolific_id != 'merve' and p23_prolific_id is not None:
            #group.p23 = True

        #p24_prolific_id = group.get_player_by_id(24).participant.label
        #if p24_prolific_id != 'merve' and p24_prolific_id is not None:
            #group.p24 = True

        #p25_prolific_id = group.get_player_by_id(25).participant.label
        #if p25_prolific_id != 'merve' and p25_prolific_id is not None:
            #group.p25 = True

        #p26_prolific_id = group.get_player_by_id(26).participant.label
        #if p26_prolific_id != 'merve' and p26_prolific_id is not None:
            #group.p26 = True

        #p27_prolific_id = group.get_player_by_id(27).participant.label
        #if p27_prolific_id != 'merve' and p27_prolific_id is not None:
            #group.p27 = True

        #p28_prolific_id = group.get_player_by_id(28).participant.label
        #if p28_prolific_id != 'merve' and p28_prolific_id is not None:
            #group.p28 = True

        #p29_prolific_id = group.get_player_by_id(29).participant.label
        #if p29_prolific_id != 'merve' and p29_prolific_id is not None:
            #group.p29 = True

        #p30_prolific_id = group.get_player_by_id(30).participant.label
        #if p30_prolific_id != 'merve' and p30_prolific_id is not None:
            #group.p30 = True

        #p31_prolific_id = group.get_player_by_id(31).participant.label
        #if p31_prolific_id != 'merve' and p31_prolific_id is not None:
            #group.p31 = True

        #p32_prolific_id = group.get_player_by_id(32).participant.label
        #if p32_prolific_id != 'merve' and p32_prolific_id is not None:
            #group.p32 = True

        #p33_prolific_id = group.get_player_by_id(33).participant.label
        #if p33_prolific_id != 'merve' and p33_prolific_id is not None:
            #group.p33 = True

        #34_prolific_id = group.get_player_by_id(34).participant.label
        #if p34_prolific_id != 'merve' and p34_prolific_id is not None:
            #group.p34 = True


class AdminPage2(Page):
    def is_displayed(self):
        return self.participant.label == "merve"

    form_model = 'group'
    form_fields = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15',
                   'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27', 'p28', 'p29',
                   'p30', 'p31', 'p32', 'p33', 'p34']

    def vars_for_template(self):
        group = self.group

        p1_prolific_id = group.get_player_by_id(1).participant.label
        p2_prolific_id = group.get_player_by_id(2).participant.label
        p3_prolific_id = group.get_player_by_id(3).participant.label
        p4_prolific_id = group.get_player_by_id(4).participant.label
        p5_prolific_id = group.get_player_by_id(5).participant.label
        p6_prolific_id = group.get_player_by_id(6).participant.label
        p7_prolific_id = group.get_player_by_id(7).participant.label
        p8_prolific_id = group.get_player_by_id(8).participant.label
        p9_prolific_id = group.get_player_by_id(9).participant.label
        p10_prolific_id = group.get_player_by_id(10).participant.label
        p11_prolific_id = group.get_player_by_id(11).participant.label
        p12_prolific_id = group.get_player_by_id(12).participant.label
        p13_prolific_id = group.get_player_by_id(13).participant.label
        p14_prolific_id = group.get_player_by_id(14).participant.label
        p15_prolific_id = group.get_player_by_id(15).participant.label
        p16_prolific_id = group.get_player_by_id(16).participant.label
        p17_prolific_id = group.get_player_by_id(17).participant.label
        p18_prolific_id = group.get_player_by_id(18).participant.label
        p19_prolific_id = group.get_player_by_id(19).participant.label
        p20_prolific_id = group.get_player_by_id(20).participant.label
        p21_prolific_id = group.get_player_by_id(21).participant.label
        p22_prolific_id = group.get_player_by_id(22).participant.label
        p23_prolific_id = group.get_player_by_id(23).participant.label
        p24_prolific_id = group.get_player_by_id(24).participant.label
        p25_prolific_id = group.get_player_by_id(25).participant.label
        p26_prolific_id = group.get_player_by_id(26).participant.label
        p27_prolific_id = group.get_player_by_id(27).participant.label
        p28_prolific_id = group.get_player_by_id(28).participant.label
        p29_prolific_id = group.get_player_by_id(29).participant.label
        p30_prolific_id = group.get_player_by_id(30).participant.label
        p31_prolific_id = group.get_player_by_id(31).participant.label
        p32_prolific_id = group.get_player_by_id(32).participant.label
        p33_prolific_id = group.get_player_by_id(33).participant.label
        p34_prolific_id = group.get_player_by_id(34).participant.label

        return{
            'p1_prolific_id': p1_prolific_id,
            'p2_prolific_id': p2_prolific_id,
            'p3_prolific_id': p3_prolific_id,
            'p4_prolific_id': p4_prolific_id,
            'p5_prolific_id': p5_prolific_id,
            'p6_prolific_id': p6_prolific_id,
            'p7_prolific_id': p7_prolific_id,
            'p8_prolific_id': p8_prolific_id,
            'p9_prolific_id': p9_prolific_id,
            'p10_prolific_id': p10_prolific_id,
            'p11_prolific_id': p11_prolific_id,
            'p12_prolific_id': p12_prolific_id,
            'p13_prolific_id': p13_prolific_id,
            'p14_prolific_id': p14_prolific_id,
            'p15_prolific_id': p15_prolific_id,
            'p16_prolific_id': p16_prolific_id,
            'p17_prolific_id': p17_prolific_id,
            'p18_prolific_id': p18_prolific_id,
            'p19_prolific_id': p19_prolific_id,
            'p20_prolific_id': p20_prolific_id,
            'p21_prolific_id': p21_prolific_id,
            'p22_prolific_id': p22_prolific_id,
            'p23_prolific_id': p23_prolific_id,
            'p24_prolific_id': p24_prolific_id,
            'p25_prolific_id': p25_prolific_id,
            'p26_prolific_id': p26_prolific_id,
            'p27_prolific_id': p27_prolific_id,
            'p28_prolific_id': p28_prolific_id,
            'p29_prolific_id': p29_prolific_id,
            'p30_prolific_id': p30_prolific_id,
            'p31_prolific_id': p31_prolific_id,
            'p32_prolific_id': p32_prolific_id,
            'p33_prolific_id': p33_prolific_id,
            'p34_prolific_id': p34_prolific_id,
        }


    def before_next_page(self):
        global p
        import random
        g = self.group
        attendance_in_zoom = [] # if this doesn't work, could use "for p in self.subsession.get_players()" as in
        #version 1 of entry links - need to add a counter and link the counter to each p1, p2, p3, etc field via if conditions tho

        if g.p1 and g.get_player_by_id(1).participant.label is not None and g.get_player_by_id(1).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(1))

        if g.p2 and g.get_player_by_id(2).participant.label is not None and g.get_player_by_id(2).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(2))

        if g.p3 and g.get_player_by_id(3).participant.label is not None and g.get_player_by_id(3).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(3))

        if g.p4 and g.get_player_by_id(4).participant.label is not None and g.get_player_by_id(4).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(4))

        if g.p5 and g.get_player_by_id(5).participant.label is not None and g.get_player_by_id(5).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(5))

        if g.p6 and g.get_player_by_id(6).participant.label is not None and g.get_player_by_id(6).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(6))

        if g.p7 and g.get_player_by_id(7).participant.label is not None and g.get_player_by_id(7).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(7))

        if g.p8 and g.get_player_by_id(8).participant.label is not None and g.get_player_by_id(8).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(8))

        if g.p9 and g.get_player_by_id(9).participant.label is not None and g.get_player_by_id(9).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(9))

        if g.p10 and g.get_player_by_id(10).participant.label is not None and g.get_player_by_id(10).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(10))

        if g.p11 and g.get_player_by_id(11).participant.label is not None and g.get_player_by_id(11).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(11))

        if g.p12 and g.get_player_by_id(12).participant.label is not None and g.get_player_by_id(12).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(12))

        if g.p13 and g.get_player_by_id(13).participant.label is not None and g.get_player_by_id(13).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(13))

        if g.p14 and g.get_player_by_id(14).participant.label is not None and g.get_player_by_id(14).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(14))

        if g.p15 and g.get_player_by_id(15).participant.label is not None and g.get_player_by_id(15).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(15))

        if g.p16 and g.get_player_by_id(16).participant.label is not None and g.get_player_by_id(16).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(16))

        if g.p17 and g.get_player_by_id(17).participant.label is not None and g.get_player_by_id(17).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(17))

        if g.p18 and g.get_player_by_id(18).participant.label is not None and g.get_player_by_id(18).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(18))

        if g.p19 and g.get_player_by_id(19).participant.label is not None and g.get_player_by_id(19).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(19))

        if g.p20 and g.get_player_by_id(20).participant.label is not None and g.get_player_by_id(20).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(20))

        if g.p21 and g.get_player_by_id(21).participant.label is not None and g.get_player_by_id(21).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(21))

        if g.p22 and g.get_player_by_id(22).participant.label is not None and g.get_player_by_id(22).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(22))

        if g.p23 and g.get_player_by_id(23).participant.label is not None and g.get_player_by_id(23).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(23))

        if g.p24 and g.get_player_by_id(24).participant.label is not None and g.get_player_by_id(24).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(24))

        if g.p25 and g.get_player_by_id(25).participant.label is not None and g.get_player_by_id(25).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(25))

        if g.p26 and g.get_player_by_id(26).participant.label is not None and g.get_player_by_id(26).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(26))

        if g.p27 and g.get_player_by_id(27).participant.label is not None and g.get_player_by_id(27).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(27))

        if g.p28 and g.get_player_by_id(28).participant.label is not None and g.get_player_by_id(28).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(28))

        if g.p29 and g.get_player_by_id(29).participant.label is not None and g.get_player_by_id(29).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(29))

        if g.p30 and g.get_player_by_id(30).participant.label is not None and g.get_player_by_id(30).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(30))

        if g.p31 and g.get_player_by_id(31).participant.label is not None and g.get_player_by_id(31).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(31))

        if g.p32 and g.get_player_by_id(32).participant.label is not None and g.get_player_by_id(32).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(32))

        if g.p33 and g.get_player_by_id(33).participant.label is not None and g.get_player_by_id(33).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(33))

        if g.p34 and g.get_player_by_id(34).participant.label is not None and g.get_player_by_id(34).participant.label \
                != "merve":
            attendance_in_zoom.append(g.get_player_by_id(34))

        print("this is the attendance_in_zoom list:", attendance_in_zoom)

        nbr_players = len(attendance_in_zoom)
        print("nbr_of_players in the zoom:", nbr_players)

        if nbr_players >= 4:
            room1_list = random.sample(attendance_in_zoom, k=4)
            print("this is the list of players in room 1:", room1_list)

            for p in room1_list:
                attendance_in_zoom.remove(p)
                p.room_organizer = 1
                print("in 'for p in room1_list' rn", " - p is:", p, "p.room_organizer is set to:", p.room_organizer)

            print("this is attendance_in_zoom list after room1 members are removed:", attendance_in_zoom)

            if nbr_players >= 8:
                room2_list = random.sample(attendance_in_zoom, k=4)
                print("this is the list of players in room 2:", room2_list)

                for p in room2_list:
                    attendance_in_zoom.remove(p)
                    p.room_organizer = 2
                    print("in 'for p in room2_list:' rn", " - p is:", p, "p.room_organizer is set to:",
                          p.room_organizer)

                print("this is the attendance_in_zoom list after room1 & room2 members are removed:",
                      attendance_in_zoom)

                if nbr_players >= 12:
                    room3_list = random.sample(attendance_in_zoom, k=4)
                    print("this is the list of players in room 3:", room3_list)

                    for p in room3_list:
                        attendance_in_zoom.remove(p)
                        p.room_organizer = 3
                        print("in 'for p in room3_list:' rn", " - p is:", p, "p.room_organizer is set to:",
                              p.room_organizer)

                    print("this is the attendance_in_zoom list after room1 & room2 & room3 members are removed:",
                          attendance_in_zoom)

                    if nbr_players >= 16:
                        room4_list = random.sample(attendance_in_zoom, k=4)
                        print("this is the list of players in room 4:", room4_list)

                        for p in room4_list:
                            attendance_in_zoom.remove(p)
                            p.room_organizer = 4
                            print("in 'for p in room4_list:' rn", " - p is:", p, "p.room_organizer is set to:",
                                  p.room_organizer)

                        print("this is the attendance_in_zoom list after room1 & room2 & room3 & room 4 members are "
                              "removed:", attendance_in_zoom)

                        if nbr_players >= 20:
                            room5_list = random.sample(attendance_in_zoom, k=4)
                            print("this is the list of players in room 5:", room5_list)

                            for p in room5_list:
                                attendance_in_zoom.remove(p)
                                p.room_organizer = 5
                                print("in 'for p in room5_list:' rn", " - p is:", p, "p.room_organizer is set to:",
                                      p.room_organizer)

                            print("this is the attendance_in_zoom list after room1 & room2 & room3 & room 4 & room 5 "
                                  "members are removed:", attendance_in_zoom)


class AdminPage3(Page):
    def is_displayed(self):
        return self.participant.label == "merve"


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
        return self.player.participant.label is not None and self.player.room_organizer == 0 and \
               self.player.participant.label != 'merve'


page_sequence = [AdminPage1,
                 AdminPage2,
                 AdminPage3,
                 EntryToZoomNew,
                 NoShowEntryPage,
                 QuotaNew,
                 ExperimentRedirectR1New,
                 ExperimentRedirectR2New,
                 ExperimentRedirectR3New,
                 ExperimentRedirectR4New,
                 ExperimentRedirectR5New
                 ]
