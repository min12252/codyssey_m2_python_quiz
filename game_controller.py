import random

class GameController:
    def __init__(self, data_handler):
        self.dh = data_handler
        # 데이터 불러오기
        self.quizzes, self.players = self.dh.load_data()
        self.current_player = None

    # 1. 플레이어 등록 또는 선택
    def set_player(self, name):
        # 이미 존재하는 플레이어인지 확인
        for p in self.players:
            if p.name == name:
                self.current_player = p
                return f"반갑습니다, {name}님! 기존 기록을 이어서 플레이합니다."
        
        # 새로운 플레이어 생성 (models.py의 Player 클래스 사용)
        from models import Player
        new_player = Player(name)
        self.players.append(new_player)
        self.current_player = new_player
        return f"환영합니다, {name}님! 새로운 게임을 시작합니다."

    # 2. 카테고리 목록 가져오기
    def get_categories(self):
        return list(set(q.category for q in self.quizzes))

    # 3. 특정 카테고리에서 안 푼 문제 하나 뽑기
    def get_random_quiz(self, category):
        # 해당 카테고리 문제 중, 플레이어가 아직 안 푼 문제만 필터링
        available_quizzes = [
            q for q in self.quizzes 
            if q.category == category and q.id not in self.current_player.solved_ids
        ]
        
        if not available_quizzes:
            return None # 더 이상 풀 문제가 없음
        
        return random.choice(available_quizzes)

    # 4. 정답 확인 및 점수 계산
    def check_answer(self, quiz, user_answer, time_taken):
        if user_answer == quiz.answer:
            # 시간 기반 점수 계산 (10초 내 100점, 30초 내 50점, 60초 내 10점)
            if time_taken <= 10: score = 100
            elif time_taken <= 30: score = 50
            elif time_taken <= 60: score = 10
            else: score = 0
            
            # self.current_player.score += score
            self.current_player.solved_ids.append(quiz.id) # 푼 문제 목록에 추가
            return True, score
        return False, 0

    # 5. 게임 데이터 저장
    def save_game(self):
        self.dh.save_data(self.quizzes, self.players)