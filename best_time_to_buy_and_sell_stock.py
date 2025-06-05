#given list of numbers, find max profit by buying on any day and selling on a future day
#greedy algorithm,two pointers for each L iterate R across and calculate profit,when r is > l, we know we have evaluated all potential max profits, so move l to where R is and repeat
#O(N) time with left and right pointers single iteration
#O(1) space
def maxprofit(prices):
    l,r=0,1
    maxp=0
    while r!= len(prices):
        if prices[l]<prices[r]:
            prof=prices[r]-prices[l]
            maxp=max(maxp,prof)
        else:
            l=r
        r+=1
    print(maxp)
prices=list(map(int,input().split()))
maxprofit(prices)
