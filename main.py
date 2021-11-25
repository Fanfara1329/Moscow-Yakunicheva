import sqlite3

a_min = int(input())
a_max = int(input())
con = sqlite3.connect('business.db')
cur = con.cursor()
qwerty_1 = cur.execute("""SELECT depth FROM Water
    WHERE salinity >= ? and depth <= ?""", (a_min, a_max)).fetchall()
dict = {}
for i in qwerty_1:
    lst = cur.execute("""SELECT location FROM Water
    WHERE salinity >= ? and depth = ?""", (a_min, *i, )).fetchall()

    dict[str(i[0])] = sorted([str(i[0]) for i in lst])

print(dict)