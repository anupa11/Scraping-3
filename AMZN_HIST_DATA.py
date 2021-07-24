import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_html('https://www.macrotrends.net/stocks/charts/AMZN/amazon/stock-price-history')
print(df[0])
df[0].to_csv('amzndata.csv')
df = pd.read_csv('amzndata.csv', header=None, skiprows=2)
x = df[1]
y = df[2]
plt.title("Amazon")
plt.xlabel('Year', fontsize=18)
plt.ylabel('Average Stock Price($)', fontsize=16)
plt.plot(x,y)
plt.show()
