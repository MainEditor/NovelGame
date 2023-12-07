init:
    $ namePos = Position(xalign=0.519, yalign=1)
    $ involvement = 0
    default friends = set()

# Определение персонажей игры.
define GG = Character("Главный герой")
define Andrew = Character("Андрей", image="Andrew")
define Oleg = Character("Олег")
define Kate = Character("Катя")

# Определение изображений
## Все изображения для мессенджера
image messengerBG = "messenger.png"

image AndrewName = "AndrewName.png"
image dialogueAndrew = "dialogueAndrew.png"

image KateName = "KateName.png"
image dialogueKate = "dialogueKate.png"

image OlegName = "OlegName.png"
image dialogueOleg = "dialogueOleg.png"



## Все изображения для части Андрея
image side Andrew nerd:
    "side_andrew_nerd.png"
    zoom 0.55
image AndrewRoom = "ai/room/1.png"

# Игра начинается здесь:
label start:

    scene messengerBG

    show AndrewName at namePos zorder 1
    show dialogueAndrew at Position(yalign=-0.22)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=-0.135)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=0.2)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=0.325)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=0.4)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=0.545)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=0.625)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=0.725)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=0.805)
    $ renpy.pause()
    
    "{size=*1.5}*Слава пишет другу Олегу, с которым тоже немало знаком*"
    window hide
    hide dialogueAndrew
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
    show dialogueOleg at Position(yalign=-0.2)
    $ renpy.pause()
    show dialogueOleg at Position(yalign=-0.01)
    $ renpy.pause()
    show dialogueOleg at Position(yalign=0.22)
    $ renpy.pause()
    show dialogueOleg at Position(yalign=0.45)
    $ renpy.pause()
    show dialogueOleg at Position(yalign=0.68)
    $ renpy.pause()
    show dialogueOleg at Position(yalign=0.85)
    $ renpy.pause()

    play audio "audio/sounds/notification.mp3" volume 0.75
    "{size=*1.5}*Пришло сообщение от Кати*"
    hide dialogueOleg
    hide OlegName

    show KateName at namePos zorder 1
    show dialogueKate at Position(yalign=-2.75)
    $ renpy.pause()

    "{size=*1.5}Похоже, вы должны выбрать, с кем пойти в первую очередь."

    ## Андрей Катя Олег
    ## Андрей Олег Катя
    ## Катя Андрей Олег
    ## Катя Олег Андрей
    ## Олег Андрей Катя
    ## Олег Катя Андрей

    menu:
        set friends
        "{size=*1.5}Выберите, с кем пойдёте на встречу в первую очередь."
        "{color=#fff}Андрей{/color}":
            jump AndrewSelected

        "{color=#fff}Катя{/color}":
            jump KateSelected

        "{color=#fff}Олег{/color}":
            jump passLabel

label AndrewSelected:
    call HideAll

    scene messengerBG

    show AndrewName at namePos zorder 1
    show dialogueAndrew at Position(yalign=0.895)
    $ renpy.pause()
    show dialogueAndrew at Position(yalign=0.95)
    $ renpy.pause()

    hide AndrewName
    hide dialogueAndrew
    hide bg

    scene AndrewRoom:
        blur 25

    "{size=*1.5}*Андрей встречает ГГ у себя дома*"
    Andrew "Ну что, абитуриентик, как оно? Пора определяться."
    GG "Да я же говорил уже. Стараюсь для себя. Ну давай, поведай мне о своём студенчестве, трекус."
    Andrew "Ого, как мы заговорили, хех, ладно. В общем, если ты любишь точные науки, такие как математика и, к сожалению, физика, то тут тебе и место, на юрфаке ты больше будешь учить обществознание, право, лево и, внезапно, латынь."
    Andrew "Вообще про работу back-end'ером нам мало что говорили, так что я тут по большей части агитирую тебя поступать, основываясь на твоих интересах. Из языков ты можешь выбрать C# или PHP, да даже Java с Python'ом. А вот на B✞✞ писать реквесты к царю батюшке через код не удасться, увы."
    GG "Ого"

    menu selectQuestion:
        "{size=*1.5}О чём хотите поговорить с Андреем?"
        "Класс, а чем бэкендр разработчик занимается на практике?":
            Andrew nerd "Ну, чисто в теории, пишет серверный код, отвечающий за реакцию ресурса на действия пользователя и выдачу информации"
            GG "Huh?"
            Andrew normal "Ну, или простыми словами: ты пишешь внутренности сайта."
            GG "А, всё понял."
            Andrew "Ещё какие-то вопросы?"
            GG "Только не по теме, столько не виделись нормально..."
            "*ГГ хорошо пообщался с Андреем и к 10 часам вечера ушёл домой*"
            jump friendSelectAfterAndrew
            $ involvement += 1
        "Думаю, что этих знаний мне должно хватить. Чем вообще занимаешься-то хоть в свободное от учёбы время?":
            "*ГГ хорошо пообщался с Андреем и к 10 часам вечера ушёл домой*"
            jump friendSelectAfterAndrew

    menu friendSelectAfterAndrew:
        set friends
        "{size=*1.5}Выберите, с кем пойдёте на встречу во вторую очередь."
        "{color=#fff}Андрей{/color}":
            jump AndrewSelected

        "{color=#fff}Катя{/color}":
            jump KateSelected

        "{color=#fff}Олег{/color}":
            jump OlegSelected

label HideAll:
    hide KateName
    hide dialogueKate
    
    hide OlegName
    hide dialogueOleg

    hide AndrewName
    hide dialogueAndrew

    hide messengerBG
    hide AndrewRoom

    return


label KateSelected:
    call HideAll

    scene messengerBG
    show KateName at namePos zorder 1
    show dialogueKate at Position(yalign=-1.15)
    $ renpy.pause()
    show dialogueKate at Position(yalign=-0.2)

    $ renpy.pause()