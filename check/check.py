from app import app
from flaskext.mysql import MySQL
import pymysql
from app import app
from flask import jsonify
from flask import flash, request
import json

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'demandes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/check', methods=['POST'])
def demandes():
    try:
        _json = request.json
        _NIN = _json['NIN']
        if _NIN and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "SELECT COUNT(NIN) FROM demandes WHERE NIN = %s"
            bindData = (_NIN)
            cursor.execute(sqlQuery, bindData)
            records = cursor.fetchall()
            conn.commit()
            respone = jsonify(records[0])
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
    app.run(debug=True,port=5008)

