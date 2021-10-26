from os import environ

SESSION_CONFIGS = [
{
        'name': 'ENTRY_LINKS_ZOOM',
        'display_name': 'ENTRY & LINKS BASED ON ATTENDANCE (V2)',
        'num_demo_participants': 1,
        'app_sequence': ['entry_links_zoom',
                         ],
        'Prolific_ID_1': 'PID1',
        'ZOOM_Regis_Link_1': 'LINK1',
        'Prolific_ID_2': 'PID2',
        'ZOOM_Regis_Link_2': 'LINK2',
        'Prolific_ID_3': 'PID3',
        'ZOOM_Regis_Link_3': 'LINK3',
        'Prolific_ID_4': 'PID4',
        'ZOOM_Regis_Link_4': 'LINK4',
        'Prolific_ID_5': 'PID5',
        'ZOOM_Regis_Link_5': 'LINK5',
        'Prolific_ID_6': 'PID6',
        'ZOOM_Regis_Link_6': 'LINK6',
        'Prolific_ID_7': 'PID7',
        'ZOOM_Regis_Link_7': 'LINK7',
        'Prolific_ID_8': 'PID8',
        'ZOOM_Regis_Link_8': 'LINK8',
        'Prolific_ID_9': 'PID9',
        'ZOOM_Regis_Link_9': 'LINK9',
        'Prolific_ID_10': 'PID10',
        'ZOOM_Regis_Link_10': 'LINK10',
        'Prolific_ID_11': 'PID11',
        'ZOOM_Regis_Link_11': 'LINK11',
        'Prolific_ID_12': 'PID12',
        'ZOOM_Regis_Link_12': 'LINK12',
        'Prolific_ID_13': 'PID13',
        'ZOOM_Regis_Link_13': 'LINK13',
        'Prolific_ID_14': 'PID14',
        'ZOOM_Regis_Link_14': 'LINK14',
        'Prolific_ID_15': 'PID15',
        'ZOOM_Regis_Link_15': 'LINK15',
        'Prolific_ID_16': 'PID16',
        'ZOOM_Regis_Link_16': 'LINK16',
        'Prolific_ID_17': 'PID17',
        'ZOOM_Regis_Link_17': 'LINK17',
        'Prolific_ID_18': 'PID18',
        'ZOOM_Regis_Link_18': 'LINK18',
        'Prolific_ID_19': 'PID19',
        'ZOOM_Regis_Link_19': 'LINK19',
        'Prolific_ID_20': 'PID20',
        'ZOOM_Regis_Link_20': 'LINK20',
        'Prolific_ID_21': 'PID21',
        'ZOOM_Regis_Link_21': 'LINK21',
        'Prolific_ID_22': 'PID22',
        'ZOOM_Regis_Link_22': 'LINK22',
        'Prolific_ID_23': 'PID23',
        'ZOOM_Regis_Link_23': 'LINK23',
        'Prolific_ID_24': 'PID24',
        'ZOOM_Regis_Link_24': 'LINK24',
        'Prolific_ID_25': 'PID25',
        'ZOOM_Regis_Link_25': 'LINK25',
        'Prolific_ID_26': 'PID26',
        'ZOOM_Regis_Link_26': 'LINK26',
        'Prolific_ID_27': 'PID27',
        'ZOOM_Regis_Link_27': 'LINK27',
        'Prolific_ID_28': 'PID28',
        'ZOOM_Regis_Link_28': 'LINK28',
        'Prolific_ID_29': 'PID29',
        'ZOOM_Regis_Link_29': 'LINK29',
        'Prolific_ID_30': 'PID30',
        'ZOOM_Regis_Link_30': 'LINK30',
        'Prolific_ID_31': 'PID31',
        'ZOOM_Regis_Link_31': 'LINK31',
        'Prolific_ID_32': 'PID32',
        'ZOOM_Regis_Link_32': 'LINK32',
        'Prolific_ID_33': 'PID33',
        'ZOOM_Regis_Link_33': 'LINK33',
        'Prolific_ID_34': 'PID33',
        'ZOOM_Regis_Link_34': 'LINK33',
    },
    {
        'name': 'ENTRY_LINKS',
        'display_name': 'ENTRY & LINKS (V1)',
        'num_demo_participants': 1,
        'app_sequence': ['entry_links',
                         ],
        'Prolific_ID_1': 'PID1',
        'ZOOM_Regis_Link_1': 'LINK1',
        'Prolific_ID_2': 'PID2',
        'ZOOM_Regis_Link_2': 'LINK2',
        'Prolific_ID_3': 'PID3',
        'ZOOM_Regis_Link_3': 'LINK3',
        'Prolific_ID_4': 'PID4',
        'ZOOM_Regis_Link_4': 'LINK4',
        'Prolific_ID_5': 'PID5',
        'ZOOM_Regis_Link_5': 'LINK5',
        'Prolific_ID_6': 'PID6',
        'ZOOM_Regis_Link_6': 'LINK6',
        'Prolific_ID_7': 'PID7',
        'ZOOM_Regis_Link_7': 'LINK7',
        'Prolific_ID_8': 'PID8',
        'ZOOM_Regis_Link_8': 'LINK8',
        'Prolific_ID_9': 'PID9',
        'ZOOM_Regis_Link_9': 'LINK9',
        'Prolific_ID_10': 'PID10',
        'ZOOM_Regis_Link_10': 'LINK10',
        'Prolific_ID_11': 'PID11',
        'ZOOM_Regis_Link_11': 'LINK11',
        'Prolific_ID_12': 'PID12',
        'ZOOM_Regis_Link_12': 'LINK12',
        'Prolific_ID_13': 'PID13',
        'ZOOM_Regis_Link_13': 'LINK13',
        'Prolific_ID_14': 'PID14',
        'ZOOM_Regis_Link_14': 'LINK14',
        'Prolific_ID_15': 'PID15',
        'ZOOM_Regis_Link_15': 'LINK15',
        'Prolific_ID_16': 'PID16',
        'ZOOM_Regis_Link_16': 'LINK16',
        'Prolific_ID_17': 'PID17',
        'ZOOM_Regis_Link_17': 'LINK17',
        'Prolific_ID_18': 'PID18',
        'ZOOM_Regis_Link_18': 'LINK18',
        'Prolific_ID_19': 'PID19',
        'ZOOM_Regis_Link_19': 'LINK19',
        'Prolific_ID_20': 'PID20',
        'ZOOM_Regis_Link_20': 'LINK20',
        'Prolific_ID_21': 'PID21',
        'ZOOM_Regis_Link_21': 'LINK21',
        'Prolific_ID_22': 'PID22',
        'ZOOM_Regis_Link_22': 'LINK22',
        'Prolific_ID_23': 'PID23',
        'ZOOM_Regis_Link_23': 'LINK23',
        'Prolific_ID_24': 'PID24',
        'ZOOM_Regis_Link_24': 'LINK24',
        'Prolific_ID_25': 'PID25',
        'ZOOM_Regis_Link_25': 'LINK25',
        'Prolific_ID_26': 'PID26',
        'ZOOM_Regis_Link_26': 'LINK26',
        'Prolific_ID_27': 'PID27',
        'ZOOM_Regis_Link_27': 'LINK27',
        'Prolific_ID_28': 'PID28',
        'ZOOM_Regis_Link_28': 'LINK28',
        'Prolific_ID_29': 'PID29',
        'ZOOM_Regis_Link_29': 'LINK29',
        'Prolific_ID_30': 'PID30',
        'ZOOM_Regis_Link_30': 'LINK30',
        'Prolific_ID_31': 'PID31',
        'ZOOM_Regis_Link_31': 'LINK31',
        'Prolific_ID_32': 'PID32',
        'ZOOM_Regis_Link_32': 'LINK32',
        'Prolific_ID_33': 'PID33',
        'ZOOM_Regis_Link_33': 'LINK33',
    },
    {
        'name': 'SHB_W1_LEFT',
        'display_name': 'SHB_W1_LEFT',
        'num_demo_participants': 4,
        'app_sequence': ['shb_w1_l',
                         'shb_w1_l_be',
                         'lottery',
                         'crtquestions',
                         'follow_up_survey'
                         ],
        'session_seed': 5,
        'Completion_URL': 'ENTER COMPLETION URL',
        'wave': 1,
        'sender_groups': 'left',
        'discretionary': 0,
        'doc': """
        Edit the 'session_seed' to change the seed for random type and error choices.
        s1: / s2: / s3: / s4: / s5: / s6: / s7: / s8: / s9: / s10: ....
        """
    }, 
    {
        'name': 'SHB_W1_RIGHT',
        'display_name': 'SHB_W1_RIGHT',
        'num_demo_participants': 2,
        'app_sequence': ['shb_w1_r',
                         'shb_w1_r_be',
                         'lottery',
                         'crtquestions',
                         'follow_up_survey'
                         ],
        'session_seed': 5,
        'Completion_URL': 'ENTER COMPLETION URL',
        'wave': 1,
        'sender_groups': 'right',
        'discretionary': 0,
        'doc': """
        Edit the 'session_seed' to change the seed for random type and error choices.
        s1: / s2: / s3: / s4: / s5: / s6: / s7: / s8: / s9: / s10: ....
        """
    },
    #{
        #'name': 'SHB_W1_SYMM',
        #'display_name': 'SHB_W1_SYMM',
        #'num_demo_participants': 4,
        #'app_sequence': ['shb_w1_s', 'acquire', 'lottery', 'token_alloc', 'follow_up_survey'],
        #'session_seed': 5, 
        # 'Completion_URL': 'ENTER COMPLETION URL',
        #'doc': """
         #Edit the 'session_seed' to change the seed for random type and error choices.
         #s1: / s2: / s3: / s4: / s5: / s6: / s7: / s8: / s9: / s10: ....
        #"""
    #},
    {
        'name': 'SHB_W2_LEFT',
        'display_name': 'SHB_W2_LEFT',
        'num_demo_participants': 2,
        'app_sequence': ['shb_w2_l',
                         'shb_w2_l_be',
                         'lottery',
                         'crtquestions',
                         'follow_up_survey'
                         ],
        'session_seed': 5, 
        'Completion_URL': 'ENTER COMPLETION URL',
        'wave': 2,
        'sender_groups': 'left',
        'discretionary': 1,
        'doc': """
         Edit the 'session_seed' to change the seed for random type and error choices.
         s1: / s2: / s3: / s4: / s5: / s6: / s7: / s8: / s9: / s10: ....
        """
    },
    {
        'name': 'SHB_W3_1',
        'display_name': 'SHB_W3_1',
        'num_demo_participants': 2,
        'app_sequence': ['shb_w3_1',
                         'shb_w3_1_be',
                         'lottery',
                         'crtquestions',
                         'follow_up_survey'
                        ],
        'session_seed': 5, 
        'Completion_URL': 'ENTER COMPLETION URL',
        'wave': 3,
        'sender_groups': 'right_left',
        'discretionary': 0,
        'doc': """
         Edit the 'session_seed' to change the seed for random type and error choices.
         s1: / s2: / s3: / s4: / s5: / s6: / s7: / s8: / s9: / s10: ....
        """
    },
    {
        'name': 'SHB_W3_2',
        'display_name': 'SHB_W3_2',
        'num_demo_participants': 2,
        'app_sequence': ['shb_w3_2',
                         'shb_w3_2_be',
                         'lottery',
                         'crtquestions',
                         'follow_up_survey'
                         ],
        'session_seed': 5, 
        'Completion_URL': 'ENTER COMPLETION URL',
        'wave': 3,
        'sender_groups': 'right_left',
        'discretionary': 1,
        'doc': """
        Edit the 'session_seed' to change the seed for random type and error choices.
        s1: / s2: / s3: / s4: / s5: / s6: / s7: / s8: / s9: / s10: ....
        """
    },
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=6.50, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    {
        'name': 'live_demo',
        'display_name': 'Room for Live Demo (no participant labels)'
    },
    {
        'name': 'entry_links',
        'display_name': 'Entry & Links'
    },
    {
        'name': 'room_1',
        'display_name': 'Room 1'
    },
    {
        'name': 'room_2',
        'display_name': 'Room 2'
    },
    {
        'name': 'room_3',
        'display_name': 'Room 3'
    },
    {
        'name': 'room_4',
        'display_name': 'Room 4'
    },
    {
        'name': 'room_5',
        'display_name': 'Room 5'
    },
    {
        'name': 'room_show_up',
        'display_name': 'Room for Show-Ups'
    },

]

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')
"""
When you first install oTree, The entire admin interface is accessible without a password. However, when you are ready 
to deploy to your audience, you should password protect the admin.

If you are launching an experiment and want visitors to only be able to play your app if you provided them with a start 
link, set the environment variable OTREE_AUTH_LEVEL to STUDY.

To put your site online in public demo mode where anybody can play a demo version of your game (but not access the full 
admin interface), set OTREE_AUTH_LEVEL to DEMO.

The normal admin username is “admin”. You should set your password in the OTREE_ADMIN_PASSWORD environment variable (on 
Heroku, log into your Heroku dashboard, and define it as a config var).

If you change the admin username or password, you need to reset the database.
"""

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'f8!8zlifoce^je^+$6m^4gh!+@q&!%!4jp3b@o%pzi98!k+9h*'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
