for _ in range(int(input())):
    N = int(input())
    G = int(input())
    prices = list(map(int, input().split()))
    prices.sort()
    print(sum(prices[:N]))