import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split


def get_data(url):
    return pd.read_csv(url)


def plot_data(df):
    plt.plot([i for i in range(0, len(df["Open"]))], df['Open'])
    plt.show()


def get_analysis(df, type, axs):
    X = np.array([i for i in range(0, len(df[type]))]).reshape(-1, 1)
    y = np.array(df[type]).reshape(-1, 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    regr = LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)

    regression = regr.score(X_test, y_test)

    axs[0].plot(X, y, color='k')
    axs[1].set_title("Regression: " + str(regression))
    axs[1].plot(X_test, y_pred, color='k')
    axs[1].scatter(X_test, y_test, color='r')


urls = [['https://query.data.world/s/jrncrg5uimw33c6yrpeavdpnwmbos7', 'Open'], ['https://query.data.world/s/jrncrg5uimw33c6yrpeavdpnwmbos7', 'Low'], ['https://query.data.world/s/jrncrg5uimw33c6yrpeavdpnwmbos7', 'High'], ['https://query.data.world/s/jrncrg5uimw33c6yrpeavdpnwmbos7', 'Close']]
fig, axs = plt.subplots(len(urls), 2)
for i in range(len(urls)):
    df = get_data(urls[i][0])
    get_analysis(df, urls[i][1], axs[i])

plt.show()
