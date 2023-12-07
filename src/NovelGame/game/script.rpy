init:
    $ namePos = Position(xalign=0.519, yalign=1)
    $ involvement = 0
    default friends = set()

# Определение персонажей игры.
define GG = Character("Главный герой")
define Andrew = Character("Андрей", image="Andrew")
define Oleg = Character("Олег", image="Oleg")
define Kate = Character("Катя", image="Kate")

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
    "Andrew/side_andrew_nerd.png"
    zoom 0.45
image Andrew nerd:
    "Andrew/Andrew talking1.png"
    zoom 0.6
image Andrew listening1: 
    "Andrew/Andrew listening1.png"
    zoom 0.6
image Andrew listening2: 
    "Andrew/Andrew listening2.png"
    zoom 0.6
image Andrew talking1: 
    "Andrew/Andrew talking1.png"
    zoom 0.6
image Andrew talking2: 
    "Andrew/Andrew talking2.png"
    zoom 0.6
image Andrew talking3: 
    "Andrew/Andrew talking3.png"
    zoom 0.6
image Andrew talking4: 
    "Andrew/Andrew talking4.png"
    zoom 0.6
image AndrewRoom = "ai/room/2.png"

## Все изображения для части Кати
image Park = "ai/park/1.png"
image Kate fromBack:
    "Kate/Kate fromBack.png"
    zoom 0.5
image Kate talking1:
    "Kate/Kate talking1.png"
    zoom 0.5
image Kate talking2:
    "Kate/Kate talking2.png"
    zoom 0.5
image Kate talking3:
    "Kate/Kate talking3.png"
    zoom 0.5
image Kate greetingsOneHand:
    "Kate/Kate greetingsOneHand.png"
    zoom 0.5
image Kate listening1:
    "Kate/Kate listening1.png"
    zoom 0.5
image Kate listening2:
    "Kate/Kate listening2.png"
    zoom 0.5

## Все изображения для части Олега


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
    
    return

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
        blur 8

#     Андрей:
#     Привествтвие и разговор) стоит прямо, руки согнуты в локтях и упёрты в бока, голова чуть наклонена вправо.
#     слушает) стоит прямо, руки сложены на груди (закрытая поза типа) 
    show Andrew talking1
    "{size=*1.5}*Андрей встречает ГГ у себя дома*"
    Andrew talking1 "Ну что, абитуриентик, как оно? Пора определяться."
    show Andrew listening1
    GG "Да я же говорил уже. Стараюсь для себя. Ну давай, поведай мне о своём студенчестве, трекус."
    Andrew talking2 "Ого, как мы заговорили, хех, ладно."
    Andrew talking3 "В общем, если ты любишь точные науки, такие как математика и, к сожалению, физика, то тут тебе и место, на юрфаке ты больше будешь учить обществознание, право, лево и, внезапно, латынь."
    Andrew talking1 "Вообще про работу back-end'ером нам мало что говорили, так что я тут по большей части агитирую тебя поступать, основываясь на твоих интересах."
    Andrew talking4 "Из языков ты можешь выбрать C# или PHP, да даже Java с Python'ом. А вот на B✞✞ писать реквесты к царю батюшке через код не удасться, увы."
    show Andrew listening2
    GG "Ого"
    show Andrew listening1

    menu:
        "{size=*1.5}О чём хотите поговорить с Андреем?"
        "Класс, а чем бэкендр разработчик занимается на практике?":
            Andrew nerd "Ну, чисто в теории, пишет серверный код, отвечающий за реакцию ресурса на действия пользователя и выдачу информации"
            show Andrew listening2
            GG "Huh?"
            Andrew talking3 "Ну, или простыми словами: ты пишешь внутренности сайта."
            show Andrew listening1
            GG "А, всё понял."
            Andrew talking4 "Ещё какие-то вопросы?"
            show Andrew listening1
            GG "Только не по теме, столько не виделись нормально..."
            "*ГГ хорошо пообщался с Андреем и к 10 часам вечера ушёл домой*"
            call OtherRoom
            jump friendSelectAfterAndrew
            $ involvement += 1
        "Думаю, что этих знаний мне должно хватить. Чем вообще занимаешься-то хоть в свободное от учёбы время?":
            "*ГГ хорошо пообщался с Андреем и к 10 часам вечера ушёл домой*"
            call OtherRoom
            jump friendSelectAfterAndrew
    
    label OtherRoom:
        scene image "ai/room/3.png":
            blur 10
        return

    menu friendSelectAfterAndrew:
        set friends
        "{size=*1.5}С кем пойти следующим?"
        "{color=#fff}Андрей{/color}":
            jump AndrewSelected

        "{color=#fff}Катя{/color}":
            jump KateSelected

        "{color=#fff}Олег{/color}":
            jump OlegSelected

    return

