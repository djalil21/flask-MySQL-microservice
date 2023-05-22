from app import app
from flaskext.mysql import MySQL
import pymysql
from app import app
from flask import jsonify
from flask import flash, request

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'demandes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/demande', methods=['POST'])
def demandes():
    try:
        _json = request.json
        _NIN = _json['NIN']
        _nom = _json['nom']
        _prenom = _json['prenom']
        _email = _json['email']
        _tel = _json['tel']
        if _NIN and _nom and _prenom and _email and _tel and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO demandes(NIN, nom, prenom, email, tel) VALUES(%s, %s, %s, %s,%s)"
            bindData = (_NIN, _nom, _prenom, _email, _tel)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('a')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run(port=5001,debug=True)

