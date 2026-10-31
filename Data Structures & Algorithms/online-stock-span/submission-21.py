class StockSpanner:

    def __init__(self):
        self.store = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.store and self.store[-1][0] <= price:
            price, aspan = self.store.pop()
            span += aspan
        self.store.append((price, span))
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)