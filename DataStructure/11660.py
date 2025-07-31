import sys
input = sys.stdin.readline

n, numberOfQuery = map(int, input().split())
OriginList = [[0]*(n+1)] #원본 배열 더미 행 만들기
prefixList = [[0]*(n+1) for _ in range(n+1)] #합 배열 전부 0으로 초기화

for i in range (n) :
    OriginList_row = [0] + [int(x) for x in input().split()]
    OriginList.append(OriginList_row) #원본 배열 한줄씩 추가

#합 배열 구하기
for i in range(1, n+1) :
    for j in range(1, n+1) :
        prefixList[i][j] = prefixList[i][j-1] + prefixList[i-1][j] - prefixList[i-1][j-1] + OriginList[i][j]

for _ in range(numberOfQuery) :
    x1, y1, x2, y2 = map(int, input().split())
    result = prefixList[x2][y2] - prefixList[x1-1][y2] - prefixList[x2][y1-1] + prefixList[x1-1][y1-1]
    print(result)