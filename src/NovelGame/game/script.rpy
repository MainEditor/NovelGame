# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define MainCharacter = Character("Главный герой")
define Andrey = Character("Андрей")
define Oleg = Character("Олег")
define Kate = Character("Катя")

image white = "bg.png"

# Игра начинается здесь:
label start:

    scene white

    #show image "GG1.png" at center
    #$ renpy.pause()
    #show image "GG1.png":
    #    #xalign 0.5 + renpy.image_size("GG1.png")[0]
    #    xalign 0.5 yalign 0
#
    #show image "A1.png" at center
    #$ renpy.pause()
    #show image "GG2.png" at center
    #$ renpy.pause()

    show image "dialogueAndrew.png" at Position(yalign=-0.27)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=-0.16)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.25)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.393)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.485)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.65)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.75)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.869)
    $ renpy.pause()
    show image "dialogueAndrew.png" at Position(yalign=0.99)
    
    "{size=*1.5}*Слава пишет другу Олегу, с которым тоже немало знаком*"
    window hide
    hide image "dialogueAndrew.png"

    show image "ToOleg.png" at truecenter
    $ renpy.pause()

    "{size=*1.5}*Слава решил написать ещё своей подруге Кате*"
    hide image "ToOleg.png"

    show image "ToKate.png" at truecenter
    $ renpy.pause()
#
    play audio "audio/sounds/notification.mp3" volume 1.0
    "{size=*1.5}*Пришло сообщение от Олега*"
    hide image "ToKate.png"

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

    show image "dialogueKate.png" at Position(yalign=0.5)
    $ renpy.pause()

    "{size=*1.5}Похоже, вы должны выбрать, с кем пойти в первую очередь."
    hide image "dialogueKate.png"

    ## Андрей Катя Олег
    ## Андрей Олег Катя
    ## Катя Андрей Олег
    ## Катя Олег Андрей
    ## Олег Андрей Катя
    ## Олег Катя Андрей

    menu selectFriend:
        "{size=*1.5}Выберите, с кем пойдёте на встречу в первую очередь."
        "Андрей":
            "Вы выбрали смерть!"
        "Катя":
            "Вы выбрали смерть!"
        "Олег":
            "Вы выбрали смерть!"

    return