import matplotlib.pyplot as plt
import operator 
import time
import numpy as np
import pylab
import math
from random import *

test = float("inf")


def convert(s):
    # return "https://www.twitch.tv/videos/"+str(id)+"/?t="+str(math.floor(s/3600))+"h"+str(math.floor((s%3600)/60))+"m"+str(s%60)+"s";
    return str(math.floor(s/3600))+"h"+str(math.floor((s%3600)/60))+"m"+str(s%60)+"s";

def thresholding_algo(y, lag, threshold, influence):
    signals = np.zeros(len(y))
    filteredY = np.array(y)
    avgFilter = [0]*len(y)
    stdFilter = [0]*len(y)
    avgFilter[lag - 1] = np.mean(y[0:lag])
    stdFilter[lag - 1] = np.std(y[0:lag])
    for i in range(lag, len(y)):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
            signals[i] = (y[i] - avgFilter[i-1])/stdFilter[i-1]
            filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
        else:
            signals[i] = 0
            filteredY[i] = y[i]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])

    return signals
    # return dict(signals = np.asarray(signals),
                # avgFilter = np.asarray(avgFilter),
                # stdFilter = np.asarray(stdFilter))

def running_mean(x, N):
   cumsum = np.cumsum(np.insert(x, 0, 0)) 
   return (cumsum[N:] - cumsum[:-N])


def get_timestamps(stream, num = 20):

    time_series = [0]*100000
    
    for message in stream:
        seconds = int(time.mktime(time.strptime(message.split("]")[0][1:], "%H:%M:%S")) + 2208970800)
        time_series[seconds] += 1

    # for i in range(25000):
    #     print('%d: %d' %(i, time_series[i]))

    d = 30;
    moving_avg = [0]*(100000-d)
    for i in range(d):
        moving_avg[0] += time_series[i]
    for i in range(1,25000-d):
        moving_avg[i] = moving_avg[i-1] + time_series[i+d-1] - time_series[i-1]
    for i in range(100000-d):
        moving_avg[i] /= d

    signals = thresholding_algo(time_series, 30, 4, 1)
    signal_list = []
    time_list = []

    for i in range(100000):
        if signals[i] != test and signals[i] > 0: 
            signal_list.append(i)

    for t in signal_list:
        time_list.append((t, int(signals[t])))

    time_list.sort(key=operator.itemgetter(1), reverse = True)
    time_list = time_list[:num]
    time_list.sort(key=operator.itemgetter(0))

    url_list = []
    for i,j in time_list:
        url_list.append((convert(i), convert(i + 30 + randint(0, 5) )))

    # for i in url_list:
    #     print(i)
    
    return url_list