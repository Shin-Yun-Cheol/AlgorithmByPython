n = int(input())
numbers = list(map(int, input().split()))

max = max(numbers)
sum = sum(numbers)

print(100*sum/max/n)