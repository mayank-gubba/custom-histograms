from flask import Flask, render_template,request
import plotly.express as px
import plotly
import plotly.graph_objs as go

from scipy.stats import truncnorm
import pandas as pd
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def index():
    
    bar = create_plot_normal(mean = 0,sd = 1,samp = 20 , rep = 'with_rep')
    
    return render_template('normal.html',plot=bar)
@app.route('/normal')
def normal():
    
    bar = create_plot_normal(mean = 0,sd = 1,samp = 20 , rep = 'with_rep')
    
    return render_template('normal.html', plot=bar)
@app.route('/uniform')
def uniform():
    
    bar = create_plot_uniform(min = 0,max = 1 ,samp = 20, rep = 'with_rep')
    
    return render_template('uniform.html', plot=bar)
@app.route('/exponential')
def exponential():
    
    bar = create_plot_exponential(lambdas = 1 , samp = 20, rep = 'with_rep')
    
    return render_template('exponential.html', plot=bar)
def get_truncated_normal(mean = 0, sd = 1, low=0, upp=100):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
def random_floats(low, high, size):
    return [np.random.uniform(low, high) for _ in range(size)]
def create_plot_normal(mean,sd,samp,rep):
    X = get_truncated_normal(mean , sd , low=1, upp=100)
    a = X.rvs(samp)
    print(mean,sd)
    
    if rep == 'with_rep':
        x = np.random.choice(a,samp, replace=True)
    else:
        x = np.random.choice(a,samp, replace=False)

    data = [
        go.Histogram(
            x=x ,
            hoverlabel = dict(bgcolor = 'blue'),
            selected_marker_color = 'black'
        )
    ]





    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
def create_plot_uniform(min,max,samp,rep):
    N = 40
    
    b = random_floats(min, max, samp)
    if rep == 'with_rep':
        x = np.random.choice(b,samp, replace=False)
    else:
        x = np.random.choice(b,samp, replace=True)
    data = [
        go.Histogram(
            x=x # assign x as the dataframe column 'x'
        )
    ]



    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
def create_plot_exponential(lambdas,samp,rep):
    N = 40
    
    c =np.random.exponential(lambdas, samp)
    if rep == 'with_rep':
        x = np.random.choice(c,samp, replace=True)
    else:
        x = np.random.choice(c,samp, replace=False)
    data = [
        go.Histogram(
            x=x # assign x as the dataframe column 'x'

        )
    ]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/bar1', methods=['GET', 'POST'])
def change_features_norm():

    rep = request.args['rep']
    mean = int(request.args['mean'])
    sd = int(request.args['sd'])
    samp = int(request.args['samp'])

    graphJSON= create_plot_normal(mean,sd,samp,rep)
    return graphJSON
@app.route('/bar2', methods=['GET', 'POST'])
def change_features_uni():

    rep = request.args['rep']
    min = int(request.args['min'])
    max = int(request.args['max'])
    samp = int(request.args['samp'])
    graphJSON= create_plot_uniform(min,max,samp,rep)
    return graphJSON
@app.route('/bar3', methods=['GET', 'POST'])
def change_features_expo():

    rep = request.args['rep']
    lambdas = int(request.args['lambda'])
    samp = int(request.args['samp'])
    graphJSON= create_plot_exponential(lambdas,samp,rep)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)