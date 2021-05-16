# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                      ..Project Owl Reborn..                           #
#                                                                       #
# Authors: Kitsugi Kendo, dacenter                                      #
# Copyright (C) KSoftware, Soviet Games 2013-2021. All Rights Reserved. #
# Code license: GNU GPL v3.0                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

label prowl_prologue:

    window hide
    stop music fadeout 2
    stop sound_loop fadeout 2
    stop ambience fadeout 2

    play music night
    scene bg black with Dissolve(5)
    pause(1)
    window show 

    '...{w}Ночь.{w} Прекрасная, тёмная ночь.{w} Может, кто-то сделал её такой?'
    '...'

    window hide 
    scene bg int_house_of_alex_night with Dissolve(1)
    window show

    'Я никогда не любил утро и день. Слишком...{w} Напряжно.'
    'Люди выходят на улицу. Кто на работу, кто ещё куда. Сразу не разберёшь.'
    '...{w}А вот ночь. Прекрасная Калуга.{w} Я уверен, что здесь по ночам нравится абсолютно всем.'
    'Фонарные столбы, усеянные разноцветными вывесками и надписями. Всё это создаёт прекрасный внешний вид улицам.'
    '...'

    th 'Не хочется вставать... А надо.'

    'Я отложил телефон, встал, потянулся, и пошёл на кухню.'

    window hide
    scene bg int_kitchen_night with Dissolve(3)
    window show

    th 'Надо бы сегодня всё же сесть за проект, а то дедлайн скоро...'
    th 'Хотя, блин... {w}Только с работы пришёл.{w}{w}{w} Но надо.'
    th 'Можно, в принципе, сбросить цену взамен на увеличение срока.'

    return
