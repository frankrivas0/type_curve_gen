from scipy.signal import savgol_filter

# smooth the data

def smooth_pD(pD, window_frac=0.05, polyorder=3):
    """
    Smooth the input data using Savitzky-Golay filter.

    Parameters:
    delta_P (array-like): The input data to be smoothed.
    window_frac (int): Fraction of the data length to use as the window size.
    polyorder (int): The order of the polynomial used to fit the samples.

    Returns:
    array-like: Smoothed data.
    """
    n = len(pD)
    w = int(window_frac * n)
    w += (w + 1) % 2  # make odd
    return savgol_filter(pD, w, polyorder)
