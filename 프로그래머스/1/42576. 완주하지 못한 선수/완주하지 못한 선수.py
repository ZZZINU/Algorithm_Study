from collections import Counter

def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    for person in participant_counter:
        if participant_counter[person] != completion_counter[person]:
            return person
