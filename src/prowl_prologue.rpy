label prowl_prologue:

    window hide
    stop music fadeout 2
    stop sound_loop fadeout 2
    stop ambience fadeout 2

    scene bg black with Dissolve(5)
    play music night fadein 2
    play ambience amb_room_silence fadein 2
    $ renpy.pause(1, hard=True)

    "...{w}{w}Ночь.{w} Прекрасная, тёмная ночь.{w} Может, кто-то сделал её такой?"
    "..."
    "Я никогда не любил утро и день. Слишком...{w} Напряжно."

    window hide
    scene int_room_of_alex_night with Dissolve(1.3)
    $ renpy.pause(1, hard=True)
    window show

    "Люди выходят на улицу. Кто на работу, кто ещё куда.{w} Сразу не разберёшь."
    "...{w}А вот ночь.{w} Прекрасная Калуга. Я уверен, что здесь по ночам нравится абсолютно всем."
    "Фонарные столбы, усеянные разноцветными вывесками и надписями. Всё это создаёт прекрасный внешний вид улицам."
    "..."
    th "Не хочется вставать...{w} А надо."

    play sound sfx_bed_stand_up

    "Я отложил телефон, встал, потянулся и пошёл на кухню."

    window hide
    play sound sfx_footsteps_wood
    scene bg black with Dissolve(2)
    scene int_kitchen_night with Dissolve(3.3)
    $ renpy.pause(delay=1, music=None, with_none=None, hard=True, checkpoint=None)
    window show

    th "Надо бы сегодня всё же сесть за проект, а то дедлайн скоро..."
    th "Хотя, блин...{w} Только с работы пришёл. Но надо."
    th "Можно, в принципе, сбросить цену взамен на увеличение срока."
    th "На жалость давить..."

    window hide
    play sound sfx_wsh
    $ renpy.pause(delay=.5, music=None, with_none=None, hard=True, checkpoint=None)
    window show

    "Я включил чайник."
    th "Не хочется."
    "Я подошёл к окну начал смотреть на улицу."
    "Да.{w} Про огни я не соврал.{w} Прекрасное зрелище."
    th "Прекрасное лето. {b}Лучшее лето.{/b}"
    "Я включил телевизор и поставил на низкую громкость, чтобы просто играл фоном."
    "Я часто так любуюсь видами.{w} {i}Высоко сижу - далеко гляжу{/i}."

    window hide
    $ renpy.pause(delay=1, music=None, with_none=None, hard=False, checkpoint=None)
    window show

    "Ежедневно по ночам мне открывается прекрасный вид на набережную, вдоль которой идут фонарные столбы с яркими, сверкающими вывесками и надписями."
    "Лето тогда было довольно жарким, потому я решил открыть окно и закурил."
    "Чайник всё кипел и кипел, убаюкивая постоянным шумом."
    th "Тц. Сука. 20 лет...{w} Скоро уже 21... "
    th "Что-то я теряю...{w} Не пойму, что."
    th "Кх.{w} Да и шло бы оно всё к чёртовой матери! Жизнь продолжается."

    window hide
    $ renpy.pause(1.5, hard=True)
    window show

    "Чайник вскипел, а я сделал телевизор погромче и начал наливать себе хороший, крепкий чай с заварника, которому лет больше, чем моему отцу."
    th "Хм.{w} 8 часов.{w} Думаю, родители ещё не спят."

    window hide
    scene bg black with Dissolve(2)
    scene bg int_room_of_alex_night with Dissolve(6)
    window show

    "Я зашёл обратно в комнату, взял телефон и пошёл обратно на кухню."

    window hide
    scene bg black with Dissolve(2)
    scene bg int_kitchen_night with Dissolve(6)
    window show

    th "Тэкс...{w} Ну, глянем."
    "Я начал звонить отцу."

    window hide
    $ renpy.pause(1, hard=True)
    window show

    "Он взял трубку.{w} Видеочат."

    window hide
    $ set_mode_nvl()
    $ renpy.pause(1, hard=True)
    window show

    alex "Привет, пап!{w} Как у вас там дела? Давно мы с вами не созванивались!"
    father "Хо-хо, кто звонит!{w} Лерка, иди сюды!{w} Сынка объявился в шайтан-коробе!"
    alex "Ха-ха! Привет, мам!"
    mother "Здравствуй, Лёш! Как у тебя там дела?"
    alex "Не-не, я первый спросил!"
    father "Тфу, ёптыть, нормально у нас всё!{w} Не девяностые же!"
    alex "Сплюнь.{w} У меня тоже всё более-менее окей.{w} Живу, не тужу, да блох развожу."
    father "Ну и бездельник же ты, ей Богу!"
    alex "Да-а...{w} Есть немного.{w} Я, в общем-то говоря, с утра на работу, так что я, пожалуй, пойду попью чаю, да спатеньки."
    mother "Конечно, Лёш, иди!{w} Рада, что позвонил! Пока!"
    alex "Пока, целую-обнимаю."

    window hide
    $ set_mode_adv()
    $ renpy.pause(1, hard=True)
    window show

    "Я положил трубку, слегка улыбнулся и допил чай."
    "Иногда я звоню родителям вечерами, просто чтобы проверить, всё ли нормально."
    "Всегда у них всё нормально...{w} Рад за них."
    th "Господи, храни маму и папу...{w} Ежи еси там, на этом,..{w} На небеси."
    th "Даже помолиться нормально не могу.{w} Жесть."
    "Я встал, последний раз взглянул в окно, улыбнулся и пошёл в комнату."

    window hide
    play sound sfx_footsteps_wood
    scene bg black with Dissolve(3)
    scene int_room_of_alex_day with dissolve
    window show

    "Тяжёлый трудовой день окончен, я с тяжёлой башкой снимаю с себя домашнюю одежду, ложу на комод...{w} И с тяжеленной башкой заваливаюсь на кровать."
    th "Мм, прохладная. За день-то охладилась...{w} Жара на улице - невыносима."
    "И так я заснул, даже не заметив этого."

    window hide
    show blink
    stop music fadeout 2
    stop ambience fadeout 2
    $ renpy.pause(1, hard=True)

    return
