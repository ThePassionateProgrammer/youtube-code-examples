class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def process(self, ctx):
        for step in self.steps:
            step.process(ctx)