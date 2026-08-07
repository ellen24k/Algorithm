def solution(babbling):
    answer = 0
    
    for b in babbling:
        replaceAya = b.replace('aya', '1')
        replaceYe = replaceAya.replace('ye', '1')
        replaceWoo = replaceYe.replace('woo', '1')
        replaceMa = replaceWoo.replace('ma', '1')
        replace1 = replaceMa.replace('1', '')
        if replace1 == '': answer += 1
    return answer