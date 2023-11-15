import math


class GrammarStats:
    def __init__(self):
        self.number_of_checks = 0
        self.good_checks = 0

    def check(self, text):
        self.number_of_checks += 1
        text = str(text)
        if len(text) < 2:
            return False
        if text[0].isupper() and text[-1] in "!?.":
            self.good_checks += 1
            return True
        return False

    def percentage_good(self):
        if self.number_of_checks == 0:
            raise Exception("No checks completed")
        return math.floor((self.good_checks / self.number_of_checks) * 100)
