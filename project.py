import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
fig=ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()
population_stdev=statistics.stdev(data)
print(population_mean)
print(population_stdev)
def random_set_of_mean(counter):
    data_set=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)
    return mean

def setup():
    meanlist=[]
    for i in range(0,1000):
        set_of_means = random_set_of_mean(81)
        meanlist.append(set_of_means)
    mean=statistics.mean(meanlist)
    fig=ff.create_distplot([meanlist],["reading_time"],show_hist=False)
    fig.show()
    print("mean of sampling distribution",mean)
    z_score=(mean-population_mean)/population_stdev
    print("z_score",z_score)
setup()

def standard_deviation():
    meanlist=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(81)
        meanlist.append(set_of_means)
    standard_deviation=statistics.stdev(meanlist)
    print("standard_deviation of sampling distribution",standard_deviation)
standard_deviation()


        
