import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

import config

pandas2ri.activate()

utils = importr('utils')
utils.chooseCRANmirror(ind=1)

try:
    forecast = importr('forecast')
    ts = robjects.r('ts')
    auto_order = robjects.r('arimaorder')
except Exception as e:
    utils.install_packages("forecast")


def auto_calibration_arima(df, col, freq=12):
    try:
        r_df = ts(df[col].values, frequency=freq)
        fit = forecast.auto_arima(r_df)
        return [x for x in auto_order(fit)]
    except Exception as e:
        print(e)


return None