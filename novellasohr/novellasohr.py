# -*- coding: cp1251 -*-
import os
import json
import csv
def convert_response(response): 
    if response == "да" or response == "lf":
        return 1
    elif response == "да" or response == "Lf":
        return 1
    elif response == "yes" or response == "Нуы":
        return 1
    elif response == "yes" or response == "нуы":
        return 1
    elif response == "нет" or response == "ytn":
        return 2
    elif response == "Нет" or response == "Ytn" or response == "нЕТ" or response == "yTN":
        return 2
    elif response == "НЕТ" or response == "YTN":
        return 2
    elif response == "No" or response == "Тщ" or response == "nO" or response == "тЩ":
        return 2
    elif response == "no" or response == "тщ":
        return 2
    elif response == "NO" or response == "ТЩ":
        return 2
def wait_for_enter():
    input("Нажмите Enter для продолжения...")
def checkint():
    while True:
        try:
            input_data = int(input())
            return input_data
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
          
def save_data(person):
    with open('save_file.json', 'w') as file:
        json.dump(person, file)

def load_data():
    if os.path.exists('save_file.json'):
        with open('save_file.json', 'r') as file:
            return json.load(file)
    else:
        return None

def delete_save():
    if os.path.exists('save_file.json'):
        os.remove('save_file.json')
        print("Сохранение успешно удалено.")
    else:
        print("Сохранение не найдено.")

