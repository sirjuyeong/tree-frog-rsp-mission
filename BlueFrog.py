import random
import time

class Bluefrog:
    def __init__(self): 
        self.choices = ["가위", "바위", "보"]

    def answer(self, player_choice, enemy_choice):     # 모범 답안
        if player_choice == enemy_choice:
            return "개굴"
        elif (player_choice == "가위" and enemy_choice == "보") or \
             (player_choice == "바위" and enemy_choice == "가위") or \
             (player_choice == "보" and enemy_choice == "바위"):
            return "졌다"
        else:
            return "이겼다"

    def start(self):     # 게임 시작
        print("청개구리 가위, 바위, 보를 시작합니다.")

        while True:
            player_choice = input("가위, 바위, 보를 입력해주세요: ")
            if player_choice not in self.choices:
                print("가위, 바위, 보 중에서 선택하세요.")
                continue
            
            enemy_choice = random.choice(self.choices)

            start_time = time.time()
            attack = input(f"상대는 [{enemy_choice}]를 냈습니다 : ")
            end_time = time.time()
            
            time_taken = end_time - start_time 

            answer = self.answer(player_choice, enemy_choice)
            
            if (attack == answer) and (time_taken < 3):     # 게임 결과 판별
                print("게임에 승리하셨습니다!")
            else:
                print("게임에 패배하셨습니다...")

            insertcoin = input("게임을 새로 시작하려면 '1', 종료하려면 '2'를 입력하세요 : ")     # 게임 재시작
            if insertcoin.lower() != '1':
                print("게임을 종료합니다.")
                break

if __name__ == "__main__":
    game = Bluefrog()
    game.start()
