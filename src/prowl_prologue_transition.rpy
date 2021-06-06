label prowl_prologue_transition:

    window hide
    stop music fadeout 2
    stop sound_loop fadeout 2
    stop ambience fadeout 2

    scene bg black with Dissolve(5)
    play music mondstadt fadein 2
    play ambience amb_mondstadt
    scene ext_mondstadt with Dissolve(1)
    $ renpy.pause(1, hard=True)

    window show
    "Странный сон мне тогда снился."
    "Я в каком-то средневековье, то ли где, но точно что-то несовременное:"
    "Каменные дома с деревянными крышами, небольшая площадь с какими-то тентами, где лежат товары..."
    "Странно, но мне постоянно стало сниться средневековье.{w} К чему бы это?"
    alex "А!?" with soft_quake

    window hide
    show dv normal pioneer with easeinright
    window show

    "Предо-мной восстала красна девица:"
    "Рыжие волосы, глаза цвета янтаря и милая рассерженная мордашка."
    "Странно только, что одета она как-то...{w} Не по-средневековому?..."

    window hide
    $ renpy.pause(.4, hard=True)
    stop music fadeout 2
    show dv cry pioneer close with dspr
    play music music_list["blow_with_the_fires"]
    window show

    "Резко она ринулась на меня, схватила за воротник, прижалась ко мне головой и начала плакать." with soft_quake

    alex "А.{w=.1}.!?{w} Ты чего?"
    null_character "{b}{size=44}СЯДЬ НА АВТОБУС!{w} СЯДЬ НА ЭТОТ ЧЁРТОВ АВТОБУС!{w} НЕ ОСТАВЛЯЙ МЕНЯ ЗДЕСЬ ОДНУ!{/size}{/b}" with hard_quake
    "Что!?"

    window hide
    stop ambience
    scene int_room_of_alex_day with medium_quake
    window show

    "Я вскочил в холодном поту, вскрикнув:"
    alex "Что за нахуй!?" with hard_quake
    "Я побежал в туалет: Меня очень сильно тошнило."
    "..."
    alex "Кх...{w} " with soft_quake
    extend "ГХРА-А-А-АХА!" with hard_quake

    window hide
    stop ambience fadeout 2
    scene logo_animated
    $ renpy.pause(9, hard=True)

    jump prowl_first_day
