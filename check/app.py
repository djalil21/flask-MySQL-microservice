from flask import Flask,render_template
# from demandes import demandes
# from judicaire import judicaire_details
# # from surte import Surte
# from requests import re
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@app.route('/')
def home ():
      return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
