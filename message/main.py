import pymysql
import requests
import json
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/demande',methods=['POST'])
def create_demandes():
    try:
        _json = request.json
        _NIN = _json['NIN']
        _nom = _json['nom']
        _prenom = _json['prenom']
        _email = _json['email']
        _tel = _json['tel']
        paras={"NIN": _NIN,"nom":_nom,"prenom": _prenom,"email": _email,"tel":_tel}
        check=requests.post(url="http://127.0.0.1:5008/check",json={"NIN":_NIN})
        if check.text=="{\n  \"COUNT(NIN)\": 1\n}\n":
            return "deja demander"
        else:
            requests.post(url="http://127.0.0.1:5001/demande",json=paras)
            civil=requests.post(url="http://127.0.0.1:5007/civil",json=paras)
            if civil.text=='{\n  \"COUNT(NIN)\": 1\n}\n':
                judicaire=requests.get(url="http://127.0.0.1:5002/judicaire/"+_NIN)
                if judicaire.text=="{\"j\":1}\n":
                    surte=requests.get(url="http://127.0.0.1:5003/surte/"+_NIN)
                    if surte.text=="{\"s\":1}\n":
                        return "salut "+_nom+" "+_prenom+" votre passport sera pret"
                    else:
                        return "votre etat surte ne vous permet pas de passport"    
                else:
                    return "votre casier judicaire ne vous permet pas de passport"    
            else:
                return "false informations"    
        
         
    except Exception as e:
        print(e)     
     
# @app.route('/demandes')
# def emp():
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT NIN, nom, prenom email, tel FROM demandes")
#         empRows = cursor.fetchall()
#         respone = jsonify(empRows)
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conn.close()  

# @app.route('/message/<string:id_judicaire>')
# def emp_details(id_judicaire):
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT j FROM judicaire WHERE id_judicaire =%s", id_judicaire)
#         empRow = cursor.fetchone()
#         respone = jsonify(empRow)
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conn.close() 

# @app.route('/update', methods=['PUT'])
# def update_emp():
#     try:
#         _json = request.json
#         _NIN = _json['NIN']
#         _nom = _json['nom']
#         _prenom = _json['prenom']
#         _email = _json['email']
#         _tel = _json['tel']
#         if _NIN and _nom and _prenom and _email and _tel and request.method == 'PUT':			
#             sqlQuery = "UPDATE emp SET nom=%s,prenom=%s, email=%s, tel=%s WHERE NIN=%s"
#             bindData = (_nom, _prenom,  _email, _tel, _NIN)
#             conn = mysql.connect()
#             cursor = conn.cursor()
#             cursor.execute(sqlQuery, bindData)
#             conn.commit()
#             respone = jsonify('Employee updated successfully!')
#             respone.status_code = 200
#             return respone
#         else:
#             return showMessage()
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conn.close() 

# @app.route('/delete/<string:NIN>', methods=['DELETE'])
# def delete_emp(NIN):
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor()
# 		cursor.execute("DELETE FROM demandes WHERE NIN =%s", (NIN))
# 		conn.commit()
# 		respone = jsonify('Employee deleted successfully!')
# 		respone.status_code = 200
# 		return respone
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
        
       
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
    app.run(port=5006,debug=True)