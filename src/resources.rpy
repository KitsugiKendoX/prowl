# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                      ..Project Owl Reborn..                           #
#                                                                       #
# Authors: Kitsugi Kendo                                                #
# Copyright (C) KSoftware, Soviet Games 2013-2021. All Rights Reserved. #
# Code license: GNU GPL v3.0                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

init:
    # Resources #
    # Paths #
    $ ROOT = 'mods/prowl/'
    $ RESOURCES = '%sres/' % ROOT
    $ SOURCES = '%ssrc/' % ROOT
    $ IMAGES = '%simg/' % RESOURCES
    $ AUDIO = '%saudio/' % RESOURCES
    $ MENU = '%smenu/' % RESOURCES
    $ BG = '%sbg/' % IMAGES
    $ CG = '%scg/' % IMAGES
    $ SPR = '%sspr/' % IMAGES
    $ SFX = '%ssfx/' % AUDIO
    $ MUS = '%smus/' % AUDIO

    # VFX #
    $ soft_quake = Shake((0, 0, 0, 0), 1.0, dist=15)
    $ medium_quake = Shake((4, 0, 4, 0), 1.0, dist=15)
    $ hard_quake = Shake((8, 0, 8, 0), 1.0, dist=15)

    # Characters #
    define alex = Character(u'Форчев', color='#e06c6e')
    define father = Character(u'Отец', color='#4a81b7')
    define mother = Character(u'Матушка', color='#5f8a34')
    define null_character = Character(". . .", color='#878787')

    # Audio #
    # SFX #
    $ audio.sfx_bed_stand_up = '%ssfx_bed_stand_up.wav' % SFX
    $ audio.sfx_breathing_alex = '%ssfx_breathing_alex.wav' % SFX
    $ audio.sfx_footsteps_wood = '%ssfx_footsteps_wood.wav' % SFX
    $ audio.sfx_wsh = '%ssfx_wsh.wav' % SFX

    # Music #
    $ gates = '%sat_eternals_gate.ogg' % MUS  # Mick Gordon  - At Eternal`s Gate
    $ mondstadt = '%smondstadt.mp3' % MUS   # Yu-Peng Chen, HOYO-Mix - Mondshtadt Starlit
    $ night = '%snight.ogg' % MUS

    # Ambience #
    $ amb_room_silence = '%samb_room_silence.wav' % SFX
    $ amb_mondstadt = '%samb_mondstadt.ogg' % SFX

    # Images #
    # BG #
    image int_room_of_alex_day = '%sint_room_of_alex_day.jpg' % BG
    image int_room_of_alex_night = '%sint_room_of_alex_night.jpg' % BG
    image int_kitchen_day = '%sint_kitchen_day.jpg' % BG
    image int_kitchen_night = '%sint_kitchen_night.jpg' % BG
    image ext_mondstadt = '%sext_mondstadt.png' % BG

    # CG #
    # Sprites #
    image jarik close calm = '%sjarik/close/jarik_1_calm_close.png' % SPR
