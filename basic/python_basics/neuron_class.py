class Neuron:
    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.f = f
        self.x = None

    def forward(self, x):
        self.x = x
        result = 0
        for w, x in zip(self.w, self.x):
            result += w * x
        return self.f(result)

    def backlog(self):
        return self.x
