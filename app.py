from flask import Flask,render_template
import socket
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


app = Flask(__name__)

def fitgen():

    df = pd.read_csv("C:/Users/Froucen/Documents/MLDS 2/DE/Projet DE/app/Dummy Data HSS.csv" )

    df = df.fillna(df.mean())
    df = pd.get_dummies(df) 
    df = df[['TV', 'Radio', 'Social Media', 'Influencer_Macro',
       'Influencer_Mega', 'Influencer_Micro', 'Influencer_Nano', 'Sales']]

    x = df.iloc[:,0:-1].values
    y = df.iloc[:,-1:].values

    x_train, x_test, y_train, y_test = train_test_split(x, y)


    lr_regressor = LinearRegression() 
    lr_regressor.fit(x_train, y_train) 
    y_pred_lr = lr_regressor.predict(x_test) 



    score = r2_score(y_test, y_pred_lr)


 
    return (score)


@app.route("/")
def index():
    
    resultat = fitgen()
    return render_template('index.html', scoreHtml = resultat,

    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
