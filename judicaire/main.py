import pymysql, json
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

# @app.route('/create', methods=['POST'])
# def create_demandes():
#     try:        
#         _json = request.json
#         _NIN = _json['NIN']
#         _nom = _json['nom']
#         _prenom = _json['prenom']
#         _email = _json['email']
#         _tel = _json['tel']
#         if _NIN and _nom and _prenom and _email and _tel and request.method == 'POST':
#             conn = mysql.connect()
#             cursor = conn.cursor(pymysql.cursors.DictCursor)		
#             sqlQuery = "INSERT INTO demandes (NIN, nom, prenom, email, tel) VALUES (%s, %s, %s, %s,%s)"
#             bindData = (_NIN, _nom, _prenom, _email, _tel)            
#             cursor.execute(sqlQuery, bindData)
#             conn.commit()
#             respone = jsonify('demande added successfully!')
#             respone.status_code = 200
#             return respone
#         else:
#             return showMessage()
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conn.close()          
     
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

@app.route('/judicaire/<int:id_judicaire>')
def emp_details(id_judicaire):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT j FROM judicaire.judicaire WHERE id_judicaire =%s", id_judicaire)
        empRow = cursor.fetchone()
        respone=jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

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
    app.run(port=5002)