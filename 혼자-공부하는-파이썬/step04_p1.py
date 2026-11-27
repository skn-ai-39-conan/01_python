# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 이름, 나이, 보호자 동의를 차례로 읽습니다.
name = input().strip()
age = int(input())
consent = int(input())
# 2) 입력값에 맞는 안내 결과를 정해 보세요.
# TODO: 조건에 따라 결과를 정하세요.
def chk_age(name , age, consent) -> str:

    if name.strip() == "":
        result = "이름을 입력하세요"

    if 18 <= age:
        result = "성인 입장"
    elif age >= 13 and age < 18 and consent == 1:
        result = "청소년 입장"
    else:
        result = "입장 불가"

    return result

# 3) 정한 안내 결과를 출력합니다.
print(chk_age(name, age, consent))
