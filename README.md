# 🏆 초성 맞추기 퀴즈 게임

## 1. 프로젝트 개요
다양한 카테고리의 초성을 보고 정답을 입력하여 맞히는 터미널 기반의 퀴즈 게임입니다.
플레이어별 이력 관리와 시간 제한 점수 시스템을 제공합니다.

## 2. 프로젝트 주제 선정 이유
- 터미널 기반 퀴즈게임에 적합한 초성맞추기 게임을 선택하였습니다. 텍스트만으로 터미널에서 실행이 가능하며 쉽게 문제를 생성할 수 있는 주제로 선택하였습니다.

## 3. 실행방법
- 실행 환경
    Python 3.9.6
    macOS 26.2
- 실행 방법
```bash
    git clone https://github.com/min12252/codyssey_m2_python_quiz.git
    cd codyssey_m2_python_quiz
    python3 main.py
```

## 4. 기능목록
* 퀴즈 플레이
    * 카테고리 선택: 원하는 주제 선택
    * 초성 퀴즈 풀기: 초성을 보고 정답 입력 (이미 푼 문제 제외)
    * Pass 기능: 모르는 문제는 넘어가고 다음 문제 진행
    * 시간 점수 시스템:
        * 10초 이내 정답: 100
        * 30초 이내 정답: 50
        * 30초 초과 정답: 10
* 문제 관리
    * 문제 등록: 카테고리, 문제(초성), 정답 등록
    * 문제 관리: 등록된 문제 리스트 확인 및 삭제
* 점수 및 플레이어 관리
    * 플레이어 등록: 닉네임으로 사용자 등록
    * 점수 확인: 플레이어별 최고 점수 확인
    * 플레이어 삭제:

## 5. 파일구조
```bash
quiz_project/
├── main.py            # 프로그램 실행 진입점 (Entry Point)
├── models.py          # Quiz, QuizGame 클래스 정의
├── game_controller.py # 퀴즈 실행, 시간 측정, 점수 계산 로직
├── data_handler.py    # state.json 파일 읽기/쓰기 및 데이터 필터링
├── state.json         # 데이터 저장 파일 (실행 시 생성)
├── .gitignore         # 불필요한 파일 제외 (__pycache__ 등)
├── README.md          # 프로젝트 문서
└── log                # 실습 로그 txt,img 파일
```

## 6. 클래스 역할
- data_handler.py: json 데이터를 읽고 다시 저장
    - load_data
    - save_data
- game_controller: 게임 실행시 필요한 기능
    - set_player: 플레이어 선택/등록
    - get_categories: 카테고리 목록 가져오기
    - start_turn: 턴 시작시 used_ids 초기화
    - get_random_quiz: 안푼 문제 랜덤으로 가져오기
    - check_answer: 정답확인, 점수계산
    - record_quiz: used_ids에 문제 기록
    - save_game: 게임 데이터 저장
- models: 퀴즈, 플레이어 객체 생성
    - quiz
    - player


## Git 브랜치 실습

- feature/readme 브랜치를 생성하여 README 수정 작업 진행
- 작업 내용을 커밋한 후 main 브랜치에 병합
<br>

[커밋 로그](log/git_log.txt)

[git log --oneline --graph](log/git_log스크린샷.png)

## Clone/Pull 실습
- clone_test 폴더에 clone
- README.md 수정 후 commit
- 원래 폴더에서 다시 pull
<br>

[clone/pull 실습 로그](log/clone_test.txt)

