# Setup
yes_no = ["да", "нет", "мяу"]
directions = ["1", "2", "3", "4", "5"]
import time
 
# Introduction
name = input("Как тебя зовут, котик? ")
print("Здравствуй, " + name + "! Пойдем на квест!")
print("Но сначала нам надо проверить, настоящий ли ты котик.")
print("Предупреждаю: тебе нас не обмануть!")

# Start of game
response = ""
while response not in yes_no:
    print("Все нормально?")
    response = input()
    if response == "да":
        print("Ты не настоящий котик.")
        quit()
    elif response == "нет":
        print("Ты не настоящий котик.")
        quit()
    elif response == "мяу":
        print("Ты настоящий котик! Мяу!")
    else: 
        print("Я не понимаю это.")



# First part of game
response = ""
location = "none"
while response not in directions:
    print("Ты на пороге темной комнаты. Что будешь делать? (выбери цифру)")
    print("1. Эээ... Ничего.")
    print("2. Пойду посплю перед приключениями. Да и перекусить давно пора...")
    print("3. Сяду и буду гипнотизировать темноту взглядом.")
    print("4. Развернусь и...ВПЕРЕЕЕЕЕД!!!!!!!!!!! (на поиски хозяина. пусть включит свет.)")
    print("5. Просто зайду в комнату.")
    response = input(" ") 
    if response == "1":
        print("Ок'ей. А дальше?")
        location = "none"
        response =""
        time.sleep(3)
    elif response == "2":
        print("Мудрое решение настоящего котика! Тогда спокойной ночи, приятного аппетита и до новых	встреч!")
        quit()
    elif response == "3":
        print("Ты выполнил вышесказанное и спокойно уселся на пол...")
        location = "sit"
    elif response == "4":
        print("Самое логичное решение! Ты быстро нашёл хозяина и попытался оторвать его от созерцания коробки под названием телевизор. Не получилось. Что дальше?")
        location = "master"
    elif response == "5":
        print("Ты зашел в комнату.")
        location = "room"
    else:
        print("Я не понимаю это.")

# Third part of game
if location == "none":
    #
  while response not in directions:
    print(" (выбери цифру)")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. )")
    print("5. ")
    response = input(" ") 
    if response == "1":
        print("Ок'ей. А дальше?")
        location = "none"
    elif response == "2":
        print("Мудрое решение настоящего котика!Тогда спокойной ночи, приятного аппетита и до новых	встреч!")
        quit()
    elif response == "3":
        print("Ты выполнил вышесказанное и спокойно уселся на пол...")
        location = "sit"
    elif response == "4":
        print("Самое логичное решение! Ты быстро нашёл хозяина и попытался оторвать его от созерцания коробки под названием телевизор. Он встал и пошёл за тобой. Включив свет в ванной, людь с упреком взглянул на тебя и пошел дальше пялится в коробку.")
        location = "room"
    elif response == "5":
        print("Ты зашел в комнату.")
        location = "room"
    else:
        print("Я не понимаю это.")
elif location == "sit":
    s="Ты сидишь возле двери. Ты сидишь возле двери. Ты...да. Ты все еще сидишь возле двери. Наконец, тебе надоело ждать, и ты..."
    ls = s.split(".")
    for i in ls:
        time.sleep(2)
        print(i, end='.')
elif location == "room":
  print("Оглядевшись по сторонам, ты заметил какую-то странную штуку. У неё было странной формы желтое тело с какими-то странными, рефлёными, боками и круглая голова с длинным рыжим...эээ... Короче говоря, обычная резиновая уточка. Ты задумчиво тронул игрушку лапой и аж подпрыгнул от неожиданности, когда она вдруг заорала так, что уши заложило. Точнее, запищала. Твои действия?")
  print("1. Подобраться и, выразительно шипя, занять угрожающую позу.")
  print("2.")
  print("")
