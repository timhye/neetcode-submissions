class FreqStack:

    def __init__(self):
        self.group = defaultdict(list)
        self.freq = defaultdict(int)
        self.mostfreq = 0
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.mostfreq = max(self.freq[val], self.mostfreq)


    def pop(self) -> int:
        x = self.group[self.mostfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.mostfreq]:
            self.mostfreq -= 1
        
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()