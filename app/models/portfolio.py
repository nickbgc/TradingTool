class Portfolio:
    def __init__(self, name, initial_balance):
        self.name = name
        self.initial_balance = initial_balance
        self.positions = {}
        self.balance = initial_balance

    def add_position(self, asset, quantity, price):
        if asset not in self.positions:
            self.positions[asset] = {'quantity': 0, 'avg_price': 0}
        position = self.positions[asset]
        total_cost = position['avg_price'] * position['quantity']
        total_cost += price * quantity
        position['quantity'] += quantity
        position['avg_price'] = total_cost / position['quantity']

    def remove_position(self, asset, quantity, price):
        if asset in self.positions:
            position = self.positions[asset]
            position['quantity'] -= quantity
            if position['quantity'] <= 0:
                del self.positions[asset]

    def calculate_portfolio_value(self):
        # Placeholder for actual valuation logic
        return sum(pos['quantity'] * pos['avg_price'] for pos in self.positions.values()) + self.balance

# Example usage
# portfolio = Portfolio('MyPortfolio', 10000)
# portfolio.add_position('AAPL', 10, 150)
# print(portfolio.calculate_portfolio_value())
