class Student:
    def __init__(self, name, dob, marks, sid=None):
        self.name = name
        self.dob = dob
        self.marks = marks
        self.total = sum(marks.values())
        self.average = self.total / len(marks)
        self.grade = self.get_grade()
        self.sid = sid

    def get_grade(self):
        if self.average >= 90:
            return 'A+'
        elif self.average >= 80:
            return 'A'
        elif self.average >= 70:
            return 'B'
        else:
            return 'C'

    def to_dict(self):
        return {
            "id": self.sid,
            "name": self.name,
            "dob": self.dob,
            "marks": self.marks,
            "total": self.total,
            "average": self.average,
            "grade": self.grade
        }
