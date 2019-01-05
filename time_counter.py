class TimeCounter:
    def __init__(self):
        self.start = True
        self.label = 30000
        self.content = "Countdown " + str(self.label//1000) + " s"

    def update(self):
        self.label -= 15
        self.content = "Countdown " + str(self.label//1000) + " s"

    def stop(self):
        self.label += 0
        self.content = "Countdown " + str(self.label//1000) + " s"