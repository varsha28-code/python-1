s = "ABCabc"
def good_segments(s):
    if not s:
        return 0
    count = 0
    currlen = 1
    for i in range(1, len(s)):
        if s[i].isupper() == s[i-1].isupper():
            currlen += 1
        else:
            if currlen > 1:
                count += 1
            currlen = 1
    if currlen > 1:
        count += 1
    return count
print(good_segments(s))
Input
s = "ABCabc"
-------------------------------------------------------------------------
Characters and their cases:

Index	Character	isupper()
0	     A	        True
1	     B	        True
2	     C	        True
3	     a	        False
4	     b	        False
5	     c	        False

Initially

count = 0
currlen = 1
Iteration 1 (i = 1)

Compare

B.isupper() == A.isupper()
True == True

Condition is True.

currlen = 2
count = 0
Iteration 2 (i = 2)

Compare

C.isupper() == B.isupper()
True == True

Condition is True.

currlen = 3
count = 0
Iteration 3 (i = 3)

Compare

a.isupper() == C.isupper()
False == True

Condition is False.

Previous segment length = 3 (>1)

count = 1
currlen = 1

Segment found:

ABC
Iteration 4 (i = 4)

Compare

b.isupper() == a.isupper()
False == False

Condition is True.

currlen = 2
count = 1
Iteration 5 (i = 5)

Compare

c.isupper() == b.isupper()
False == False

Condition is True.

currlen = 3
count = 1
After Loop

Current segment length = 3 (>1)

count = 2

Segment found:

abc

Return

2
Output
2
Good Segments
ABC
abc

Hence the output is:

2
Time Complexity
O(n) — one pass through the string.
Space Complexity
O(1) — only a few variables are used.
