# Copyright (c) k1tsukendo, alexwindyxdev 2021. All rights reserved. #
# Notice: GNU General Public License 3.0

init python:

    def build_generator(flag):
        import datetime
        now = datetime.datetime.now()
        if flag == 11: return 'build-{}{}-{}'.format(now.day, now.hour, now.year)
        if flag == 12:
            import random
            hash = random.getrandbits(128)
            return 'build : %032x' % hash 

    def get_user_machine_characerisics():
        try:
            # System Information #
            import platform

            system_name = platform.system()
            system_release = platform.release()
            system_architecture = platform.architecure()[0]

            global system_name, system_release, system_version, system_architecture

        except:
            import os

            system_name = os.uname()[0]
            system_release = os.uname()[2]
            system_version =  os.uname()[3]
            system_architecture = os.uname()[4]
        try:
            # Hardware Info #

            # CPU #
            physical_cores = psutil.cpu_count(logical=False)
            total_cores = psutil.cpu_count(logical=True)

            global physical_cores, total_cores

            # RAM #
            svmem = psutil.virtual_memory()
            memory_total = get_size(svmem.total)

            global memory_total
        except:
            return


    # Constants #
    BUILDGEN_BUILDTIME = 11
    BUILDGEN_BUILDHASH = 12

    K1TSUKENDO_MOD_NAMESPACE = 'prowl'
    K1TSUKENDO_MOD_VERSION = 1.0
    K1TSUKENDO_MOD_BUILD = build_generator(BUILDGEN_BUILDHASH)
    K1TSUKENDO_MOD_NAME = '{font=mods/prowl/res/etc/fnt/12177.ttf}{size=32}Project Owl RE v%s{/size}{/font}' % K1TSUKENDO_MOD_VERSION
    K1TSUKENDO_MOD_BUILDTIME = build_generator(BUILDGEN_BUILDTIME)
    K1TSUKENDO_MOD_STARTPOINT = 'prowl_menu_variant_classic'

    # Preferences #
    prowl_preference_show_hentai = True
    prowl_preference_show_nowPlaying = False
    prowl_preference_show_debug = False

    # Other #
    def mod_launch_debug():
        log = open('debug_log.log', 'w')
        log.write(
            '''Build {}\nBuild time {}\nUsing namespace \'{}\'\n'''
        )
        log.close()

    # Initialization #
    mods[K1TSUKENDO_MOD_STARTPOINT] = K1TSUKENDO_MOD_NAME
    
    try:
        modsImages[K1TSUKENDO_MOD_STARTPOINT] = ('mods/prowl/res/etc/img/mods_image_logo_320x180.jpg', False, K1TSUKENDO_MOD_STARTPOINT)
    except:
        pass
