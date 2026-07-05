num1 = input().strip()
num2 = input().strip()
count = 0
for digit in num1:
    if digit == num2:
        count += 1
print(count)
---------------------------
num1 = input().strip()
num2 = input().strip()
print(num1.count(num2))
----------------------------
INPUT:
1223332
2
OUTPUT:
3
