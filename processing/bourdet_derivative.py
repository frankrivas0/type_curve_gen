import numpy as np


def bourdet_derivative(t, p):
        t, p = np.asarray(t), np.asarray(p)
        logt = np.log(t)
        dt = np.diff(logt)
        dp = np.diff(p)

        d = np.zeros_like(p)
        d[1:-1] = ((dt[:-1]/dt[1:])*dp[1:] + (dt[1:]/dt[:-1])*dp[:-1]) / (dt[:-1] + dt[1:])
        d[0]  = dp[0]  / dt[0]
        d[-1] = dp[-1] / dt[-1]
        return d