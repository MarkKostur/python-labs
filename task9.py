import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Читаємо дані про втрати русні з csv
df = pd.read_csv('./data/russia_losses_personnel.csv', sep=',')
df = df.fillna(0)

df_copy = df.copy()

first_value_to_save = df['personnel'][0]
df_copy['personnel'] = df_copy['personnel'].diff().fillna(first_value_to_save)

max_losses = df_copy['personnel'].max()
min_losses = df_copy['personnel'].min()
avg_losses = df_copy['personnel'].mean()
print('avg_losses', avg_losses)
print('min_losses', min_losses)

def get_index(value):
    for i in range(len(df_copy['personnel'])):
        if df_copy['personnel'][i] == value:
            return i

index_max_value = get_index(max_losses)
index_min_value = get_index(min_losses)
index_avg_value = get_index(int(avg_losses))
print('min_losses_index', index_min_value)
print('index avg',)

train_size = int(len(df_copy))
train = df_copy['personnel'][:train_size]

model = ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=100)
model_fit = model.fit()

steps_to_predict = 500
forecast = model_fit.forecast(steps=steps_to_predict)
print('model_fit', forecast)

forecast_index = pd.Index(train.index[-1] + i for i in range(1, steps_to_predict+2))
print(forecast_index)

forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=['personnel'])


plt.plot(train.index, train, label='Train')
plt.plot(forecast_df.index, forecast_df['personnel'], label='Forecast', linestyle='--', color='red')

plt.xlabel('Дні')
plt.ylabel('Втрати русні')
plt.title('Прогноз втрат русні за часом')

plt.bar(df_copy.index, df_copy['personnel'], alpha=0.5, label='Втрати русні')

plt.scatter(index_max_value, max_losses, marker='o', color='green', label='Максимальні втрати')
plt.scatter(index_min_value, min_losses, marker='o', color='red', label='Мінімальні втрати')
plt.scatter(index_avg_value, avg_losses, marker='o', color='yellow', label='Середні втрати')

plt.legend()
plt.show()
