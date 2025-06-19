def solution(n):
    n = str(n)
    
    answer = 0
    
    for char in n:
        char = int(char)
        answer += char
    
    return answer