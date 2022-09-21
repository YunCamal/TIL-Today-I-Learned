import collections 

def solution(id_list, report, k):
    answer = []                 # return 값
    report = list(set(report))  # 중복제거
    reportHash = collections.defaultdict(set) # 키에 대응되는 value는 set
    stoped = collections.defaultdict(int)     # 카운트

    # 공백으로 연결된 문자열을 분리한후 카운팅
    for x in report:
        a, b = x.split(' ')
        reportHash[a].add(b)
        stoped[b]+=1
    
    # id_list 별로     
    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stoped[user]>=k:
                mail+=1
        answer.append(mail)

    return answer

if __name__ == "__main__":
    solution()
    

# 해쉬 자료구조로 사용하면 된다. 문자말고 숫자로 가능하다
# 해쉬는 key와 value로 이루어져 있다.
# reportHash = collections. defaultdict(set) << set이 뜻하는건 {}, list를 넣으면 []로 받는다.
# stoped = collections.defaultdict(int) << 0으로 초기화 된다.

# 1.
# reportHash['muzi'].add('frodo') 
#                   -> reportHash = {'muzi':{'frodo'}}
# stoped['frodo']+=1 
#               -> stoped={'frodo':1}

# 2.
# reportHash['apeach'].add('frodo') 
#                   -> reportHash = {'muzi':{'frodo'},{'apeach':{'neo'}}
# stoped['frodo']+=1 
#               -> stoped={'frodo':2}

# 3.
# reportHash['frodo'].add('neo') 
#                   -> reportHash = {'muzi':{'frodo'},{'apeach':{'neo'},'frodo':{'neo'}}
# stoped['neo']+=1 
#               -> stoped={'frodo':2,'neo':1}

# 4. 
# reportHash['muzi'].add('neo') 
#                   -> reportHash = {'muzi':{'frodo'},{'apeach':{'neo'},'frodo':{'neo'}}
# stoped['neo']+=1 
#               -> stoped={'frodo':2,'neo':2}

# 5.
# reportHash['apeach'].add('muzi') 
#                   -> reportHash = {'muzi':{'frodo'},{'apeach':{'neo'},'frodo':{'neo'}}
# stoped['neo']+=1 
#               -> stoped={'frodo':2,'neo':2,'muzi':1}



# for name in id_list:
#   mail=0
#   for user in reportHash[name]:
#      if stoped[user] >= k:
#      mail+=1
# import collections 를 꼭 써야한다.
# report = list(set(report)) 로 변경한다. (중복제거)
# reportHash = collections.defaultdict(set)
# stoped = collections.defaultdict(int)
# for x in report:
#   a, b = x.split(' ')
#   reportHash[a].add(b)
#   stoped[b]+=1
# for name in id_list:
#   mail = 0
#   for user in reportHash[name]
#       if stoped[user] >=k:
#           mail+=1
#   answer.append(mail
# print(reportHash)
# return answer
