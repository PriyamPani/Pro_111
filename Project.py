import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

# code to show the plot of raw data
# fig = ff.create_distplot([data], ["temp"], show_hist=False)
# fig.show()



#code to find mean and std deviation of 100 data points
# dataset = []
# for i in range(0, 100):
#     random_index= random.randint(0,len(data))
#     value = data[random_index]
#     dataset.append(value)
# mean = statistics.mean(dataset)
# std_deviation = statistics.stdev(dataset)
#
# print("Mean of sample:- ",mean)
# print("std_deviation of sample:- ",std_deviation)



##  code to find the mean of 100 data points 1000 times and plot it
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )




#Code to find the mean of the raw data ("population data")
mean = statistics.mean(data)
print("population mean:- ", mean)


# code to find the standard deviation of the sample data

mean_list = []

for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)
df = mean_list

std_deviation = statistics.stdev(mean_list)
print("Standard deviation of sampling distribution:- ", std_deviation)


first_start, first_end = mean - std_deviation, mean + std_deviation
second_start, second_end = mean-(2*std_deviation), mean + (2*std_deviation)
third_start, second_end =  mean-(3*std_deviation), mean + (3*std_deviation)

print("1",first_start,first_end)

fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_start,first_start], y=[0,1], mode="lines", name="STD1 Start"))
fig.add_trace(go.Scatter(x=[first_end,first_end], y=[0,1], mode="lines", name="STD1 End"))
fig.add_trace(go.Scatter(x=[second_start,second_start], y=[0,1], mode="lines", name="STD2 Start"))
fig.add_trace(go.Scatter(x=[second_end,second_end], y=[0,1], mode="lines", name="STD2 End"))



#Data 1 
df1 = pd.read_csv("medium_data.csv")
data1 = df1["reading_time"].tolist()
mean_data1 = statistics.mean(data1)
fig.add_trace(go.Scatter(x=[mean_data1,mean_data1], y=[0,1], mode="lines", name="Data1"))
fig.show()