It finds the longest word that:
*starts with a vowel (a, e, i, o, u)
*has an even length

Dry Run
s = "The sun sets in the west"
Step 1: Split into words
words = ['The', 'sun', 'sets', 'in', 'the', 'west']
Initial Values
vowels = {'a','e','i','o','u'}
res = "00"
ml = 0
Iterate through each word
Word	Length	Even?	Starts with vowel?	Action
The	     3	    ❌	     No	                Skip
sun    	 3	    ❌	     No	                Skip
sets	 4	    ✅	     No (s)	            Skip
in	     2	    ✅	     Yes (i)	      ml=2, res="in"
the	     3	    ❌	     No	                Skip
west	 4	    ✅	     No (w)	            Skip
Final Output
in
Output
in
Time Complexity
split() → O(n)
Loop through words → O(n)

Overall:

Time Complexity = O(n)
Space Complexity = O(n)

where n is the length of the string.

-----------------------------------------------------------------------------------
s = "The sun sets in the west"
def longest(s):
    words = s.split()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = "00"
    ml = 0
    for word in words:
        if len(word) % 2 == 0 and word[0].lower() in vowels:
            if len(word) > ml:
                ml = len(word)
                res = word
    print(res)
longest(s)

