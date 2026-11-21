import json
import os
from models import Quiz, Player

class DataHandler:
    def __init__(self, file_path="state.json"):
        self.file_path = file_path

    # 파일에서 데이터를 읽어와 객체 리스트로 변환
    def load_data(self):
        if not os.path.exists(self.file_path):
            return [], []

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 1. 딕셔너리 리스트를 Quiz 객체 리스트로 변환
        quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
        
        # 2. 딕셔너리 리스트를 Player 객체 리스트로 변환
        players = [Player(**p) for p in data.get("players", [])]
        
        return quizzes, players

    # 객체 리스트를 다시 딕셔너리로 바꿔서 파일에 저장
    def save_data(self, quizzes=None, players=None):
        data = self.load_data()
        if quizzes is None:
            quizzes = data[0]
        if players is None:
            players = data[1]
        data = {
            # 객체를 딕셔너리로 변환 (__dict__ 사용)
            "quizzes": [q.__dict__ for q in quizzes],
            "players": [p.__dict__ for p in players]
        }
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)