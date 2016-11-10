import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

subway_df = pd.read_csv('nyc_subway_weather.csv')
data_by_location = subway_df.groupby(['latitude', 'longitude'],
                                     as_index=False).mean()
# print data_by_location.head()
scatter_scale = (data_by_location['ENTRIESn_hourly'] /
                 data_by_location['ENTRIESn_hourly'].std())
plt.scatter(data_by_location['latitude'],
            data_by_location['longitude'],
            s=scatter_scale)
plt.show()
