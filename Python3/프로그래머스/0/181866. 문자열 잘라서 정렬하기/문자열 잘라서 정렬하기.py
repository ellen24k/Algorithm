def solution(myString):
    return sorted(substr for substr in myString.split('x') if substr != '')