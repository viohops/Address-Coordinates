import sqlite3



def createDB():
    db = sqlite3.connect("settings.db")
    sql = db.cursor()

    sql.execute(
        """CREATE TABLE IF NOT EXISTS preferens (
                    url TEXT,
                    token TEXT,
                    language TEXT

                    )"""
    )

    db.commit()

    url = "https://dadata.ru/"
    token: str
    language: str

    def preferens():
        token = input("Ввкдите API-ключ: ")
        print("1.'ru' \n2.'en'")
        num = int(input("Выбирете язык: "))
        if num == 1:
            language = "ru"
        else:
            language = "en"
        return token, language

    token, language = preferens()

    sql.execute("SELECT language FROM preferens")

    sql.execute(f"INSERT INTO preferens VALUES (?, ?, ?)", (url, token, language))
    db.commit()

    for value in sql.execute("SELECT * FROM preferens"):
        responnce = value
    token = responnce[1]
    language = responnce[2]
    return token, language


def dataBase():
    db = sqlite3.connect("settings.db")
    sql = db.cursor()
    for value in sql.execute("SELECT * FROM preferens"):
        responnce = value
    token = responnce[1]
    language = responnce[2]

    return token, language
