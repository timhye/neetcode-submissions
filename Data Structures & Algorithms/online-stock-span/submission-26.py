class StockSpanner:

    def __init__(self):
        self.store = []
        

    def next(self, price: int) -> int:
        cnt = 1
        while self.store:
            if self.store[-1][0] <= price:
                amt, span = self.store.pop()
                cnt += span
        
        self.store.append((price, cnt))

        return cnt
        

                
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)