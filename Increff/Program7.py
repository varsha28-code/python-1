s="AbCDEfghI"
def convert(s):
    if not s:
        return 0
    count=0
    for i in range(len(s)-1):
        if s[i].isupper()!=s[i+1].isupper():
            count+=1
    return count
print(convert(s))
----------------------------------------------------------------------
Step 1: String
Index : 0 1 2 3 4 5 6 7 8
Char  : A b C D E f g h I
Case  : U L U U U L L L U
Step 2: Compare adjacent characters
i	Pair	Cases	Different?	Count
0	A, b	U, L	Yes	         1
1	b, C	L, U	Yes	         2
2	C, D	U, U	No	         2
3	D, E	U, U	No	         2
4	E, f	U, L	Yes	         3
5	f, g	L, L	No	         3
6	g, h	L, L	No	         3
7	h, I	L, U	Yes	         4
Final Output
4
What the code does

isupper() returns:

True for uppercase letters
False for lowercase letters

The condition

s[i].isupper() != s[i+1].isupper()

checks whether two consecutive characters have different cases.

Whenever the case changes from:

Upper → Lower, or
Lower → Upper,

the counter is incremented.

For "AbCDEfghI" the case changes are:

A → b   ✓
b → C   ✓
C → D   ✗
D → E   ✗
E → f   ✓
f → g   ✗
g → h   ✗
h → I   ✓

Total case transitions = 4.
