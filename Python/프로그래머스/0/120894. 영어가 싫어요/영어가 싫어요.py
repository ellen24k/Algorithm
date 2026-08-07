def solution(numbers):
    answer = []
    idx = len(numbers)
    while numbers:
        if numbers.endswith('one'):
            answer.append('1')
            idx -= 3
        elif numbers.endswith('two'):
            answer.append('2')
            idx -= 3
        elif numbers.endswith('three'):
            answer.append('3')
            idx -= 5
        elif numbers.endswith('four'):
            answer.append('4')
            idx -= 4
        elif numbers.endswith('five'):
            answer.append('5')
            idx -= 4
        elif numbers.endswith('six'):
            answer.append('6')
            idx -= 3
        elif numbers.endswith('seven'):
            answer.append('7')
            idx -= 5
        elif numbers.endswith('eight'):
            answer.append('8')
            idx -= 5
        elif numbers.endswith('nine'):
            answer.append('9')
            idx -= 4
        else:
            answer.append('0')
            idx -= 4
        numbers = numbers[:idx]
    answer.reverse()
    return int(''.join(answer))