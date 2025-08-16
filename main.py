import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm

# import METAR values with date parsing
METAR = pd.read_csv('PANC_METAR_cleaned.csv', parse_dates=['valid'])
# sort dates - required for rolling average function
METAR = METAR.set_index("valid").sort_index()

# calculate 3-hour rolling averages
temperature_3hour_average = METAR['tmpf'].rolling("3H").mean()
humidity_3hour_average = METAR['relh'].rolling("3H").mean()
dewpoint_3hour_average = METAR['dwpf'].rolling("3H").mean()
windspeed_3hour_average = METAR['sknt'].rolling("3H").mean()

ceiling_model = pm.Model()

with ceiling_model:
    # priors
    baseline = pm.Normal('baseline', mu=7500, sigma=1000) # use first low-ceiling value from data set
    temperature_effect = pm.Normal('temperature_effect', mu=0, sigma=10)
    humidity_effect = pm.Normal('humidity_effect', mu=0, sigma=10)
    dewpoint_effect = pm.Normal('dewpoint_effect', mu=0, sigma=10)
    windspeed_effect = pm.Normal('windspeed_effect', mu=0, sigma=10)

    # expected value of outcome
    ceiling_prediction = baseline + temperature_3hour_average * METAR['tmpf'] + humidity_3hour_average * METAR['relh'] + dewpoint_3hour_average * METAR['dwpf'] + windspeed_3hour_average * METAR['sknt']

    # likelihood (sampling distribution) of observations
    ceiling_obs = pm.HalfNormal("ceiling_obs", sigma=500, observed=METAR['ceiling'])

    # sampling with NUTS multiprocessing error workaround
    if __name__ == '__main__':
        with ceiling_model:
            trace = pm.sample(1000,tune=1000)
            # print results of sampling
            print(pm.summary(trace))
            pm.plot_trace(trace)
            plt.show()

    