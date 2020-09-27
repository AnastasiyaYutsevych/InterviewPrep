def maxProfit (prices):
    i = 0
    valley = prices[0]
    peak = prices[0]
    maxprofit= 0
    while i < len(prices)-1 :
        print('I is ', i)
        print(prices[i] >= prices[i+1])
        while(i<len(prices)-1 and prices[i] >= prices[i+1]):
            i+=1
            print('I increased to', i)
        valley = prices[i]
        while(i<len(prices)-1 and prices[i] <= prices[i+1]):
             i+=1
             print('II increased to',i)
        peak = prices[i]
        print(valley,peak)
        maxprofit+= peak - valley
    return maxprofit
print(maxProfit([7,1,5,3,6,4]))