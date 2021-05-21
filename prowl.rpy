# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                      ..Project Owl Reborn..                           #
#                                                                       #
# Authors: Kitsugi Kendo                                                #
# Copyright (C) KSoftware, Soviet Games 2013-2021. All Rights Reserved. #
# Code license: GNU GPL v3.0                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# initialization #
init 69 python:

    # Mod constants #
    MOD_VERSION = 'v1.0.0dev1'  # Displaying in debug mode
    MOD_NAME = 'Project Owl Reborn %s' % MOD_VERSION  # Displaying in debug mode
    MOD_START = 'prowl_menu'  # Displaying in debug mode
    MOD_IMAGE = None  # Displaying in mod as preview

    mods[MOD_START] = MOD_NAME # Display in mod selection menu
    config.developer = True

    configuration = {
        'debug': False,
        'display_variables': False,
        'display_debug_info': False,
        'display_user_info': False
    }
