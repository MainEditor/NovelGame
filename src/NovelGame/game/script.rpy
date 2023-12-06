init:
    $ namePos = Position(xalign=0.519, yalign=1)

init python:
    involvement = 0

# Определение персонажей игры.
define GG = Character("Главный герой")
define Andrew = Character("Андрей", image="Andrew")
define Oleg = Character("Олег")
define Kate = Character("Катя")

image messengerBG = "messenger.png"
image AndrewName = "AndrewName.png"
image side Andrew nerd:
    "side_andrew_nerd.png"
    zoom 0.55
image KateName = "KateName.png"
image OlegName = "OlegName.png"

# Игра начинается здесь:
label start:

    scene messengerBG

    show AndrewName at namePos zorder 1
    show image "dialogueAndrew.png" at Position(yalign=-0.22)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=-0.135)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.2)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.325)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.4)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.545)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.625)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.725)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.805)
    $ renpy.pause()
    
    "{size=*1.5}*Слава пишет другу Олегу, с которым тоже немало знаком*"
    window hide
    hide image "dialogueAndrew.png"
    hide AndrewName

    show OlegName at namePos zorder 1
    show image "ToOleg.png" at truecenter
    $ renpy.pause()

    "{size=*1.5}*Слава решил написать ещё своей подруге Кате*"
    hide image "ToOleg.png"
    hide OlegName

    show KateName at namePos zorder 1
    show image "ToKate.png" at truecenter
    $ renpy.pause()
#
    play audio "audio/sounds/notification.mp3" volume 1.0
    "{size=*1.5}*Пришло сообщение от Олега*"
    hide image "ToKate.png"
    hide KateName

    show OlegName at namePos zorder 1
    show image "dialogueOleg.png" at Position(yalign=-0.2)
    $ renpy.pause()
    show image "dialogueOleg.png" at Position(yalign=-0.01)
    $ renpy.pause()
    show image "dialogueOleg.png" at Position(yalign=0.22)
    $ renpy.pause()
    show image "dialogueOleg.png" at Position(yalign=0.45)
    $ renpy.pause()
    show image "dialogueOleg.png" at Position(yalign=0.68)
    $ renpy.pause()
    show image "dialogueOleg.png" at Position(yalign=0.85)
    $ renpy.pause()

    play audio "audio/sounds/notification.mp3" volume 0.75
    "{size=*1.5}*Пришло сообщение от Кати*"
    hide image "dialogueOleg.png"
    hide OlegName

    show KateName at namePos zorder 1
    show image "dialogueKate.png" at Position(yalign=0.5)
    $ renpy.pause()

    "{size=*1.5}Похоже, вы должны выбрать, с кем пойти в первую очередь."

    ## Андрей Катя Олег
    ## Андрей Олег Катя
    ## Катя Андрей Олег
    ## Катя Олег Андрей
    ## Олег Андрей Катя
    ## Олег Катя Андрей

    menu:
        "{size=*1.5}Выберите, с кем пойдёте на встречу в первую очередь."
        "{color=#fff}Андрей{/color}":
            hide KateName
            hide image "dialogueKate.png"
            jump AndrewSelected

        "{color=#fff}Катя{/color}":
            hide KateName
            hide image "dialogueKate.png"
        "{color=#fff}Олег{/color}":
            hide KateName
            hide image "dialogueKate.png"

    return

label AndrewSelected:
    show AndrewName at namePos zorder 1
    show image "dialogueAndrew.png" at Position(yalign=0.895)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.95)
    $ renpy.pause()

    hide AndrewName
    hide image "dialogueAndrew.png"
    hide bg

    image AndrewRoom = "ai/room/1.png"

    scene AndrewRoom:
        blur 5

    "{size=*1.5}*Андрей встречает ГГ у себя дома*"
    Andrew "Ну что, абитуриентик, как оно? Пора определяться."
    GG "Да я же говорил уже. Стараюсь для себя. Ну давай, поведай мне о своём студенчестве, трекус."
    Andrew "Ого, как мы заговорили, хех, ладно. В общем, если ты любишь точные науки, такие как математика и, к сожалению, физика, то тут тебе и место, на юрфаке ты больше будешь учить обществознание, право, лево и, внезапно, латынь."
    Andrew "Вообще про работу back-end'ером нам мало что говорили, так что я тут по большей части агитирую тебя поступать, основываясь на твоих интересах. Из языков ты можешь выбрать C# или PHP, да даже Java с Python'ом. А вот на B✞✞ писать реквесты к царю батюшке через код не удасться, увы."
    GG "Ого"

    menu selectQuestion:
        "Класс, а чем бэкендр разработчик занимается на практике?":
            Andrew nerd "Ну, чисто в теории, пишет серверный код, отвечающий за реакцию ресурса на действия пользователя и выдачу информации"
            GG "Huh?"
            Andrew normal "Ну, или простыми словами: ты пишешь внутренности сайта."
            GG "А, всё понял."
            Andrew "Ещё какие-то вопросы?"
            GG "Только не по теме, столько не виделись нормально..."
            "*ГГ хорошо пообщался с Андреем и к 10 часам вечера ушёл домой*"
            jump secondFriendSelect
            $ involvement += 1
        "Думаю, что этих знаний мне должно хватить. Чем вообще занимаешься-то хоть в свободное от учёбы время?":
            "*ГГ хорошо пообщался с Андреем и к 10 часам вечера ушёл домой*"
            jump secondFriendSelect

    menu secondFriendSelect:
        "{size=*1.5}Выберите, с кем пойдёте на встречу во вторую очередь."
        "{color=#a79696}Андрей{/color}":
            jump secondFriendSelect
        "{color=#fff}Катя{/color}":
            jump 
        "{color=#fff}Олег{/color}":