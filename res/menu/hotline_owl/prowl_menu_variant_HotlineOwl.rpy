init 1994:

    define hotline_owl_RESOURCES = PROWL_RESOURCES + '/menu/hotline_owl'

    image prowl_menu_HotlineOwl = Movie(play=hotline_owl_RESOURCES+'/prowl_menu_HotlineOwl.ogv')
    if renpy.variant('mobile'):
        image prowl_menu_HotlineOwl = Movie(size=(1280, 720), play=hotline_owl_RESOURCES+'/prowl_menu_HotlineOwl.ogv')

    define hotline_owl = hotline_owl_RESOURCES+'/sexualizer.ogg'


label prowl_menu_variant_HotlineOwl:

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
    $ renpy.start_predict_screen('prowl_menu_variant_HotlineOwl_screen')
    $ renpy.start_predict_screen('prowl_menu_variant_HotlineOwl_screen_preferences')

    $ renpy.block_rollback()

    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2

    play music hotline_owl fadein 2
    scene bg black with dissolve2

    $ renpy.pause(4, hard=True)
    scene prowl_menu_HotlineOwl with dissolve2
    show screen prowl_menu_variant_HotlineOwl_screen with dissolve
    call screen prowl_menu_variant_HotlineOwl_screen


screen prowl_menu_variant_HotlineOwl_screen:
    tag menu

    imagemap:
        alpha False 
        cache True

        idle hotline_owl_RESOURCES+'/ui_hotlineowl_unhovered.png'
        hover hotline_owl_RESOURCES+'/ui_hotlineowl_hovered.png'

        hotspot (689, 401, 549, 66) action (Hide('prowl_menu_variant_HotlineOwl_screen', dissolve), Jump('prowl_prologue'))  # Start Game
        hotspot (668, 472, 596, 68) action   (Hide('prowl_menu_variant_HotlineOwl_screen', dspr), Show('prowl_menu_variant_HotlineOwl_screen_preferences', dspr))
        hotspot (866, 547, 200, 60) action (Hide('prowl_menu_variant_HotlineOwl_screen', dissolve), Jump('prowl_terminate_HotlineOwl'))


screen prowl_menu_variant_HotlineOwl_screen_preferences:
    tag variant_HotlineOwl_menu_preferences

    imagemap:

        alpha False
        cache True

        idle hotline_owl_RESOURCES+'/ui_hotlineowl_unhovered_preferences.png'
        hover hotline_owl_RESOURCES+'/ui_hotlineowl_hovered_preferences.png'

        hotspot (622, 465, 679, 77) action ToggleVariable('prowl_preference_show_hentai', true_value=True, false_value=False)  # NSFW Content
        hotspot (456, 554, 1008, 53) action ToggleVariable('prowl_preference_show_nowPlaying', true_value=True, false_value=False)  # "Now Playing.." widget
        hotspot (689, 626, 540, 48) action ToggleVariable('prowl_preference_show_debug', true_value=True, false_value=False)

        hotspot (618, 788, 683, 75) action (Hide('prowl_menu_variant_HotlineOwl_screen_preferences', dspr), Jump('prowl_menu_variant_classic'))

        hotspot (0, 924, 743, 153) action (Hide('prowl_menu_variant_HotlineOwl_screen_preferences', dspr), Show('prowl_menu_variant_HotlineOwl_screen', dspr))  # Back


label prowl_terminate_HotlineOwl:

    # Stops music. Yes.
    stop music fadeout 4

    # Rolling back changes
    $ config.developer = False  # Developer mode
    $ renpy.stop_predict_screen('prowl_menu_variant_HotlineOwl_screen')  # Aborting predict of main screen
    $ renpy.stop_predict_screen('prowl_menu_variant_HotlineOwl_screen_preferences')  # Aborting predict of prefereces screen

    # Just for smooth transition
    $ renpy.pause(1, hard=True)

    scene bg black with dissolve2
    $ renpy.pause(1, hard=True)

    return
