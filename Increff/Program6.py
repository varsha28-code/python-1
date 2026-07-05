def find_action(input1,input2):
    act=set(input1.split())
    sent=input2.split()
    n=len(sent)
    for i, w in enumerate(sent):
        if w in act:
            if i+1<n:
                next=sent[i+1]
                if next.lower()=="the":
                    if i+2<n:
                        return f"{w}{sent[i+2]}"
                else:
                    return f"{w}{next}"
    return None
input1 = "turn open close switch"
input2 = "please the fan off"
print( find_action(input1,input2))
------------------------------------------------------------------
Dry Run
Step 1
act = set(input1.split())

input1.split() gives

['turn', 'open', 'close', 'switch']

So,

act = {'turn', 'open', 'close', 'switch'}
Step 2
sent = input2.split()

Result:

['please', 'the', 'fan', 'off']

Length:

n = 4
Step 3

Loop through every word.

Iteration 1
i = 0
w = "please"

Check

if w in act

Is "please" in

{'turn','open','close','switch'}

No.

Move to next iteration.

Iteration 2
i = 1
w = "the"

Is "the" an action?

No.

Iteration 3
i = 2
w = "fan"

Is "fan" an action?

No.

Iteration 4
i = 3
w = "off"

Is "off" an action?

No.

Loop ends.

No action word was found.

Therefore,

return None
Output
None
Why?

Your function expects an action word like

turn
open
close
switch

to already exist in the sentence.

But your sentence is

please the fan off

which contains

please
the
fan
off

There is no action word.

Hence it returns

None
Example where it works
input1 = "turn open close switch"
input2 = "please turn the fan off"

Dry run:

Finds "turn"
Next word = "the"
Skips "the"
Returns
turnfan
