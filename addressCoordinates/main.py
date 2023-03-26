from dadata import Dadata
import os
import dataBase as db


def preferens():
    """Функция создает файл с БД и записывает пользовательские настройки
    или берет их из уже имеющегося файла с БД
    и возвращает (записывает и возвращает) API и язык
    на котором программа будет возвращать ответ
    """
    token: str
    language: str
    if os.path.exists("settings.db"):
        token, language = db.dataBase()
    else:
        token, language = db.createDB()
    return token, language


def inputAddress():
    """Принимает данные от польхователя и возвращает их"""
    address: str = input("Введите адрес: ")
    return address


def responceDadata(address: str, count: int, TOKEN: str, language: str):
    """Функция принимает данные с адресом, настройками и возвращает список словарей
    Кол-во словарейй ограничено переменной <count>  которая задается в главной функции
    """
    token = TOKEN
    dadata = Dadata(token)
    result = dadata.suggest("address", address, count=count, language=language)
    if result == []:
        print("К сожалению по вашему запросу ничего не найдено. \nПопроуйте еще раз...")
        main()
    else:
        return result


def getAllAdresses(result: list):
    """Функция принимает список со словарями и возвращает список
    со значениями (адреса) по ключу ['unrestricted_value']
    """
    addres: list = []
    for i in result:
        for key, value in i.items():
            if key == "unrestricted_value":
                addres.append(value)
    return addres


def getTheCoordinates(result: list):
    """Функция получает список в котором содержится словарь с данными по адресу
    и достает полный адрес и координаты (долгота, широта)
    возвращает список с этими данными"""
    addres: list = []
    for i in result:
        for key, value in i.items():
            if key == "unrestricted_value":
                addres.append(value)

            elif key == "data":
                for k, v in value.items():
                    if k == "geo_lat":
                        addres.append(v)
                    elif k == "geo_lon":
                        addres.append(v)
    return addres


def printRecponse(address: list):
    """Функция принимает список с адресами и выводит их в конслосль построчно"""
    count: int = 1
    for i in address:
        print(f"{count}. {i}")
        count += 1


def selectTheCorrectAdress(address: list):
    """Функция принимает список с адресами
    пользователь выбирает один из них
    и функция возвращает его"""
    num: int
    try:
        num = int(input("Выберите один из адресов: "))
        return address[num - 1]
    except (ValueError, IndexError):
        print("Попробуйте снова: ")
        num = int(input("Выберите один из адресов: "))

    finally:
        return address[num - 1]


def main():
    tokken: str
    language: str
    tokken, language = preferens()
    count: int = 5
    address: str = inputAddress()
    result: list = responceDadata(address, count, tokken, language)
    recponceAddress: list = getAllAdresses(result)
    printRecponse(recponceAddress)
    address = selectTheCorrectAdress(recponceAddress)
    count: int = 1
    result: list = responceDadata(address, count, tokken, language)
    recponceAddress: list = getTheCoordinates(result)
    printRecponse(recponceAddress)
    progress: str = input('Продолжить работу в программе: "Y" - да, "N" - выйти: ')

    if progress.lower() == "y" or progress.lower() == "н":
        main()


if __name__ == "__main__":
    main()
