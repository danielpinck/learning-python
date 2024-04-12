import mysql.connector, tabulate


cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='lager_db')
cursor = cnx.cursor()

# Zeigen Sie für jeden Artikel die Artikelnummer und die Bezeichnung dieses Artikels an.
aufgabe1 = ("SELECT a.anr, a.abezeichnung FROM artikel a") 
# Fragt die Bezeichnungen für columns anr und abezeichnung ab
aufgabe1_columns = ("SELECT column_name FROM information_schema.COLUMNS where table_schema = 'lager_db' AND table_name = 'artikel' AND column_name IN('anr', 'abezeichnung')")


cursor.execute(aufgabe1_columns)
for i in cursor:
    print(*i,end="  ", sep="")
print()

cursor.execute(aufgabe1)
for (anr, abezeichnung) in cursor:
    print(f"{str(anr).ljust(4)} {str(abezeichnung).ljust(15)}")


cursor.close()
cnx.close()