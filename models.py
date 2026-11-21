class Quiz:
    def __init__(self, id, category, initials, answer):
        self.id = id
        self.category = category
        self.initials = initials
        self.answer = answer

class Player:
    def __init__(self, name, score=0, solved_ids=None):
        self.name = name
        self.score = score
        self.solved_ids = solved_ids if solved_ids is not None else []