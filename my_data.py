import csv
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("Temp.csv")
data = df["temp"].tolist()

mean = statistics.mean(data)
print(mean)
sd = statistics.stdev(data)
print(sd)

final_samplemean = 0

#sample of 100 points only
def random_setofmeans():
    dataSet = []
    for i in range(0,30):
        num = random.randint(0,len(data)-1)
        value = data[num]
        dataSet.append(value)
    sample_mean = statistics.mean(dataSet)
    return(sample_mean)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["Sample Mean Temperature Graph"], show_hist = False)
    #fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        setofmeans = random_setofmeans()
        mean_list.append(setofmeans)
    show_fig(mean_list)
    final_samplemean = statistics.mean(mean_list)
    print(final_samplemean)
    sample_sd = statistics.stdev(mean_list)
    print(sample_sd)
setup()

zScore = (mean - final_samplemean) / sd
print(zScore)

#fig = ff.create_distplot([data],["temp"], show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "mean"))
#fig.show()