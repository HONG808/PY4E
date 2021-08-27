#수익률 = (판매가-매수가)/매수가*100
def stock_profit(stocks, sells):
    stocks_li = make_li(stocks)
    rate_li = list()

    for i in range(len(sells)):
        stock = stocks_li[i][0]
        buying = float(stocks_li[i][2])

        rate_li.append([stock, profit_cal(buying,sells[i])])
    
    rate_li = rate_sort(rate_li)
    for i in rate_li:
        print(f"{i[0]}의 수익률 {i[1]:.3}")


def rate_sort(rate_li):         #수익률 기준으로 정렬
    rate_li = sorted(rate_li,key=lambda li:li[1],reverse=1)
    return rate_li


def profit_cal(buying,price):   #수익률 계산하여 
    return (price-buying)/buying*100


def make_li(stocks):        #주식 리스트로 변환하여 리턴
    stocks_li = list()
    tmp_li = stocks.split(',')
    
    for i in tmp_li:
        stocks_li.append(i.split('/'))
    
    return stocks_li


stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

stock_profit(stocks, sells)