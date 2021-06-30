label prowl_prologue:

    window hide

    $ prolog_time()
    $ new_chapter(u'Project Owl : Reborn : Chapter 0')

    stop music fadeout 2
    stop sound_loop fadeout 2
    stop ambience fadeout 2

    play ambience amb_room_silence fadein 4
    scene bg black with Dissolve(4)

    $ renpy.pause(1, hard=True)

    show screen prowl_debug_info
    play music around
    window show

    alex 'Ночь.{w} Тёмная, прекрасная ночь.'
    alex 'Кто же сделал её такой?'
    alex 'Наверное, мы никогда не узнаем.'

    window hide 
    $ renpy.pause(1, hard=True)
    scene bg semen_room with Dissolve(5)
    window show 

    'Снова я лежу в комнате, заполненной хламом.'
    'Листая телеграм посреди ночи ты мало задумываешься об уборке.'
    'Почему не ДваЧ?{w} Ну… {w}Мягко говоря… {w}ДваЧ уже не торт.'
    '...'

    window hide 
    $ renpy.pause(1, hard=True)
    window show 

    'Всё же жить в спокойствии — прекрасно.'
    '...'

    window hide 
    $ renpy.pause(1, hard=True)
    window show 

    'Единственный, кто в последнее время говорил со мной, так это старый друг…'
    'Точнее сказать — бывший одногруппник.{w} Стас.'
    'Стас никогда не был весёлым, или даже близко к этому.'
    'Потому он и начал общаться со мной, так как я тоже в кой-то степени был белой вороной.'

    'Я бы не сказал, что я был грустным, но не очень любил общаться.'
    'Я, конечно, жаждал поговорить за просто так, но всё же зная лживость людей этого совсем не хочется, потому жажду общения я всё же категоризировал, как обычную потребность.'

    window hide 
    $ renpy.pause(1, hard=True)
    window show 

    alex 'Сап. Не хотел бы ты прогуляться сегодня до магаза электроплюшек'
    prowl_Stas 'здаров'
    prowl_Stas 'ну хз хз я сегодня хотел в доме прибраться'
    alex 'Чего? Ты? Прибраться?)))'
    alex 'Дай угадаю девушку нашёл?))'
    prowl_Stas 'ну типа того))'
    alex 'Хахах ну кк оставлю вас в покое{w}{w}{w}'
    prowl_Stas ')'

    window hide 
    $ renpy.pause(1, hard=True)
    stop music fadeout 2
    window show 

    '…'
    'Я отложил телефон и посмотрел в окно.'
    'Я не видел ни-че-го.{w} Только лишь ночное небо.'
    'Через 15 минут я развернулся к стене, прикрыл ногу одеялом, и очень быстро уснул.'
    '…'

    window hide
    stop ambience fadeout 2.34

    $ renpy.pause(1, hard=True)
    $ day_time()

    scene bg black with Dissolve(1.3)
    play music mondstadt_starlit
    window show

    th 'Сколько времени прошло?'
    th 'Почему так громко звонят колокола?'
    th 'Где я?'
    '...'
    'Я открыл глаза.'

    window hide 
    scene ext_mondstadt_dream with Dissolve(1.3)
    window show

    'Передо-мной возвышались здания из каменных кирпичей, некоторые обросшие лозой, с крышей из красной черепицы.'
    'Вокруг меня бегали люди в одежде, похожей на какие-то тряпки.'
    'Вон, бежит светловолосый мальчик.{w} Судя по всему — к воротам города.'
    'А вон, видимо, богатая персона — светловолосая девочка в белоснежных одеяниях, а рядом с ней летит волшебная бестия: маленькая девочка в пышной одежде.'

    window hide 
    stop music fadeout 4
    $ renpy.pause(1, hard=True)

    show dv cry far pioneer2 at fright with dissolve
    window show 

    'Стоило мне отвести взгляд, как передо-мной будто из-под земли вылезла девчушка, что по одежде не подходила ни под эту, ни под мою эпоху.'
    'Она стояла, смотрела на меня и плакала.'
    'Только я собрался я спросить «что случилось?», так сразу же она набросилась на меня и закричала:'

    play music music_list["blow_with_the_fires"]

    show dv cry close pioneer2 with dspr

    unknown_narrator 'СЯДЬ НА ЭТОТ ЧЁРТОВ АВТОБУС!{w} НЕ ОСТАВЛЯЙ МЕНЯ!{w} ПРОШУ!' with soft_shake

    window hide 
    $ prolog_time()
    scene bg semen_room with dissolve 
    with soft_shake
    $ renpy.pause(0.3, hard=True)
    window show 

    'В холодном поту я вскочил с кровати.'
    'Меня накрыла тошнота, начала кружиться голова, тысячи мыслей захлестнули меня и я полетел к унитазу.'

    window hide 
    scene bg black with dissolve2
    $ renpy.pause(0.6, hard=True)
    window show 

    'Кх… {w}КХА-А-АХА!'

    window hide 
    stop music fadeout 4
    $ renpy.pause(4, hard=True)

    return
