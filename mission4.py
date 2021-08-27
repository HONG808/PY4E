#아이디,나이,전화번호,성별,지역,구매횟수
def good_customer(info):
    customer_dict = customer_func(info)

    #조건1 - 8회 이상 구매한 회원이 VIP대상
    #조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
    #조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것



    pass


def customer_func(info):    #딕셔너리 (key:아이디 values:그외 정보들)로 리턴
    customer_dict = dict()
    
    info = info.split(',')
    for i in range(0,len(info),6):
        customer_dict[info[i]] = info[i+1:i+6]
    
    return customer_dict


info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

good_customer(info)