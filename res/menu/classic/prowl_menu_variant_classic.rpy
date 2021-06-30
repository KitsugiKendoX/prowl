# Copyright (c) k1tsukendo. Some rights reserved.
# License: CC (code always GNU General Public License 3.0)


init 696:

    define PROWL_classic_RESOURCES = PROWL_RESOURCES+'/menu/classic'

    image prowl_menu_classic = Movie(play=PROWL_classic_RESOURCES+'/prowl_menu_classic.ogv')
    if renpy.variant('mobile'):
        image prowl_menu_classic = Movie(size=(1280, 720), play=PROWL_classic_RESOURCES+'/prowl_menu_classic.ogv')


# Default menu style
label prowl_menu_variant_classic:

    # First initialization step:
    #     If something went wrong in main menu,
    #     or user running mod from other mod
    #     this procedure excepting sound issues
    # ProTip: Copy this code in any file and use everywhere!

    window hide
    if prowl_preference_show_debug:
        if not config.developer:
            $ config.developer = True
        $ config.autoreload = True

    # Screen prediction speeds up screen loading and excepting freezes
    $ renpy.start_predict_screen('prowl_menu_variant_classic_screen')
    $ renpy.start_predict_screen('prowl_menu_variant_classic_screen_preferences')

    $ renpy.block_rollback()

    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2

    play music at_eternals_gate fadein 2
    scene bg black with dissolve2

    $ renpy.pause(4, hard=True)
    scene prowl_menu_classic with dissolve2
    show screen prowl_menu_variant_classic_screen with dissolve
    call screen prowl_menu_variant_classic_screen


# Default screen interface style
screen prowl_menu_variant_classic_screen:
    tag menu

    imagemap:

        alpha False 
        cache True  # ProTip: Use "cache" statement everywhere!

        idle PROWL_classic_RESOURCES+'/ui_classic_unhovered.png'
        hover PROWL_classic_RESOURCES+'/ui_classic_hovered.png'

        hotspot (682, 505, 562, 70) action (Hide('prowl_menu_variant_classic_screen', dissolve), Jump('prowl_prologue'))  # Start Game
        hotspot (730, 575, 508, 64) action (Hide('prowl_menu_variant_classic_screen', dspr), Show('prowl_menu_variant_classic_screen_preferences', dspr))
        hotspot (826, 639, 296, 74) action (Hide('prowl_menu_variant_classic_screen', dissolve), Jump('prowl_terminate_classic'))  # Exit

    if config.developer:
        text "{} {} {} {}".format(K1TSUKENDO_MOD_NAME, K1TSUKENDO_MOD_VERSION, K1TSUKENDO_MOD_BUILD, K1TSUKENDO_MOD_BUILDTIME) xalign 0.99:
            size 24
            color "#fff"

        use prowl_debug_info


# Default screen preferences interface style
screen prowl_menu_variant_classic_screen_preferences:
    tag menu

    imagemap:

        alpha False
        cache True

        idle PROWL_classic_RESOURCES+'/ui_classic_unhovered_preferences.png'
        hover PROWL_classic_RESOURCES+'/ui_classic_hovered_preferences.png'

        hotspot (473, 479, 946, 66) action ToggleVariable('prowl_preference_show_hentai', true_value=True, false_value=False)  # NSFW Content
        hotspot (319, 545, 1248, 62) action ToggleVariable('prowl_preference_show_nowPlaying', true_value=True, false_value=False)  # "Now Playing.." widget
        hotspot (623, 609, 650, 66) action ToggleVariable('config.developer', true_value=True, false_value=False)

        hotspot (440, 218, 256, 160) action (Hide('prowl_menu_variant_classic_screen_preferences', dspr), Jump('prowl_menu_variant_HotlineOwl'))

        hotspot (294, 278, 128, 85) action (Hide('prowl_menu_variant_classic_screen_preferences', dspr), Show('prowl_menu_variant_classic_screen', dspr))  # Back

    if config.developer:
        text "{} {} {} {}".format(K1TSUKENDO_MOD_NAME, K1TSUKENDO_MOD_VERSION, K1TSUKENDO_MOD_BUILD, K1TSUKENDO_MOD_BUILDTIME) xalign 0.99:
            size 24
            color "#fff"

        use prowl_debug_info


label prowl_terminate_classic:

    # Stops music. Yes.
    stop music fadeout 4

    # Rolling back changes
    $ config.developer = False  # Developer mode
    $ renpy.stop_predict_screen('prowl_menu_variant_classic_screen')  # Aborting predict of main screen
    $ renpy.stop_predict_screen('prowl_menu_variant_classic_screen_preferences')  # Aborting predict of prefereces screen

    # Just for smooth transition
    $ renpy.pause(1, hard=True)

    scene bg black with dissolve2
    $ renpy.pause(1, hard=True)

    return
