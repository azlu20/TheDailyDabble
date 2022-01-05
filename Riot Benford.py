import requests
import matplotlib.pyplot as plt
import numpy as np

key = "RGAPI-48a9c0e0-a3bf-4f6b-b242-ac3602906fd8"
wins = []
for i in range(1, 10):
    page = str(i)
    response = requests.get(
        f"https://br1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/SILVER/I?page={page}&api_key=RGAPI-48a9c0e0-a3bf-4f6b-b242-ac3602906fd8")
    for ele in response.json():
        cur = ele['wins']
        wins.append(cur)
print("Max is ", np.max(np.asarray(wins)))
print("Min is ", np.min(np.asarray(wins)))
print(len(wins))
first = list(map(lambda x: int(str(x)[0]), wins))
digits = [i for i in range(1, 10)]
count = [0 for i in range(1, 10)]
for ele in first:
    count[ele - 1] += 1
count = count / np.sum(count)
y = [0.301, 0.176, 0.125, 0.97, 0.079, 0.067, 0.058, 0.051, 0.046]
fit = np.polyfit(np.log(digits), count, 1)
plt.figure()
plt.plot(digits, fit[0] * np.log(digits) + fit[1], label= "Log Fit Line")
plt.bar(digits, count)
plt.xticks(digits[::1])
plt.title("First Digit of Number of Wins for Random Players in League of Legend's Silver 1 Elo", fontsize=9)
plt.ylabel("Frequency")
plt.xlabel("Digits")
plt.legend()
plt.show()
