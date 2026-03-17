class Student:
    def __init__(self, name, section, score_1, score_2, score_3, score_4):
        self.name = name
        self.section = section
        self.score_1 = float(score_1)
        self.score_2 = float(score_2)
        self.score_3 = float(score_3)
        self.score_4 = float(score_4)

    def get_average(self):
        return (self.score_1 + self.score_2 + self.score_3 + self.score_4) / 4


    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.score_1,
            "english": self.score_2,
            "social_studies": self.score_3,
            "science": self.score_4
        }
    

   


