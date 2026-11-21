class Quiz:
    def __init__(self, id, category, initials, answer):
        self.id = id
        self.category = category
        self.initials = initials
        self.answer = answer

class Player:
    def __init__(self, name, score=0, used_ids=None):
        self.name = name
        self.score = score
        self.used_ids = used_ids if used_ids is not None else []