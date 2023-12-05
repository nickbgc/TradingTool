import pandas as pd
import numpy as np

class BacktestService:
    def __init__(self, data):
        self.data = data

    def simple_moving_average_strategy(self, short_window, long_window):
        # Generate moving averages
        signals = pd.DataFrame(index=self.data.index)
        signals['signal'] = 0.0
        signals['short_mavg'] = self.data['Close'].rolling(window=short_window, min_periods=1).mean()
        signals['long_mavg'] = self.data['Close'].rolling(window=long_window, min_periods=1).mean()
        
        # Create signals
        signals['signal'][short_window:] = np.where(signals['short_mavg'][
