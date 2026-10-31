class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        if len(self.stk) == 0:
            self.stk.append(price)
            return 1
        count = 1
        while len(self.stk) != 0:
            if self.stk.pop() <= price:
                count += 1
                continue
            else:
                return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)