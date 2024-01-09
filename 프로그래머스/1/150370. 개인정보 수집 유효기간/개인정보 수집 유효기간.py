def calc(date) :
    year, month, day = map(int, date.split('.'))
    sum = year * 336 + month * 28 + day
    return sum

def solution(today, terms, privacies):
    answer = []
    todayDate = calc(today)
    
    termList = []
    termsDic = {}
    for i in terms :
        term, period = i.split()
        termList.append(term)
        termsDic[term] = int(period) * 28
    # {'A': 168, 'B': 336, 'C': 84}
    
    privacyDateList = []
    for i in privacies :
        period, term = i.split()
        sum = calc(period)
        privacyDateList.append(sum + termsDic[term])
    
    for i in range(len(privacyDateList)) :
        if (todayDate >= privacyDateList[i]) :
            answer.append(i+1)
    
    return answer