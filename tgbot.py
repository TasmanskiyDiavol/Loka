import telebot
from random import randint

bot = telebot.TeleBot(token="5889190596:AAG6XYaHhGG2p-PKOfNoVR1oUPq7qAMpA-c")

@bot.message_handler(content_types=['text'])
def answer(message):
    global baza
    global adress
    global filtr
    global opisanie
    #global n
    text = message.text
    user = message.chat.id


    if text == "/help":
        bot.send_message(user, r"""Тебе нужна помощь?
/start - Заполнить анкету нового места
/random - Случайная локация
/poisk - Поиск по фильтр(ам)""")
        


    elif text == "/g":
        bot.send_message(user, "https://paste.geekclass.ru/?id=EG1CLT")
    

    elif text == "/start":
        bot.send_photo(user, "https://yandex.ru/images/search?from=tabbar&text=%D1%81%D0%BE%D0%B1%D0%B0%D1%87%D0%BA%D0%B0%20%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0&family=yes&pos=1&img_url=http%3A%2F%2Fadonius.club%2Fuploads%2Fposts%2F2022-06%2F1655597329_7-adonius-club-p-khobotkovaya-sobachka-krasivo-foto-7.jpg&rpt=simage&lr=213")
        answer = bot.send_message(user, "напишите адресс места")
        bot.register_next_step_handler(answer, adr)




    elif text == "/d":
        bot.send_message(user, ','.join(adress))
        bot.send_message(user, ','.join(filtr))
        bot.send_message(user, ','.join(opisanie))


    elif text == "/random":
        if len(adress) == 0 or len(adress) == 1:
            bot.send_photo(user, "https://yandex.ru/images/search?text=%D0%BF%D0%B8%D0%BD%D0%BE%D0%B3%D0%BE%D1%80&from=tabbar&pos=5&img_url=http%3A%2F%2Factivefisher.net%2Fwp-content%2Fuploads%2F8%2F9%2Fe%2F89e511d824140391de7aad1ae12e76d2.jpeg&rpt=simage&lr=213")
            bot.send_message(user, "Пока что нет локаций(")
        else:

            bot.send_photo(user, "https://yandex.ru/images/search?from=tabbar&text=%D0%BF%D0%BE%D0%BB%D0%BE%D1%81%D0%B0%D1%82%D1%8B%D0%B9%20%D1%82%D0%B5%D0%BD%D1%80%D0%B5%D0%BA&family=yes&pos=0&img_url=http%3A%2F%2Fmnogo-krolikov.ru%2Fwp-content%2Fuploads%2F2021%2F01%2Fstriped-malagasy-tenrec.jpg.838x0_q80.jpg&rpt=simage&lr=213")
            a1 = ""
            f1 = ""
            o1 = ""
            while a1 == "" or f1 == "" or o1 == "" or a1 == "\n":
                a = randint(0, len(adress)-1)
                a1 = adress[a]
                f1 =filtr[a]
                o1 = opisanie[a]
            a1 = a1[:(len(a1)-1)]
            f1 = f1[:(len(f1)-1)]
            o1 = o1[:(len(o1)-1)]
            a2 = "Адресс:" + a1
            f2 = "Указанные фильтры:" + f1
            o2 = "Описание:" + o1
            bot.send_message(user, a2)
            bot.send_message(user, f2)
            bot.send_message(user, o2)



    elif text == "/poisk":
            answer = bot.send_message(user, "напишите название фильтра")
            # в ответ на приветствие просим вызвать функцию Sherlok
            bot.register_next_step_handler(answer, Sherlok)



    else:
        bot.send_photo(user, "https://yandex.ru/images/search?text=%D0%B8%D0%BB%D0%B8%D1%81%D1%82%D1%8B%D0%B9%20%D0%BF%D1%80%D1%8B%D0%B3%D1%83%D0%BD&from=tabbar&pos=0&img_url=http%3A%2F%2Fpic.rutubelist.ru%2Fvideo%2F01%2F5b%2F015b8b9a031a258e0b414764f3a8e48d.jpg&rpt=simage&lr=213")
        bot.send_message(user, "Я тебя не понимаю, пропиши '/help', что бы узнать, что я умею")
        print(user, text)



def Sherlok (message):
    user = message.chat.id
    text = message.text
    p = text
    print (p, user)
    s = []
    for i in range (len(adress)):
        e = filtr[i]
        if e.count(p) > 0 and len(s)<= 10:
            s = s + [i]
    for i in range (len(s)):
        s1 = s[i]
        a1 = adress[s1]
        o1 = opisanie[s1]
        f1 = filtr[s1]
        a2 = "Адресс:" + a1
        f2 = "Указанные фильтры:" + f1
        o2 = "Описание:" + o1
        bot.send_message(user, a2)
        bot.send_message(user, f2)
        bot.send_message(user, o2)
    if len(s) == 0:
        bot.send_message(user, "У нас пока что такого нету(")





def adr (message):
    global baza
    user = message.chat.id
    text = message.text
    baza[user] = (text + "|")
    
    answer = bot.send_message(user, "напишите подходящие фильтры")
    # в ответ на приветствие просим вызвать функцию point1
    bot.register_next_step_handler(answer, fil)

def fil (message):
    global baza
    user = message.chat.id
    text = message.text
    baza[user] = (baza[user] + text + "|")
    answer = bot.send_message(user, "напишите описание этой локации")
    # в ответ на приветствие просим вызвать функцию point1
    bot.register_next_step_handler(answer, opis)

def opis (message):
    global baza
    global adress
    global filtr
    global opisanie
    user = message.chat.id
    text = message.text
    baza[user] = (baza[user] + text)
    afo = baza[user]
    afo = afo.split("|")



    a9 = afo[0]
    adress = adress + [a9 + "|"]
    f9 = afo[1]
    filtr = filtr + [f9 + "|"]
    opisanie = opisanie + [afo[2] + "|"]

    with open("adress.txt", "w") as file_adress:
        for i in adress:
            file_adress.write("".join(i) + "\n")

    with open("filtr.txt", "w") as file_filtr:
        for i in filtr:
            file_filtr.write("".join(i) + "\n")

    with open("opisanie.txt", "w") as file_opisanie:
        for i in opisanie:
            file_opisanie.write("".join(i) + "\n")
    bot.send_message(user, "Спасибо за информацию")
    bot.send_photo(user, "https://yandex.ru/images/search?text=%D0%BA%D0%B8%D1%82%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2&family=yes&from=tabbar&pos=0&rpt=simage&img_url=http%3A%2F%2Fgas-kvas.com%2Fuploads%2Fposts%2F2022-09%2F1663253619_1-gas-kvas-com-p-ptitsa-kitoglav-foto-1.jpg&lr=213")
        


baza = {}
adress = []
filtr = []
opisanie = []
adress = open("adress.txt")
adress = (adress.read())
opisanie = open("opisanie.txt")
opisanie = (opisanie.read())
filtr = open("filtr.txt")
filtr = (filtr.read())

adress = adress.split("|")
filtr = filtr.split("|")
opisanie = opisanie.split("|")

#n = len(adress)
bot.polling(none_stop=True)

#ctaroe foto: https://funart.pro/uploads/posts/2021-07/1626378013_8-funart-pro-p-khobotkovaya-sobachka-petersa-zhivotnie-kr-9.jpg
