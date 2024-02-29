import random

def rock_paper_scissors():
    # 초기화된 통계 변수
    wins = 0
    losses = 0
    draws = 0

    while True:
        # 플레이어의 선택
        player_choice = input("가위, 바위, 보 중 하나를 선택하세요 (끝내려면 '종료' 입력): ").lower()

        # 게임 종료 여부 확인
        if player_choice == '종료':
            print("게임 종료.")
            break

        # 대소문자 구분 없이 입력 처리하기
        player_choice = player_choice.lower()

        # 컴퓨터의 선택
        computer_choice = random.choice(['가위', '바위', '보'])

        # 선택 출력
        print(f"플레이어: {player_choice}, 컴퓨터: {computer_choice}")

        # 결과 판정
        if player_choice == computer_choice:
            print("무승부!")
            draws += 1
        elif (
            (player_choice == '가위' and computer_choice == '보') or
            (player_choice == '바위' and computer_choice == '가위') or
            (player_choice == '보' and computer_choice == '바위')
        ):
            print("플레이어 승리!")
            wins += 1
        else:
            print("컴퓨터 승리!")
            losses += 1

        # 게임 통계 출력
        print(f"현재까지의 통계 - 승: {wins}, 패: {losses}, 무승부: {draws}")

        # 게임 재시작 여부 물어보기
        play_again = input("다시 하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            print("게임 종료. 최종 통계 - 승: {wins}, 패: {losses}, 무승부: {draws}")
            break

# 게임 시작
rock_paper_scissors()