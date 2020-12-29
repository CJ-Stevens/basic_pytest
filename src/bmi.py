class Bmi:
    def __init__(self, w_kg, h_cm):
        self.w_kg = w_kg
        self.h_cm = h_cm
        # what if we have self.bmi in __init__ (its value can be changed outside class!!!)
        # self.bmi = self.w_kg / (self.h_cm / 100) ** 2

    @property  # readonly
    def bmi(self):
        return self.w_kg / (self.h_cm / 100) ** 2

    def bmi2(self):
        return self.w_kg / (self.h_cm / 100) ** 2

    def category(self):
        cat = ""
        if self.bmi < 18.5:
            cat = "ต่ำกว่าเกณฑ์"
        elif 18.5 <= self.bmi <= 25:
            cat = "ตามเกณฑ์"
        elif 25 < self.bmi <= 30:
            cat = "เกินเกณฑ์"
        elif self.bmi > 30:
            cat = "อ้วน"
        return cat

    def __str__(self):
        return "BMI = {:.2f} ({})".format(self.bmi2(), self.category())