def save_to_csv(person):
    fieldnames = ['name', 'age', 'weapon', 'bronya', 'Klass']
    if not os.path.exists('game_data.csv'):
        with open('game_data.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            

person = {"name": "???", "age": "???", "weapon": "???", "bronya": "???", "Klass": "???", "???": 0}

print("1.Новая игра")
print("2.Загрузить сохранение")
print("3.Удалить сохранение")
while True:
    print("Введите номер выбора:")
    nachalo = checkint()
    if nachalo == 1:
        break
    if nachalo == 2:
        person = load_data()
        break
    if nachalo == 3:
        delete_save()
        break
    else:
        print("Странно, но этот вариант не приходит в голову")
            
if person["???"] == 0:
    print('Terraria part 1\n')
    print('Вступление')
    print('Вы попадаете в необычайный мир, который вы не помните или не знаете.может быть вы были великим человеком.')
    print('Единственное, что ты знаешь... это твоё существование. Ты есть и являешься обычным человеком.')
    print('Также вы заметили, что имеете при себе ржавый меч, кирку и удивительно топор.')
    print('Вы видите зелёные луга вместе с лесом, солнце и одинокий огромный домик, похожий на крепость. Там вы находите гида. Странно, но его так и зовут.')
    print('Он сам не знает зачем ты тут, но говорит,что ты нужен этому миру, чтобы спасти его от неминуемой гибели!!!')
    print('Гид разрешил жить у себя, а также сказал, что будет помогать вам.')
    wait_for_enter()
    print('Позже вы решили чуть-чуть посидеть на свежем воздухе и помечтать.')
    print('И в один момент вы чувствуете странное чуство и вы резко задумались над тем, кто же вы такой.')
    print('Вы долго думали, но вспомнили только одно имя.')
    name = str(input("Введите имя: "))
    person["name"] = name
    person["???"] = 1
    save_data(person)
if person["???"] == 1:
    print('Ну и недолго думая, вы решаете назвать себя этим именем.')
    print('Теперь вы ' + name)
    print('Но и не только это вас беспокоило')
    print('Вы задумались о родителях. Кем же они были?')
    wait_for_enter()
    print('У вас было много вариантов и вы остановились на самых опасных:')
    print('1.Воин')
    print('2.Лучник')
    print('3.Маг')
    while True:
        print("Введите номер класса:")
        klasvibor = checkint()
        if klasvibor == 1:
            klas = str("Воин")
            break
        if klasvibor == 2:
            klas = str("Лучник")
            break
        if klasvibor == 3:
            klas = str("Маг")
            break
        else:
            print("Странно, но этот вариант не приходит в голову")
    person["Klass"] = klas
    person["???"] = 2
    save_data(person)
    print("Теперь вы " + klas + ".")
    print("Судьба была сделанна. Вы думете, что это ваше призвание.")
    wait_for_enter()

if person["???"] == 2:
    print("\nЧасть ???")
    print("Вам любопытен этот мир, но при этом и страшен.")
    print("Но всё таки вам больше любопытно и вы решили немного изучить этот странный и неизведанный мир")
    print("Вы ходите по округе. Пока на горизонте виднеются тёмные и глубокие пещеры, но пока вы не решаетесь туда пойти.")
    print("На удивление смена геолокации очень сильно меняет климат:\n Вы увидели пустыню, снег и какой-то странная и непонятная территория... Вы назвали её порчей ")
    print("Воздух там был достаточно тяжёлый и летали непонятные, странные и в то же время ужасающие существа, а трава была вообще мёртвой")
    wait_for_enter()
    print("При виде их вы сразу убежали в ужасе")
    print("Отойдя подальше вы успокоились и побежали лёгким бегом, но в итоге споткнулись об что-то мягкое")
    print("Оно было похоже на сгусток слизи... И вы его так и назвали... слизняк")
    print("Этот так назывемый слизняк был вроде дружелюбным и очень слабым, но стоило вам его пнуть он как-то начал много двигаться и пытаться вам навредить.")
    print("На удивление это было больно. Вы на панике ещё пару раз его попинали и итоге слизь умерла")
    print("Ну и вы чуть того... почти...Но вы были рады выжить")
    wait_for_enter()
    print("После этого вы задумались насчёт снаряжения")
    print("Раз вы " + person["Klass"] + " " + person["name"] + " то для начала нужно сделать броню и хоть какое-то оружие получше")
    print("Вы начали думать из чего же сделать броню, вспоминая при этом недавние похождения")
    print("В лесу деревья, в пустыне... кактусы? В снежном биоме тоже деревья. Про порчу вы даже думать не хотели.")
    wait_for_enter()
    print("Можно так же посоветоваться с гидом. Но советоваться ли с ним?")
    broni = ["кактусовая броня","броня из снежного дерева","деревянная броня"]
    while True:
        print("Введите ответ буквами:")
        cer = str(input())
        otveta = convert_response(cer)
        if otveta == 1:
            print("Гид вам посоветовал вам сделать броню из кактуса. Колючее, но на удивление достаточно прочное.")
            print("Вы её и решили сделать")
            person["bronya"] = broni[0]
            break
        if otveta == 2:
            print("Вы решаете выбрать броню сами")
            print("Выбрать самому или же на рандом?")
            print("1.Дерево")
            print("2.Кактус")
            print("3.Снежное дерево")
            print("4.Рандом")
            while True:
                print("Введите номер выбора:")
                vibor1 = checkint()
                if vibor1 == 1:
                    person["bronya"] = broni[2]
                    break
                if vibor1 == 2:
                    person["bronya"] = broni[0]
                    break
                if vibor1 == 3:
                    person["bronya"] = broni[1]
                    break
                if vibor1 == 4:
                    person["bronya"] = broni.pop()
                    print("Вы в итоге выбрали" + person["bronya"])
                    break
                else:
                    print("Странно, но этот вариант не приходит в голову")
                break
            break
    print("После некоторого количесво времени вы сделали себе броню по размеру")
    wait_for_enter()
    person["???"] = 3
    save_data(person)
    
if person["???"] == 3:
    print("После этого вы устали и пошли к гиду и он пока вы добывали ресурсы нашёл интересное оружие")
    wait_for_enter()
    if person["Klass"] == "Воин":
        print("Гид вам даёт интересный, но хороший меч Зенит")
        person["weapon"] = "Зенит"
    if person["Klass"] == "Маг":
        print("Гид вам даёт призму. Странная стекляшка, но с мощной боевой мощью")
        person["weapon"] = "призма"
    if person["Klass"] == "Лучник":
        print("Гид вам даёт безымянный лук. Выглядит стильно и мощно")
        person["weapon"] = "безымянный лук"
    person["???"] = 4
    save_data(person)
    wait_for_enter()
    
if person["???"] == 4:
    print("Вы спокойно покидаете дом Гида, но теряете сознание на пороге. Ваше тело стало крайне тяжёлым.")
    print("И просыпаетесь вы в аду. Вы думаете, что вы умерли, но снаряжение было при вас и вы сделали вывод, что вы живы.")
    print("Звучит очевидно")
    wait_for_enter()
    print("Но вашему покою помешала странная стена, похожая из плоти, с огромным ртом и большими глазами")
    print("Она шла медленно, но уверено. Вы почувствовали угрозу от этой стены и начали убегать паралельно отбиваясь свом оружием")
    print("Она из-за ваших ударом начала ускоряться и вы естественно тоже")
    print("Вы разменялись несколькими десятками или сотками ударов и в итоге она умерла и остановилась.")
    wait_for_enter()
    if person["bronya"] == "кактусовая броня":
        print("Это была легкая победа. Вы даже особо не устали.")
    else:
        print("Это была тяжёлая победа. Вы чуть не умерли и ваша броня сломалась.")
    print("Из стенки плоти вылезло что-то похожее на серце.")
    print("Вы подощли к этому нечто и начали рассматривать.")
    print("В итоге вы решили прикоснуться к этому предмету и вас накрыло ударной волной")
    wait_for_enter()
    print("Конец")
    save_to_csv(person)

