# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                      ..Project Owl Reborn..                           #
#                                                                       #
# Authors: Kitsugi Kendo, dacenter                                      #
# Copyright (C) KSoftware, Soviet Games 2013-2021. All Rights Reserved. #
# Code license: GNU GPL v3.0                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Menu #
init:
    image m_bg_animated = Movie(play='res/menu/main_mov.ogv')

label prowl_menu:
    play music gates
    scene bg black with dissolve2
    pause(1)
    scene m_bg_animated with dspr
    show screen prowl_menu
    call screen prowl_menu

screen prowl_menu:
    imagemap:
        idle '%sm_nav_unh.png' % MENU
        hover '%sm_nav_h.png' % MENU

        alpha False
        cache True

        hotspot(62,393,649,476) action Jump(label='prowl_menu')  # Start
        hotspot(63,482,649,558) action Jump(label='prowl_menu')  # Continue
        hotspot(219,642,495,744) action Return()  # Exit
