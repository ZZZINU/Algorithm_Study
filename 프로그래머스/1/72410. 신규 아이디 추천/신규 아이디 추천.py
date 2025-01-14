def solution(new_id):
    answer = ''
    # 1단계: 소문자로 바꾸기
    answer = new_id.lower()
    # print("1단계:", answer)
    
    
    # 2단계: 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    temp_answer = ''
    for char in answer:
        if char.isalnum() or char in ['-', '_', '.']:
            temp_answer += char
    answer = temp_answer
    # print("2단계:", answer)
    
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    temp_answer = ''
    check = False
    for char in answer:
        if char == '.':
            check = True
        else:
            if check:
                temp_answer += '.'
                check = False
            temp_answer += char
    if check:
        temp_answer += '.'
    answer = temp_answer
    # print("3단계:", answer)   
    
    
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = answer.strip('.')
    # print("4단계:", answer) 
    
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if answer == '':
        answer = 'a'
    
    # print("5단계:", answer) 
    
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    answer = answer[:15]
    answer = answer.rstrip('.')
    # print("6단계:", ) 
    
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 끝에 붙이기
    text = answer[-1]
    while len(answer) <= 2:
        answer+=text
    

    
        
    
    
    return answer