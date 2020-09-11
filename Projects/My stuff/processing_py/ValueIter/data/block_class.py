class block:

    def __init__(self, val):
        self.val = val
        self.pval = self.val
        self.dir = (0,-1)
        self.isDigit = isinstance(self.val, (int, float))
        if not self.isDigit:
        	if self.val == "n":
        		self.pval = -1
        	if self.val == "p":
        		self.pval = 1
        	if self.val == "b":
        		self.pval = "Wall"
