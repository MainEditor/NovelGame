﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define MainCharacter = Character("Главный герой (Слава)")
define Andrey = Character("Андрей")
define plotNarrator = Character("")
define Oleg = Character("Олег")
define Kate = Character("Катя")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    MainCharacter "Наконец-то спустя 10 месяцев этого ада я свободен, больше никаких бесконечных вопросов про административные и уголовные правонарушения и никаких больше изменений строк через реплейс."

    Andrey "Поздравляю, все там были. Ты хоть уже определился, ты всё-таки пойдёшь на юрфак или в IT на бэкенд, как ты мечтал?"

    MainCharacter "{size=*0.9}В принципе с одной стороны я бы не хотел расстраивать родственников, что вот до меня было 3 поколения юристов, а я, вдруг такой-сякой, юристом быть не хочу, но с другой стороны, я понимаю, что вот эта вот вся юриспреденция - это вот вообще не моё. Я ЕГЭ-то по обществу с божьей помошью сдал."
    MainCharacter "{size=*0.9}Я чуть не утонул во всех этих терминах и законах, пока готовился, но меня упорно не слушают, а информатику мне даже очень понравилось писать. Это как-будто бы моё. Честно, я бы ещё хотел поспрашивать у друзей и у тебя в том числе, насчёт обучения на бэкенд разработчика побольше. А то ты знаешь какая у меня ситуация, если мне не удасться убедить родню, что я разбираюсь и действительно хочу и..."

    plotNarrator "{size=*1.5}*Андрей перебивает Славу*"

    Andrey "В IT, да-да, тебя заставят идти на юриста. Ты много раз нам это уже рассказывал. Плюсом я помню, с каким трудом тебе удалось убедить их, что юристами мир не ограничивается."

    MainCharacter "Damn, я настолько часто это рассказывал, что ты уже можешь за меня закочить мою же фразу?"

    Andrey "Cлишком часто, но не суть. Лично я готов помочь тебе, кстати, в следующий понедельник, вторник и среду я как раз вернусь в город, так что можем встретиться, расскажу тебе о всех прелестях студента вуза информационных технологий."

    MainCharacter "А что, звучит. Отличная идея. Ш-шпасибо. Сейчас спрошу других, смогут ли они помочь мне."

    Andrey "Окей, только вот от Олега молниеносного ответа вообще не жди. Он же всё-таки работяга, понимаешь, весь в работе. В общем спишемся тогда ещё. Удачи!"

    MainCharacter "Да знаю я о его среднем времени отклика. Давай пока тогда, тебе тоже удачки."

    plotNarrator "{size=*1.5}*Слава пишет другу Олегу, с которым тоже немало знаком.*"

    MainCharacter "Привет, Олег, я тут думаю о возможности поступления в вуз на айти специальность, думаю выйти в back-end разработку. Ты же вроде как раз в этой специальности работаешь, не расскажешь, что да как там у вас?"

    plotNarrator "{size=*1.5}*Слава решил написать ещё своей подруге Кате.*"

    MainCharacter "Привет, Кать, я вот начинаю потихоньку решаться на поступление в айти вуз, чтобы уйти потом в back-end. Собственно, не объяснишь мне что да как там, ты же вроде тоже из back-end разработчиков? Буду безгранично благодарен."

    play audio "audio/sounds/notification.mp3" volume 0.75
    plotNarrator "{size=*1.5}*Пришло сообщение от Олега.*"

    Oleg "Привет, Слав, а я всегда знал, что ты, так сказать, покатишься с нами по этой наклонной плоскости, xD. Смотри, на неделе я занят, так что, увы, нам не встретиться, но вот в эти выходные я совсем-таки не занят. Так что валяй, я не против. Только напиши, где и когда."

    MainCharacter "А ты быстро, даже не похоже на тебя. Чё, как дела, как сам?"

    Oleg "А кто знает, может я специально обычно мариную твои сообщения подольше, чтобы обидней было?"
    Oleg "Да шучу я, всё нормально, просто конкретно в данный промежуток времени у меня перерыв."

    MainCharacter "A, ясно, ну я тогда вечерочком сегодня напишу тебе, где и когда лучше встретиться."
    Oleg "Окей."

    play audio "audio/sounds/notification.mp3" volume 0.75
    plotNarrator "{size=*1.5}*Пришло сообщение от Кати.*"

    Kate "Круто, скажи где и когда встречаемся!"

    plotNarrator "Похоже, вы должны выбрать, с кем пойти в первую очередь."

    ## Андрей Катя Олег
    ## Андрей Олег Катя
    ## Катя Андрей Олег
    ## Катя Олег Андрей
    ## Олег Андрей Катя
    ## Олег Катя Андрей
,
    menu selectFriend:
        "Выберите, с кем пойдёте на встречу."
        "Андрей":
            plotNarrator "Вы выбрали смерть!"
        "Катя":
            plotNarrator "Вы выбрали смерть!"
        "Олег":
            plotNarrator "Вы выбрали смерть!"
        

    

    return
