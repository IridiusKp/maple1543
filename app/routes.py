from flask import render_template
from app import app
import sqlite3

db = sqlite3.connect("data/main.db", check_same_thread=False)
cursor = db.cursor()
isBeta = True


@app.route('/')
@app.route('/index')
def index():
    table = cursor.execute("SELECT id,title,date,value FROM News")

    return render_template(
        "index.html",
        isBeta=isBeta,
        table=table
    )


@app.route('/homework')
def homework():
    table = get_table()

    return render_template(
        "homework.html",
        isBeta=isBeta,
        table=table,
        sortedDays=sorted(table.keys(), key=get_day_number)
    )


def get_table():
    table = {}
    requestResult = cursor.execute(f"SELECT date,id,title,value FROM Homework").fetchall()

    for row in requestResult:
        date = row[0]
        rowId = row[1]
        title = row[2]
        value = row[3]

        if date not in table:
            table[date] = []
        values = table[date]
        values.append([rowId, title, value])

    return table


def get_day_number(key):
    match key:
        case 'Понедельник':
            return 1
        case 'Вторник':
            return 2
        case 'Среда':
            return 3
        case 'Четверг':
            return 4
        case 'Пятница':
            return 5
        case 'Суббота':
            return 6
        case _:
            return 99

