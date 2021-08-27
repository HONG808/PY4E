#고려,조선시대 왕 이름 중 중복
def king(korea_king, chosun_king):
    k_kings = set(korea_king.split(','))    #set으로 같은 시대 속 중복제외
    c_kings = set(chosun_king.split(','))

    kings = list(k_kings)+list(c_kings)
    kings_dict = dict()

    for king in kings:
        kings_dict[king] = kings_dict.get(king,0)+1 #이미 딕셔너리에 있을 시 +1, 없을 시 기본값0에서+1 하여 딕셔너리에 새로 삽입 
    
    cnt = 0
    for king in kings_dict:
        if kings_dict[king] > 1:
            cnt += 1
            print('조선과 고려에 모두 있는 왕 이름: ',king)
    print(f"조선과 고려에 모두 있는 왕 이름은 총 {cnt}개 입니다")


# 왕이름
korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

king(korea_king, chosun_king)