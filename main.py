import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm

# import METAR values
METAR = pd.read_csv('PANC_METAR_cleaned.csv')

ceiling_model = pm.Model()

with ceiling_model:
    # priors
    baseline = pm.Normal('baseline', mu=7500, sigma=1000) # use first low-ceiling value from data set
    temperature_effect = pm.Normal('temperature_effect', mu=0, sigma=10)

    # expected value of outcome
    ceiling_prediction = baseline + temperature_effect * METAR['tmpf']

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

    