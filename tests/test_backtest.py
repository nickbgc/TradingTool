import unittest
from app.services.backtest import BacktestService
import pandas as pd
import numpy as np

class TestBacktestService(unittest.TestCase):

    def setUp(self):
        data = pd.DataFrame({'Close': np.random.random(100)})
        self.backtest_service = BacktestService(data)

    def test_simple_moving_average_strategy(self):
        stats = self.backtest_service.simple_moving_average_strategy(10, 30)
        self.assertIsNotNone(stats)  # Basic check to ensure stats are returned

    # Additional tests for other strategies

if __name__ == '__main__':
    unittest.main()
