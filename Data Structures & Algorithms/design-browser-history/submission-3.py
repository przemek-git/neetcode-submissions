class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currentPage = 0
        self.historyLength = 1

    def visit(self, url: str) -> None:
        self.currentPage += 1
        if self.currentPage < self.historyLength:
            self.history[self.currentPage] = url
        else:
            self.history.append(url)
        self.historyLength = self.currentPage + 1

    def back(self, steps: int) -> str:
        if steps >= self.currentPage + 1:
            self.currentPage = 0
        else:
            self.currentPage -= steps
        return self.history[self.currentPage]
        

    def forward(self, steps: int) -> str:
        if self.currentPage + steps >= self.historyLength - 1:
            self.currentPage = self.historyLength - 1
        else:
            self.currentPage += steps
        return self.history[self.currentPage]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)