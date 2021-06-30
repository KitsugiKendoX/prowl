# Project Owl Reborn`s resources file

init 666:

    # Variables #
    define PROWL_ROOT      = 'mods/'         + K1TSUKENDO_MOD_NAMESPACE
    define PROWL_RESOURCES = PROWL_ROOT      + '/res'
    define PROWL_IMAGES    = PROWL_RESOURCES + '/img'
    define PROWL_AUDIO     = PROWL_RESOURCES + '/audio'
    define PROWL_BG        = PROWL_IMAGES    + '/bg'
    define PROWL_CG        = PROWL_IMAGES    + '/cg'
    define PROWL_SP        = PROWL_IMAGES    + '/sp'
    define PROWL_MUS       = PROWL_AUDIO     + '/mus'
    define PROWL_SND       = PROWL_AUDIO     + '/snd'
    define PROWL_AMB       = PROWL_AUDIO     + '/amb'

    # Characters #
    define alex = Character('Алексей', color='#696969')
    define unknown_narrator = Character('...', color='#a1c24e')
    define prowl_Stas = Character('Стас', color='ba0000')

    # Scripts #
    define soft_shake = Shake((0.5, 1, 0.5, 1), 1.0, dist=6)
    define norm_shake = Shake((0.5, 1, 0.5, 1), 1.0, dist=15)

    # Backgrounds #
    image ext_mondstadt_dream = PROWL_BG + '/ext_mondstadt_dream.jpg'

    # Music #
    define around = PROWL_MUS + '/around.ogg'
    define at_eternals_gate = PROWL_MUS + '/at_eternals_gate.ogg'
    define mondstadt_starlit = PROWL_MUS + '/mondstadt_starlit.ogg'

    # Ambience #
    # TODO: Convert all media to .jpg, .ogg, .wav, and .ogv
    define amb_room_silence = PROWL_AMB + 'amb_room_silence.mp3'
