screen prowl_debug_info:
    text 'prowl ' + str(K1TSUKENDO_MOD_VERSION) + ' debug mode.' yalign 0 xalign 0.5:
        size 28
    text 'show_nsfw: {} show_NowPlaying: {} rel_alice: NODATA rel_sofia: NODATA'.format(prowl_preference_show_hentai, prowl_preference_show_nowPlaying) yalign 0.88 xalign 0.5
