import pandas as pd
import numpy as np
import vectorbt as vbt

class BacktestService:
    def __init__(self, data):
        self.data = data

    def simple_moving_average_strategy(self, short_window, long_window):
        # Calculate moving averages
        short_sma = vbt.MA.run(self.data['Close'], window=short_window)
        long_sma = vbt.MA.run(self.data['Close'], window=long_window)

        # Generate signals
        entries = short_sma.ma_above(long_sma)
        exits = short_sma.ma_below(long_sma)

        # Perform backtest
        portfolio = vbt.Portfolio.from_signals(self.data['Close'], entries, exits, fees=0.001)
        return portfolio.stats()

# Example usage
# data = pd.DataFrame({'Close': np.random.random(100)})
# backtest_service = BacktestService(data)
# print(backtest_service.simple_moving_average_strategy(10, 30))
