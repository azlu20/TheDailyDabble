import requests
import matplotlib.pyplot as plt
import numpy as np

key = "OMITTED"
wins = []
for i in range(1, 10):
    page = str(i)
    response = requests.get(
        f"https://br1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/SILVER/I?page={page}&api_key=OMITTED")
    for ele in response.json():
        cur = ele['wins']
        wins.append(cur)
print("Max is ", np.max(np.asarray(wins)))
print("Min is ", np.min(np.asarray(wins)))
print(len(wins))
ind = np.arange(9)
width = 0.3
first = list(map(lambda x: int(str(x)[0]), wins))
digits = [i for i in range(1, 10)]
count = [0 for i in range(1, 10)]
for ele in first:
    count[ele - 1] += 1
count = count / np.sum(count)
func = lambda a: np.log10(1+1/a)
y_prime = [func(i) for i in range(1,10)]
error = np.abs(np.asarray(count) - np.asarray(y_prime))
error = error/np.asarray(y_prime)
print(error * 100)
y = np.linspace(1, 9, 20)
y = np.log10(y+1) - np.log10(y)
x = np.linspace(1, 9, 20)
fit = np.polyfit(np.log(digits), count, 1)
plt.figure()
plt.bar(ind, count, width, zorder = 5, label = "Leading Digit from Dataset")
plt.bar(ind+width, y_prime, width, zorder = 5, label = "Benford's Law Values")
plt.plot(x-width/0.5, y, c = "r", label= "Benford's Law Curve", zorder = 10)
plt.xticks(ind+width/2, digits[::1])
plt.title("First Digit of Number of Wins for Random Players in League of Legend's Silver 1 Elo", fontsize=9)
plt.ylabel("Frequency")
plt.xlabel("Digits")
plt.legend()
plt.show()
