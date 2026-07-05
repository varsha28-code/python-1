def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

n = int(input())
arr = list(map(int, input().split()))

prime_sum = 0

for num in arr:
    if is_prime(num):
        prime_sum += num

print(prime_sum)
