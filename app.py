from flask import Flask,render_template
import socket
import pandas as pd







app = Flask(__name__)

def fitgen():

    df = pd.read_csv("C:/Users/Froucen/Documents/MLDS 2/DE/Projet DE/app/Dummy Data HSS.csv" )

    df = df.fillna(df.mean())
    df = pd.get_dummies(df) 
    df = df[['TV', 'Radio', 'Social Media', 'Influencer_Macro',
       'Influencer_Mega', 'Influencer_Micro', 'Influencer_Nano', 'Sales']]


 
    return (df)



@app.route("/")
def index():
    

    return render_template('index.html', 

    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
