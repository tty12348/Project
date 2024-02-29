import random


def up_down_game():
    # 최고 시도 횟수 초기화
    best_attempts = float('inf')

    while True:
        # 컴퓨터가 생각한 숫자
        target_number = random.randint(1, 100)

        # 시도 횟수 초기화
        attempts = 0

        while True:
            # 플레이어가 숫자 입력
            try:
                guess = int(input("숫자를 입력하세요: "))

                # 입력한 숫자가 범위를 벗어날 경우 유효한 범위 내의 숫자 입력 유도
                if not (1 <= guess <= 100):
                    print("1부터 100 사이의 숫자를 입력하세요.")
                    continue

            except ValueError:
                print("올바른 숫자를 입력하세요.")
                continue

            # 시도 횟수 증가
            attempts += 1

            # 입력한 숫자와 컴퓨터의 숫자 비교
            if guess < target_number:
                print("업! 더 큰 숫자를 입력하세요.")
            elif guess > target_number:
                print("다운! 더 작은 숫자를 입력하세요.")
            else:
                print(f"축하합니다! {attempts}번째 시도에 숫자를 맞추셨습니다.")

                # 최고 시도 횟수 업데이트
                best_attempts = min(best_attempts, attempts)
                print(f"최고 시도 횟수: {best_attempts}")

                break

        # 게임 재시작 여부 확인
        play_again = input("게임을 다시 하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            print("게임 종료. 최고 시도 횟수:", best_attempts)
            break


# 게임 시작
up_down_game()