label HideAll:
    hide KateName
    hide dialogueKate
    
    hide OlegName
    hide dialogueOleg

    hide AndrewName
    hide dialogueAndrew

    hide messengerBG
    hide AndrewRoom
    hide image "ai/room/3.png"

    return


label KateSelected:
    call HideAll

    scene messengerBG
    show KateName at namePos zorder 1
    show dialogueKate at Position(yalign=-1.15)
    $ renpy.pause()
    show dialogueKate at Position(yalign=-0.2)
    $ renpy.pause()

    scene Park:
        blur 10

    show Kate fromBack
    "{size=*1.5}*ГГ окликивает Катю, и они начинают разговаривать*"
    Kate talking1 "Привет-привет, сколько лет, сколько зим?"
    show Kate listening1
    GG "Привет, да, прошло не мало времени с нашей последней встречи."
    Kate talking3 "Как дела, давай, давай колись."
    show Kate listening2
    GG "Да вообще отлично. Я вот хочу узнать некоторые вещи по поводу твоей профессии, расскажешь?"
    Kate talking1 "О-ооо, конечно! Что именно тебе рассказать о фронтэнде? Может его отличиях от бэкенда?"
    show Kate listening1
    GG "Стой, а я думал, что ты в бэкенде работаешь. Ну ладно, это тоже будет познавательно, информативно и полезно, так что с радостью выслушаю."
    Kate talking2 "а в-оот, фронтэнд отличается от бэкенда тем, что тут ты стараешься не для других программистов, а для юзеров. Им вообще не важно написан у тебя сайт в 4 метода или в 44, им важен UI, юзер интрефасе, если так удобно, воооот"
    show Kate listening2
    GG "Ого, прикольно!"

    menu:
        "О чём хотите поговорить с Катей?"
        "Я просто думал пойти в бэкенд, но если не получится, то смогу ли я перейти на фронтенд?":
            Kate talking3 "Думаю, что сможешь. В конце концов и фронтэнд и бэкенд можно писать на JavaScript, хоть у этих двух прфессий и разные предназначения, думаю, что ты быстро должен будешь освоиться с переходом."
            show kate listening2
            GG "Ясно."
            jump SecondSelect
        "Думаю, что я всё понял. Пройдёмся?":
            show Kate greetingsOneHand
            "ГГ отлично пообщался с Катей на отвлечённый темы"
            jump friendSelectAfterKate

    menu SecondSelect:
        "О чём ещё хотите поговорить?"
        "А про условия труда есть, что сказать?":
            Kate talking2 "Труда? А, всё более менее, есть сроки и в них нужно укладываться. Что немало важно нужно иметь хорошую фантазию и чувство вкуса, чтобы создавать что-то действительно необычное и красивое."
            show Kate listening1
            GG "Дак это же буквально я."
            Kate talking3 "Ага, Гослинг ты наш, охотно в это верю.  Надеюсь, это не очень всё занудно?"
            show Kate listening1
            GG "Да нет, нет, что ты."
            jump ThirdSelect
        "Думаю, что я всё понял. Пройдёмся?":
            show Kate greetingsOneHand
            "ГГ отлично пообщался с Катей на отвлечённый темы"
            jump friendSelectAfterKate
    
    menu ThirdSelect:
        "О чём ещё хотите поговорить?"
        "А вот ещё, хоть немного и неприлично, но какая зп у фронтэндера?":
            Kate talking1 "Сейчас, дай-ка посчитаю... ммм…  в среднем это 80+ хихи"
            show Kate listening2
            GG "Немало"
            Kate talking3 "Ага, работка не особо пыльная, но освоиться можно и если что, то у тебя обязательно получится."
            show Kate listening1
            GG "Ой, уж прости, но мне в выборе из бэкенда и фронтенда больше импонирует первое, хотя звучало довольно заманчиво."
            Kate talking2 "Я тебя не заставляю, это твой выбор."
            show kate listening2
            GG "Ну на этом я думаю, что по моей теме всё. Ну что, как лето-то хоть проводишь?"
            Kate talking1 "Знаешь..."
            jump friendSelectAfterKate
        "Думаю, что я всё понял. Пройдёмся?":
            show Kate greetingsOneHand
            "ГГ отлично пообщался с Катей на отвлечённый темы"
            jump friendSelectAfterKate
    
    label friendSelectAfterKate:
        call OtherPark
        menu:
            set friends
            "{size=*1.5}С кем пойти следующим?"
            "{color=#fff}Андрей{/color}":
                jump AndrewSelected

            "{color=#fff}Катя{/color}":
                jump KateSelected

            "{color=#fff}Олег{/color}":
                jump OlegSelected
    
    label OtherPark:
        scene image "ai/Park/2.png":
            blur 10
        return
    
    return

