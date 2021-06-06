# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                      ..Project Owl Reborn..                           #
#                                                                       #
# Authors: Kitsugi Kendo (k1tsukendo)                                   #
# Copyright (C) KSoftware, Soviet Games 2013-2021. All Rights Reserved. #
# license: GNU GPL v3.0                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Menu #
init:
    image m_bg_animated = Movie(play='mods/prowl/res/menu/main_mov.ogv')
    image logo_animated = Movie(play='mods/prowl/res/menu/logo.ogv')

label prowl_menu:
    stop music fadeout 2
    play music gates
    scene bg black with dissolve2
    pause(1)
    scene m_bg_animated with Dissolve(6)
    show screen prowl_menu with dissolve
    call screen prowl_menu

screen prowl_menu:
    imagemap:
        idle '%sm_nav_unh.png' % MENU
        hover '%sm_nav_h.png' % MENU

        alpha False
        cache True

        hotspot(0,0,433,279) action NullAction()
        hotspot(65,390,589,88) action Jump(label='prowl_prologue')  # Start
        hotspot(67,483,586,77) action NullAction()  # Continue
        hotspot(220,627,277,122) action Return()  # Exit
