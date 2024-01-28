import sqlite3
import sys

def Connect():
    return sqlite3.connect('baza.db')

class Reg():
    name = ""
    passport = ""
    tren = ""
    abonement = ""
    def registration():
        numbers = ["1","2","3","4","5","6","7","8","9","0"]

        while True:
            name = input("введите имя: ")
            tren = input("хотите ли вы заниматься с тренером?\n1.Да\n2.Нет\n")
            match tren:
                case "1":
                    trenirovkistrenerom = "Да"
            match tren:
                case "2":
                    trenirovkistrenerom = "Нет"
            abon = input("на сколько месяцев вы хотите взять абонемент?\n1. 1 месяц\n2. 3 месяца\n3. 6 месяцев\n4. 12 месяцев\n")
            match abon:
                case "1":
                    abonement = "1 месяц"
            match abon:
                case "2":
                    abonement = "3 месяца"
            match abon:
                case "3":
                    abonement = "6 месяцев"
            match abon:
                case "4":
                    abonement = "12 месяцев"
            break
        Database.CreateClient(name, trenirovkistrenerom, abonement)
        print("вы успешно зарегистрированы!")
        Main.main()

class Admin():
    def CheckAdminPassword():
        password = "111"
        a = input("введите пароль: ")
        if a == password:
            Admin.ControlPanel()
        else:
            Main.main()

    def ControlPanel():
        while True:
            chose = input("МЕНЮ:\n1. Показать всех клиентов\n2. Удалить клиента\n3. Поменять абонемент клиенту\n4. Поменять информацию о тренировках с тренером\n5. Выйти\n")
            match chose:
                case "1":
                    Database.ShowAllClients()
                case "2":
                    name = input("введите имя клиента ")
                    Database.KickClientByName(name)
                    print("клиент удален")
                case "3":
                    name = input("введите имя клиента ")
                    abon = input("введите на какой абонемент будете менять:\n1. 1 месяц\n2. 3 месяца\n3. 6 месяцев\n4. 12 месяцев\n")
                    match abon:
                        case "1":
                            abonement = "1 месяц"
                    match abon:
                        case "2":
                            abonement = "3 месяца"
                    match abon:
                        case "3":
                            abonement = "6 месяцев"
                    match abon:
                        case "4":
                            abonement = "12 месяцев"
                    Database.UpdateAbonementByName(name, abonement)
                    print("абонемент обновлен")
                case "4":
                    name = input("введите имя клиента ")
                    trenirovke = input("введите новый статус занятий с тренером: \n1. Установить тренировки с тренером\n2. Убрать тренировки с тренером\n")
                    match trenirovke:
                        case "1":
                            tren = "Да"
                    match trenirovke:
                        case "2":
                            tren = "Нет"
                    Database.UpdateTrainingswithtrenerByName(name, tren)
                    print("тариф изменен")
                case "5":
                    break
        return 0

class Database():
    def CreateTable():
        conn = Connect()
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS Clients(
            Id INTEGER PRIMARY KEY,
            ClientName TEXT NOT NULL,
            Tren TEXT NOT NULL,
            Abonement TEXT NOT NULL
            );
        ''')
        conn.commit()
        conn.close()

    def CreateClient(name, tren, abonement):
        conn = Connect()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO Clients (ClientName, Tren, Abonement) VALUES(?,?,?)', (name, tren, abonement))
        conn.commit()
        conn.close()

    def ShowAllClients():
        conn = Connect()
        cur = conn.cursor()

        cur.execute('SELECT * FROM Clients')
        clients = cur.fetchall()

        for client in clients:
            print(client)

            conn.close()

    def KickClientByName(name):
        conn = Connect()
        cur = conn.cursor()

        cur.execute('DELETE FROM Clients WHERE ClientName = ?', (name))
        conn.commit()
        conn.close()

    def UpdateAbonementByName(name, abonement ):
        conn = Connect()
        cur = conn.cursor()

        cur.execute('UPDATE Clients SET Abonement = ? WHERE ClientName = ?', (abonement, name))
        conn.commit()
        conn.close()


    def UpdateTrainingswithtrenerByName(name, tren):
        conn = Connect()
        cur = conn.cursor()

        cur.execute('UPDATE Clients SET Tren = ? WHERE ClientName = ?', (tren, name))
        conn.commit()
        conn.close()


class Main():
    def main():
        Database.CreateTable()
        chose = input("МЕНЮ:\n1. Зарегистрироваться как обычный пользователь\n2. Войти как админ\n3. Выйти\n")

        match chose:
            case "1":
                Reg.registration()
            case "2":
                Admin.CheckAdminPassword()
            case "3":
                sys.exit()
Main.main()