import mysql.connector
import matplotlib.pyplot as plt

LOCALHOST = '127.0.0.1'
USERNAME = 'root'
PASSWORD = '*********'
DATABASE = 'online_retail'

con = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=LOCALHOST, database=DATABASE)
cursor = con.cursor()

cursor.execute('SELECT Country, SUM(Price) AS p FROM registers' +
               ' WHERE Price >= 1200' +
               ' GROUP BY Country' +
               ' ORDER BY p' +
               ' LIMIT 7;')

query = cursor.fetchall()

listaNomes = [i[0] for i in query]
listaVal = [i[1] for i in query]

fig, ax = plt.subplots()
ax.pie(listaVal, labels=listaNomes, autopct='%1.1f%%', radius=1.3)
plt.show()
