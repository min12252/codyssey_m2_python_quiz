import time
from data_handler import DataHandler
from game_controller import GameController
from models import Quiz



def main():
    # 1. 초기 설정
    dh = DataHandler()
    gc = GameController(dh)

    print("=== ✨ 초성 맞추기 퀴즈 게임 ✨ ===")
    print("게임을 시작하려면 플레이어 이름을 입력하세요. (종료하려면 'exit' 입력)")
    name = input(": ").strip()
    if name=="exit":
        print("게임을 종료합니다.")
        return
    message = gc.set_player(name)
    print(message)

    while True:
        print(f"\n[ {gc.current_player.name}님의 현재 점수: {gc.current_player.score}점 ]")
        print("1. 게임 시작")
        print("2. 데이터 확인 및 수정")
        print("3. 종료 및 저장")
        choice = input("선택: ")

        if choice == "1":
            # 카테고리 선택
            categories = gc.get_categories()
            print("\n[ 카테고리 목록 ]")
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")
            
            cat_idx = int(input("카테고리 번호를 선택하세요: ")) - 1
            selected_cat = categories[cat_idx]

            # 퀴즈 루프
            score_sum = 0
            cunt = 0
            while True:
                quiz = gc.get_random_quiz(selected_cat)
                if not quiz:
                    print(f"\n👏 '{selected_cat}' 카테고리의 모든 문제를 풀었습니다!")
                    break

                print(f"\n문제: {quiz.initials} (카테고리: {quiz.category})")
                print("(패스하려면 'pass', 그만하려면 'exit' 입력)")
                
                start_time = time.time() # 시간 측정 시작
                user_input = input("정답: ").strip()
                end_time = time.time() # 시간 측정 종료
                
                time_taken = end_time - start_time

                if user_input.lower() == 'exit':
                    break
                if user_input.lower() == 'pass':
                    print("패스! 다음 문제로 넘어갑니다.")
                    continue

                # 정답 확인
                is_correct, score = gc.check_answer(quiz, user_input, time_taken)
                score_sum += score
                cunt += 1
                gc.current_player.score = int(score_sum/cunt)

                if is_correct:
                    print(f"✅ 정답입니다! ({time_taken:.1f}초 소요 / {int(score_sum/cunt)}점)")
                else:
                    print(f"❌ 틀렸습니다! 정답은 [{quiz.answer}]였습니다.")

        elif choice == "2":

            while True:
                print("\n[ 데이터 확인 및 수정 ]")
                print("1. 퀴즈 목록")
                print("2. 퀴즈 등록")
                print("3. 플레이어 점수 확인")
                print("4. 플레이어 삭제")
                print('5. 저장 후 이전으로 돌아가기')

                sub_choice = input("선택: ")

                if sub_choice == "1":
                    print("\n[ 퀴즈 목록 ]")
                    for q in gc.quizzes:
                        print(f"{q.id}. 카테고리: {q.category}, 초성: {q.initials}, 정답: {q.answer}")

                elif sub_choice == "2":
                    print("\n[ 퀴즈 등록 ]")
                    new_id = max((q.id for q in gc.quizzes), default=0) + 1
                    new_category = input("카테고리: ").strip()
                    new_initials = input("초성: ").strip()
                    new_answer = input("정답: ").strip()
                    new_quiz = Quiz(new_id, new_category, new_initials, new_answer)
                    gc.quizzes.append(new_quiz)
                    print("\n새 퀴즈가 등록되었습니다!")

                elif sub_choice == "3":
                    print("\n[ 플레이어 점수 확인 ]")
                    for p in gc.players:
                        print(f"이름: {p.name}, 점수: {p.score}")

                elif sub_choice == "4":
                    del_name = input("\n삭제할 플레이어 이름: ").strip()
                    gc.players = [p for p in gc.players if p.name != del_name]
                    print(f"\n{del_name} 플레이어가 삭제되었습니다.")

                elif sub_choice == "5":
                    gc.save_game()
                    print("\n게임 데이터를 저장했습니다. 이전 메뉴로 돌아갑니다.")
                    break

                else:
                    print("\n잘못된 선택입니다. 다시 입력해주세요.")
                    continue

        elif choice == "3":
            gc.save_game()
            print("\n게임 데이터를 저장했습니다. 안녕히 가세요!")
            break

        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()