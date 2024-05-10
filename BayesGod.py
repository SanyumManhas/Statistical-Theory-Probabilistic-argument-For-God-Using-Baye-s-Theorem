import pandas as pd
import matplotlib.pyplot as plt

def bayes(x, y_x, y_nx):
    num = y_x * x
    denom = y_x * x + y_nx * (1 - x)
    return num / denom

posterior = [0.01] * 11
for i in range(1, 11):
    post = bayes(posterior[i - 1], 1, 1 / 7)
    posterior[i] = post

posterior_2 = [0.0001] * 11
for i in range(1, 11):
    post = bayes(posterior_2[i - 1], 1, 1 / 7)
    posterior_2[i] = post

days = list(range(0, 11))

df = pd.DataFrame({"days": days, "posterior": posterior, "posterior_2": posterior_2})

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(df["days"], df["posterior"], marker='o')
plt.xticks(days)
plt.title("Posterior estimate")
plt.xlabel("Days")
plt.ylabel("Posterior")

plt.subplot(1, 2, 2)
plt.plot(df["days"], df["posterior"], marker='o', label="0.01")
plt.plot(df["days"], df["posterior_2"], marker='o', label="0.0001")
plt.legend(title="Value of prior\non Day-1")
plt.xticks(days)
plt.title("Posterior estimate")
plt.xlabel("Days")
plt.ylabel("Posterior")

plt.tight_layout()
plt.show()
