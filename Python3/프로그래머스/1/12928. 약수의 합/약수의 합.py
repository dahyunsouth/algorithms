def solution(n):
    lst = []
    
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    
    answer = sum(lst)
    
    return answer