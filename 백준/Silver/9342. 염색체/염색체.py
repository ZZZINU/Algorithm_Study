# 9342번: 염색체 (⚪실버_3)
import re # 정규 표현식 사용하기 위해서

# 패턴 설정
# `^` 해당 패턴으로 시작
# `?` 해당 패턴을 0번또는 1번
# `$` 해당 패턴으로 끝
# `+`  해당 패턴이 하나 이상
pattern = '^[A-F]?A+F+C+[A-F]?$' 

# 테스트 케이스의 개수 T만큼 반복
for i in range(int(input())):
    text = input() # 테스트 케이스 입력

    # 문자열 text에서 정규 표현식 패턴인 pattern과 
    # 일치하는 부분이 있다면 Infected!
    # 일치하는 부분이 없다면 Good
    if re.findall(pattern, text): 
        print("Infected!")
    else:
        print("Good")