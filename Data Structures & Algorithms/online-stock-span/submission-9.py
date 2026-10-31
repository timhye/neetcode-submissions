class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        print(stk)
        if len(self.stk) == 0:
            self.stk.append(price)
            return 1
        count = 1
        for i in range(len(self.stk)-1,-1,-1):
            if self.stk[i] <= price:
                count += 1

        self.stk.append(price)

        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)