import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

pf=pd.read_csv("medium_data.csv")
data=pf["reading_time"].tolist()
mean=statistics.mean(data)
stdev=statistics.stdev(data)

print("Population mean: {}".format(mean))
#print("Population stdev: {}".format(stdev))

def meanGen(count):
    newData=[]
    for i in range(0,count):
        num=random.randint(0,len(data)-1)
        newData.append(data[num])
    mean1=statistics.mean(newData)
    return mean1

def showFig(meanList):
    fig=ff.create_distplot([meanList],['result'],show_hist=False)
    fig.show()


def setup():
    meanList=[]
    for i in range(0,100):
        num=meanGen(30)
        meanList.append(num)

    mean2=statistics.mean(meanList)
    stdev2=statistics.stdev(meanList)

    print(" ")
    print("Sample mean: {}".format(mean2))
    #print("Sample stdev: {}".format(stdev2))

    showFig(meanList)

setup()