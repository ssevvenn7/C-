# -*- coding: utf-8 -*-
import random
from time import sleep
import json
import csv


class Player():
    Networth = 1000
    Name = ""
    isNew = 0


def load():
    try:
        with open('jsonsave.json', 'r') as file:
            data = json.load(file)
            Player.Name = data["Name"]
            Player.Networth = data["Networth"]
    except FileNotFoundError:
        print("У вас нет сохранения!")
        Player.IsNew = 1
def save():
    datajson = {"Name": f"{Player.Name}",
                "Networth": f"{Player.Networth}"}

    with open('jsonsave.json', 'w') as file:
        json.dump(datajson, file, indent=4)

    datacsv = [[f'{Player.Name}', f'{Player.Networth}']]
    with open('csvsave.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in datacsv:
            writer.writerow(row)
    exit()


class Sloti():
    def gameworks():

        print("Перед вами стоят несколько игральных автоматов\n1. Поиграть в один из них\n2. Уйти")
        a = int(input())
        if a == 1:
            Sloti.sloti777()
        if a == 2:
            vibor()

    def sloti777():
        elem = ["вишня", "семерочка", "кубик льда", "лимон", "очки", "бомба"]
        result = []

        print(f"сколько ставите? У вас есть {Player.Networth}")
        stavka = float(input())
        Player.Networth -= stavka

        for i in range(3):
            r = random.randint(0,5)
            result.append(elem[r])


        print(f"Результат: ", end="")
        for i in range(3):
            print(result[i] + " ", end="")
        print("\n")

        if result[0] == result[1] == result[2]:
            Player.Networth += (float(stavka) + (float(stavka) * 3.25))
            print(f"вы выиграли, ваш баланс {Player.Networth}")
            Sloti.gameworks()

        if result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            Player.Networth += (float(stavka) * 1.35)
            print(f"вы выиграли, ваш баланс {Player.Networth}")
            Sloti.gameworks()

        else:
            print(f"вы проиграли, ваш баланс {Player.Networth}")
            Sloti.gameworks()


class Roulette:
    stavka_cv = ""
    result = ""
    b = 0
    def gameworks():

        print("Перед вами большая рулетка, красивейший барабан завораживающе крутится\n1. Присоединиться\n2. Уйти")
        a = int(input())
        if a == 1:
            Roulette.stavka()
        if a == 2:
            vibor()
    def stavka():
        print("на что ставите?: \n1.черное\n2.красное\n3.зеро")
        a = float(input())

        print(f"сколько ставите? У вас есть {Player.Networth}")
        Roulette.b = float(input())
        Player.Networth -= Roulette.b


        match a:
            case 1:
                Roulette.stavka_cv = "черная клетка"
            case 2:
                Roulette.stavka_cv = "красная клетка"
            case 3:
                Roulette.stavka_cv = "зеро"
        Roulette.roulette()
    def roulette():

        stavka = Roulette.stavka_cv
        result = Roulette.result
        r = random.randint(0, 100)


        if r <= 49:
            result = "черная клетка"
        if 49 < r <= 98:
            result = "красная клетка"
        if 98 < r <= 100:
            result = "зеро"


        print("рулетка крутится")
        sleep(0.5)
        print("1")
        sleep(0.5)
        print("2")
        sleep(0.5)
        print("3")
        sleep(0.5)


        match result:
            case "черная клетка":
                print("вам выпала черная клетка")
            case "красная клетка":
                print("вам выпала красная клетка")
            case "зеро":
                print("вам выпало зеро")


        if result == stavka:
            if(stavka != "зеро"):
                print("вы выиграли")
                Player.Networth += (float(Roulette.b) * 1.5)

            if(stavka == "зеро"):
                print("вы выиграли")
                Player.Networth += (float(Roulette.b) * 20)
            vibor()

        else:
            print("вы проиграли")
        Roulette.gameworks()

class Blackjack:
    koloda = ["бубновый король", "червовый король", "король треф", "крестовый король",
                "бубновая дама", "червовая дама", "дама треф", "крестовая дама",
                "бубновый валет", "червовый валет", "валет треф", "крестовый валет",
                "бубновый туз", "червовый туз", "туз треф", "крестовый туз",
                "2 буби", "2 черви", "2 крести", "2 треф",
                "3 буби", "3 черви", "3 крести", "3 треф",
                "4 буби", "4 черви", "4 крести", "4 треф",
                "5 буби", "5 черви", "5 крести", "5 треф",
                "6 буби", "6 черви", "6 крести", "6 треф",
                "7 буби", "7 черви", "7 крести", "7 треф",
                "8 буби", "8 черви", "8 крести", "8 треф",
                "9 буби", "9 черви", "9 крести", "9 треф",
                "10 буби", "10 черви", "10 крести", "10 треф",]
    cost = 0
    ruka = []
    dealerCost = 0
    dealerRuka = []
    stavka = 0


    def dealer():
        for i in range(2):
            r = random.randint(0,51)
            if r <= 15:
                Blackjack.dealerCost += 10
            if 15 < r <= 19:
                Blackjack.dealerCost += 2
            if 19 < r <= 23:
                Blackjack.dealerCost += 3
            if 23 < r <= 27:
                Blackjack.dealerCost += 4
            if 27 < r <= 31:
                Blackjack.dealerCost += 5
            if 31 < r <= 35:
                Blackjack.dealerCost += 6
            if 35 < r <= 39:
                Blackjack.dealerCost += 7
            if 39 < r <= 43:
                Blackjack.dealerCost += 8
            if 43 < r <= 47:
                Blackjack.dealerCost += 9
            if 47 < r <= 51:
                Blackjack.dealerCost += 10
            Blackjack.dealerRuka.append(Blackjack.koloda[r])


    def gameworks():
        print("Перед вами большой покерный стол, на нем играют в блекджек\n1. Присоединиться\n2. Уйти")
        a = int(input())
        print(f"сколько ставите? У вас есть {Player.Networth}")
        Blackjack.stavka = float(input())
        Player.Networth -= Blackjack.stavka
        if a == 1:
            Blackjack.game(1)
        if a == 2:
            vibor()


    def game(new):
        if new == 1:
            Blackjack.cost = 0
            Blackjack.dealerCost = 0
            Blackjack.ruka.clear()
            Blackjack.dealerRuka.clear()
        if new == 0:
            new = 0
        r = random.randint(0,51)
        if r <= 11:
            Blackjack.cost += 10
        if 11 < r <= 15:
            Blackjack.cost += 11
        if 15 < r <= 19:
            Blackjack.cost += 2
        if 19 < r <= 23:
            Blackjack.cost += 3
        if 23 < r <= 27:
            Blackjack.cost += 4
        if 27 < r <= 31:
            Blackjack.cost += 5
        if 31 < r <= 35:
            Blackjack.cost += 6
        if 35 < r <= 39:
            Blackjack.cost += 7
        if 39 < r <= 43:
            Blackjack.cost += 8
        if 43 < r <= 47:
            Blackjack.cost += 9
        if 47 < r <= 51:
            Blackjack.cost += 10

        Blackjack.ruka.append(Blackjack.koloda[r])


        print("ваша рука: ", end = "")
        for i in range(len(Blackjack.ruka)):
            print(Blackjack.ruka[i], end = " | ")
        print ("\nЦена руки: " + str(Blackjack.cost))



        if Blackjack.cost == 21:
            print("\nВы выиграли\n")
            Player.Networth += (float(Blackjack) * 2)
            Blackjack.gameworks()

        if Blackjack.cost > 21:
            print("\nВы проиграли\n")
            Blackjack.gameworks()


        print("1. Добираем\n2. Пас")
        a = int(input())
        if(a == 1):
            Blackjack.game(0)
        if(a == 2):
            Blackjack.dealer()


            print("цена руки дилера: " + str(Blackjack.dealerCost))
            if(Blackjack.cost > Blackjack.dealerCost):
                print("\nВы выиграли!\n")
                Player.Networth += (float(Blackjack.stavka) *1.5)
                Blackjack.gameworks()

            if(Blackjack.cost < Blackjack.dealerCost):
                print("\nВы проиграли\n")
                Blackjack.gameworks()

            if(Blackjack.cost == Blackjack.dealerCost):
                print("\nНичья\n")
                Player.Networth += Blackjack.stavka
                Blackjack.gameworks()

        print("вы проиграли")
        return 0


def vibor():
    print(f"Вы стоите посреди большого красивого зала, в ваших карманах находится валюта в размере {Player.Networth}")
    print("Выбор:\n1. Пойти поиграть в блекджек\n2. Словить три поплавских и пойти играть в кубаны\n3. Пойти играть в рулетку\n4. Выйти из игры")
    a = int(input())


    match a:
        case 1:
            Blackjack.gameworks()
        case 2:
            Sloti.gameworks()
        case 3:
            Roulette.gameworks()
        case 4:
            save()


def jelsohr():
    print("Желаете загрузить сохранение при наличии?\n1. Да\n2. Нет")
    a = int(input())
    match a:
        case 1:
            load()
            if Player.isNew == 1:
                return 0
            else:
                print(f"с возвращением, {Player.Name}\n")
                vibor()
        case 2:
            return 0


print("казиныч v f.01\n")
jelsohr()

print("перед началом игры введите своё имя:")
name = input()
Player.Name = name
print("Д", end = "")
sleep(0.1)
print("a", end = "")
sleep(0.1)
print("т", end = "")
sleep(0.1)
print("а", end = "")
sleep(0.1)
print(": ", end = "")
sleep(0.1)
print("н", end = "")
sleep(0.1)
print("е", end = "")
sleep(0.1)
print("и", end = "")
sleep(0.1)
print("з", end = "")
sleep(0.1)
print("в", end = "")
sleep(0.1)
print("е", end = "")
sleep(0.1)
print("с", end = "")
sleep(0.1)
print("т", end = "")
sleep(0.1)
print("н", end = "")
sleep(0.1)
print("а")
sleep(0.1)
print("В", end = "")
sleep(0.1)
print("р", end = "")
sleep(0.1)
print("е", end = "")
sleep(0.1)
print("м", end = "")
sleep(0.1)
print("я", end = "")
sleep(0.1)
print(": ", end = "")
sleep(0.1)
print("н", end = "")
sleep(0.1)
print("е", end = "")
sleep(0.1)
print("и", end = "")
sleep(0.1)
print("з", end = "")
sleep(0.1)
print("в", end = "")
sleep(0.1)
print("е", end = "")
sleep(0.1)
print("с", end = "")
sleep(0.1)
print("т", end = "")
sleep(0.1)
print("н", end = "")
sleep(0.1)
print("о")
sleep(2)


print("Вы стоите у входа в казино, вокруг лишь неизвестный вам тёмный враждебный город")
print("1. Войти в казино")
print("2. Испугавшись закрыть глаза и упасть на землю")
print("Чтобы выбрать действие напишите цифру, ему соответствующую")
a = int(input())


match a:
    case 1:
        print("Вы входите в казино, открыв слегка тяжелые тонированные двери", end = "")
    case 2:
        exit()
print(".", end = "")
sleep(0.1)
print(".", end = "")
sleep(0.1)
print(".")


print("Войдя в казино вы лицезрели ослепляющий свет и рёв, казалось, бесконечного количества игровых автоматов")
print("На входе вас встретил опрятного вида портье, сказав, что гардероб до верха забит куртками и к сожалению у них нет места для вашей")
sleep(1)
print("Но на улице достаточно жарко, какие куртки")
sleep(1)
print("да и на мне ничего нет")
sleep(2)


print("Войдя дальше в казино вы заметили огромное количество слотов, покерных столов и другой типичной для казино аттрибутики")
vibor()