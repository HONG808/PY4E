def sales_management(member_names, member_records):
    m_avg_li = members_salesavg(member_names, member_records)

    bonus_li = m_avg_li[:2]         #조건 1 - 예비 보너스 대상자는 평균 실적 1등 2등
    interview_li = m_avg_li[-2:]    #조건 2 - 예비 면담 대상자는 평균 실적 5등 6등

    for i in bonus_li:  
        if i[1] < 5:                #조건 3 - 보너스 대상자의 평균 실적이 5보다 크지 않으면 보너스 대상자에서 제외
            bonus_li.remove(i)
    
    for j in interview_li:
        if j[1] > 3:                #조건 4 - 면담 대상자의 평균 실적이 3보다 크면 면담 대상자에서 제외
            interview_li.remove(j)

    bonus_member_li = [i[0] for i in bonus_li]
    interview_member_li = [j[0] for j in interview_li]

    for i in bonus_member_li:
        print("보너스 대상자 ",i)
    print()
    for j in interview_member_li:
        print("면담 대상자 ",j)

def sorting_sales(member_avg):  #평균실적 기준으로 정렬
    member_avg = sorted(member_avg,key=lambda li:li[1], reverse=1)
    return member_avg


def members_salesavg(member_names,member_records):  #실적평균을 기준으로 정렬한 리스트 (멤버,실적평균) 로  리턴
    m_avgs = [sum(i)/12 for i in member_records]
    member_avg = list(zip(member_names,m_avgs))
    
    return sorting_sales(member_avg)
    

# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
        
sales_management(member_names, member_records)