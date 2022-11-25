
import timeit

class RunningValues(object):
    def __init__(self, initial=None):
        self.mean = 0
        self.oldmean = 0
        self.sum = 0
        self.oldsum = 0
        self.variance = 0
        self.oldvariance = 0
        self.n = 0

    def calculateNewMean(self, x):
        # self.oldmean = self.mean
        self.n += 1
        self.sum += x
        if(self.n == 1):
            self.mean = x
            return self.mean
        # self.mean += (self.n * x - self.sum) / (self.n * (self.n - 1))
        self.mean = self.sum / self.n
        return self.mean
    def getMean(self):
        return self.mean

import math

class RunningStats:

    def __init__(self):
        self.n = 0
        self.old_m = 0
        self.new_m = 0
        self.old_s = 0
        self.new_s = 0

    def clear(self):
        self.n = 0

    def push(self, x):
        self.n += 1

        if self.n == 1:
            self.old_m = self.new_m = x
            self.old_s = 0
        else:
            self.new_m = self.old_m + (x - self.old_m) / self.n
            self.new_s = self.old_s + (x - self.old_m) * (x - self.new_m)

            self.old_m = self.new_m
            self.old_s = self.new_s

    def mean(self):
        return self.new_m if self.n else 0.0

    def variance(self):
        return self.new_s / (self.n - 1) if self.n > 1 else 0.0

    def standard_deviation(self):
        return math.sqrt(self.variance())

import numpy as np
import matplotlib.pyplot as plt

test = np.random.randint(-100000, 100000, 1000)

real_variance = np.zeros(len(test))
predicted_variance = np.zeros(len(test))
real_diff = np.zeros(len(test))
predicted_diff = np.zeros(len(test))
sum = 0
n = 0
for index, i in enumerate(test):
    oldsum = sum
    sum += i
    n += 1
    mean = sum/(index+1)

    if index > 1:

        predicted_variance[index] = predicted_variance[index - 1] + ((i - (sum / n)) * (i - (sum / n)) )
        predicted_diff[index] = predicted_variance[index]/(n-1) - predicted_variance[index-1]/(n-2)
        real_variance[index] = np.var(test[0:index+1])
        real_diff[index] = real_variance[index] - real_variance[index-1]

    else:

        real_diff[index] = 0
        predicted_diff[index] = 0
        predicted_variance[index] = 0

plt.plot(range(len(test)), real_diff, label="real")
plt.plot(range(len(test)), predicted_diff, label="predicted")
plt.legend()
plt.show()
print(predicted_variance[-1]/(n-1))
print(real_variance[-1])
# print(real_diff[-1])
# print(predicted_diff[-1])
# print(mean)
# print(np.mean(test))
# print(real_diff[-1]/real_variance[-1])
# print(predicted_diff[-1]/predicted_variance[-1])
x = test[-1]
x_bar = np.mean(test[0::-1])

# print((x - np.mean(test[0:len(test)]))**2/(len(test)-1))
# real_variance = np.zeros(len(test))
# predicted_variance = np.zeros(len(test))
# sum = 0
# n = 0
# for index, i in enumerate(test):
#     sum += i
#     n += 1
#     real_variance[index] = np.var(test[0:index])
#     if index > 1:
#         predicted_variance[index] = predicted_variance[index-1] + ((i - (sum / n)) ** 2) / (n - 1)
#
#     else:
#         predicted_variance[index] = 0
#
# plt.plot(range(len(test)), real_variance, label="real")
# plt.plot(range(len(test)), predicted_variance, label="predicted")
# plt.legend()
# plt.show()
# print(real_variance[2])
# print(predicted_variance[2])
# test = range(1, 1000000)
#Worst solution
# nparr = np.zeros(100000)
# starttime = timeit.default_timer()
#
# for idx, i in enumerate(test):
#     nparr[idx] = i
#     np.mean(nparr)
# print(timeit.default_timer() - starttime)

##Best Solution for smaller numbers. UNSTABLE!
# run = RunningValues()
# starttime = timeit.default_timer()
# for i in test:
#     run.calculateNewMean(i)
# print(run.getMean())
# print(timeit.default_timer() - starttime)
#
# run1 = RunningStats()
# starttime = timeit.default_timer()
# for i in test:
#     run1.push(i)
# print(timeit.default_timer() - starttime)
# print(run1.mean())