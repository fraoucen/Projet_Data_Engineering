from flask import Flask,render_template
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import r2_score



app = Flask(__name__)

def fitgen():

    df = pd.read_csv("C:/Users/Claas/Downloads/Dummy Data HSS.csv" )
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
    scoreRegression = r2_score(y_test, y_pred_lr)



    rf_regressor = RandomForestRegressor() 
    rf_regressor.fit(x_train, y_train) 
    y_pred_rf = rf_regressor.predict(x_test) 
    scoreRandomForest = r2_score(y_test, y_pred_rf)


    dt_regressor = DecisionTreeRegressor()
    dt_regressor.fit(x_train, y_test)
    y_pred_dt = dt_regressor.predict(x_test)
    scoreDecisionTree = r2_score(y_test, y_pred_dt)




    return [scoreRegression, scoreRandomForest, scoreDecisionTree]






@app.route("/", )
def index():
   
    list = fitgen()
    scoreRegression = list[0]
    scoreRandomForest = list[1]
    scoreDecisionTree = list[2]

    return render_template('index.html', scoreRegressionHtml = scoreRegression , 
                                         scoreRandomHtml = scoreRandomForest ,
                                         scoreDecisionTreeHtml = scoreDecisionTree)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True )