import random

playerskill = {1: '공격', 2: '가드', 3: '패링'}
PLH = ("| 성공 |", "| 실패 |", "| 실패 |")
bossskill = {1: 'HP회복', 2: '하모슬래시', 3: '조개방패', 4: '회피'}
BH = ("성공", "실패", "실패", "실패")

boss_skill = []

playerHP = 100
bossHP = 200

print()
print("옛날 옛적, 평화로운 마을 JINJOO는 무시무시한 마왕HAMO에 의해 어둠으로 뒤덮였습니다.")
print()
print("마을 사람들은 저주받은 마왕 HAMO의 앞에 비명 소리조차 내지 못하고 무력했습니다.")
print()
print("그러던 어느 날, 무모한 용사 갓다운이 나타났습니다.")
print()
print("그는 사람들의 마음을 이끌어 모아 마왕을 물리치겠다고 맹세했습니다. ")
print()
print("JINJOO마을을 떠나, 갓다운은 마왕의 성으로 향했습니다.")
print()
print("갓다운은 마왕성의 성문 앞에서 크게 호흡을 하고 마왕성으로 들어갔습니다.")
print()
print("용사 갓다운 : 마왕 HAMO!! 나 용사 갓다운이 널 물리치러 왔다!!!!!!!!!!!!")
print("마왕 HAMO : 니가 용사라고?? 홓홓홓홓홓 가소롭구나 어리석은 인간이여....")
print("용사 갓다운 : 에잇 헛소리는 집어치우고 내 칼을 받아라!!!")
print("마왕 HAMO : 그래 여기까지 온 용기는 칭찬해주마, 자! 덤벼라 용사!!!! ")
print()
print()
print("게임 설명")
print("1, 2, 3을 눌러 용사의 행동을 정해주세요.")
print("용사                     마왕")
print("체력 : 100               체력 : 200") 
print("공격력 : 20              공격력 : 30") 
print("방어력 : 10              방어력 : 5") 
print("패링 : 33%               회피 : 25%")
print()
print("마왕의 체력을 0으로 만들면 용사는 마왕을 물리칠 수 있습니다.")
print("용사의 체력이 0이 되면 용사는 쓰러지게 됩니다.")
print()
print("그럼, 행운을 빌겠습니다. 부디 마왕을 물리칠 수 있기를......")
print()
print("Game Start!!!")
print()
print()

while playerHP > 0 and bossHP > 0:
    select = int(input("당신의 턴입니다. 행동을 선택해 주세요.(1:공격, 2:가드, 3:패링)"))

    if select == 1:
        value = playerskill[1]
        boss_skill = random.choice(list(bossskill.values()))
        if value == "공격":
            if boss_skill == "HP회복":
                bossHP -= 10
                print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                print()
                print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                print()
            elif boss_skill == "하모슬래시":
                playerHP -= 30
                bossHP -= 20
                print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                print()
                print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                print()
            elif boss_skill == "조개방패":
                bossHP -= 10
                print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                print()
                print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                print()
            elif boss_skill == "회피":
                resultB = random.choice(BH)
                if resultB == "성공":
                    print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                    print("마왕 HAMO가 | 회피 | 을/를 사용했습니다.")
                    print()
                    print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                    print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                    print()  
                elif resultB == "실패":
                    bossHP -= 20
                    print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                    print("마왕 HAMO가 | 회피 | 을/를 실패하여 넘어졌습니다.")
                    print()
                    print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                    print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                    print()  

    if select == 2:
        value = playerskill[2]
        boss_skill = random.choice(list(bossskill.values()))
        if value == "가드":
            if boss_skill == "HP회복":
                bossHP += 10
                print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                print()
                print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                print()
            elif boss_skill == "하모슬래시":
                playerHP -= 20
                print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                print()
                print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                print()
            elif boss_skill == "조개방패":
                print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                print()
                print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                print()
            elif boss_skill == "회피":
                resultB = random.choice(BH)
                if resultB == "성공":
                    print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                    print("마왕 HAMO가 | 회피 | 을/를 사용했습니다.")
                    print()
                    print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                    print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                    print()  
                elif resultB == "실패":
                    print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                    print("마왕 HAMO가 | 회피 | 을/를 실패하여 넘어졌습니다.")
                    print()
                    print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                    print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                    print()  

    if select == 3:
        value = playerskill[3]
        boss_skill = random.choice(list(bossskill.values()))
        if value == "패링":
            if boss_skill == "HP회복":
                bossHP += 10
                print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                print()
                print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                print()
            elif boss_skill == "하모슬래시":
                resultP = random.choice(PLH)
                if resultP == "| 성공 |":
                    print("용사 갓다운이 | 패링 | 을/를 사용했습니다.")
                    print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                    print()
                    print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                    print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                    print()  
                elif resultP == "| 실패 |":
                    playerHP-=30
                    print("용사 갓다운이 | 패링 | 을/를 실패하였습니다.")
                    print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                    print()
                    print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                    print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                    print()  
            elif boss_skill == "조개방패":
                print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                print("마왕 HAMO가 | {} | 을/를 사용했습니다.".format(boss_skill))
                print()
                print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                print()
            elif boss_skill == "회피":
                resultB = random.choice(BH)
                if resultB == "성공":
                    print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                    print("마왕 HAMO가 | 회피 | 을/를 사용했습니다.")
                    print()
                    print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                    print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                    print()  
                elif resultB == "실패":
                    print("용사 갓다운이 | {} | 을/를 사용했습니다." .format(playerskill[select]))
                    print("마왕 HAMO가 | 회피 | 을/를 실패하여 넘어졌습니다.")
                    print()
                    print("플레이어의 체력이 | {} | 입니다.".format(playerHP))
                    print("마왕 HAMO의 체력이 | {} | 입니다.".format(bossHP))
                    print()  
                    

if playerHP <= 0:
    print("You Die")
    print()
else:
    print("You Win")
    print()
