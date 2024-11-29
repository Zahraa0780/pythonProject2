from flask import Flask
import mysql.connector
app = Flask(__name__)
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='zahraa1995',
    autocommit=True
)
@app.route('/kenttä/<icao>')
def haekentantiedot(icao):
    sql = "select name, municipality from airport where ident ='" +icao+"'";
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
           vastaus = {
               "ICAO": icao,
               "Name": rivi[0],
               "municipality":rivi[1]
           }
           return vastaus
    else:
        return {"message": "Airport not found"}
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)