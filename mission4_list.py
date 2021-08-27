#아이디,나이,전화번호,성별,지역,구매횟수
#{'아이디': ['abc', 'cdb', 'bbc', 'ccb', 'dab', 'aab'], '나이': ['21세', '25세', '30세', '29세', '26세', '23세'], '전화번호': ['010-1234-5678', '000-0000-0000', '010-2222-3333', '000-0000-0000', '000-0000-0000', '010-3333-1111'], '성별': ['남자', '남자', '여자', '여자', '남자', '여자'], '지역': ['서울', '서울', '서울', '경기', '인천', '경기'], '구매횟수': [5, 4, 3, 9, 8, 10]}
def good_customer(info):
    category = ['아이디','나이','전화번호','성별','지역','구매횟수']
    customer_dict = make_dict_func(info,category)
    
    vip_tf = [i>=8 for i in customer_dict['구매횟수']]      #조건1 - 8회 이상 구매한 회원이 VIP대상
    customer_dict,vip_tf = update_phone(customer_dict,vip_tf)

    vip_info = list()
    for i in category:
        tmp_li = list()
        for j in range(len(vip_tf)):
            if vip_tf[j] == True:
                tmp_li.append(customer_dict[i][j])
        vip_info.append(tmp_li)                      #멤버별X, 각 카테고리별로 대상 값 삽입 [[아이디1,아이디2],[나이1,나이2],,,]
    
    for i in range(len(vip_info[0])):  #한 카테고리안에 있는 원소의 갯수로 몇명이 vip인지 확인 
        print(f"할인 쿠폰을 받을 회원정보 {category[0]}:{vip_info[0][i]}, {category[1]}:{vip_info[1][i]}, {category[2]}:{vip_info[2][i]}, {category[3]}:{vip_info[3][i]}, {category[4]}:{vip_info[4][i]}, {category[5]}:{vip_info[5][i]}")
    

def update_phone(customer_dict,vip_tf):
    for i in range(len(customer_dict['전화번호'])):
        if '-' not in customer_dict['전화번호'][i]:
            customer_dict['전화번호'][i] = '000-0000-0000'  #조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것
            vip_tf[i] = False                               #조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
    
    return [customer_dict, vip_tf]
    
   
def make_dict_func(info,category):   #딕셔너리 (key:아이디,나이,전화번호,성별,지역,구매횟수)
    info = info.split(',')
    customer_dict = dict()
    
    for i in range(len(category)):
        tmp_list = list()
        for j in range(i,len(info),6):
            if j%6 == 5:
                info[j] = int(info[j])
            tmp_list.append(info[j])
        customer_dict[category[i]] = tmp_list

    return customer_dict


info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10,cdcd,20세,010-1234-1234,남자,서울,100"

good_customer(info)