Assignment: Asymptotic Notations and Correctness of Algorithms 

[You may include handwritten submission for the parts of the assignment that are difficult to type, like equations, rough graphs etc., but make sure it is legible for the graders. Regrade requests due to the illegible parts of the work will not be accepted.] 

1. **Identify and compare the order of growth**: Identify if the following statements are true or false. Prove your assertion using any of the methods shown in the exploration. Draw a rough graph marking rough c and n values if the statement is True. [You don’t have to find the values of c 

0

and n , just mention as c and n in your graphs]. 

0  0

1. n(n+1)/2 ∈ O(n3) 
1. n(n+1)/2 ∈ Θ(n2) 
1. 10n-6  ∈ Ω(78n + 2020) 
1. n! ∈ Ω (0.00001n) 
2. **Read and Analyze Pseudocode:** Consider the following algorithm 

Classified(A...n-1): 

`    `minval = A[0] 

`    `maxval = A[0] 

`    `for i = 1 to n-1: 

`        `if A[i] < minval: 

`            `minval = A[i] 

`        `if A[i] > maxval 

`            `maxval = A[i] 

`    `return maxval – minval 

1. What does this algorithm compute? 
1. What is its basic operation (i.e. the line of code or operation that is executed maximum number of times)?  
1. How many times is the basic operation executed? 
1. What is the time complexity of this algorithm? 
3. **Using mathematical induction prove below non-recursive algorithm:** 

def reverse\_array(Arr): 

`    `n = len(Arr) 

`    `i = (n-1)//2 

`    `j = n//2 

`    `while(i>= 0 and j <= (n-1)):         temp = Arr[i] 

`        `Arr[i] = Arr[j] 

`        `Arr[j] = temp 

`        `i = i-1 

`        `j = j+1 

1. Write the loop invariant of the reverse\_array function. 
1. Prove correctness of reverse\_array function using induction. 

----------------------(Ungraded question: you can try this question if time permits)---------------  Any number greater than 8 can written in terms of three or five.  

1. Write a pseudocode of algorithm that that takes a number greater than 8 and returns a tuple (x,y); where x represents number of threes and y represent number of fives make that number 

If number = 8 your pseudocode should return (1,1) 

2. Code your pseudocode into python and name your file ThreeAndFive.py  

Debriefing (required!): --------------------------

Report: 

Fill the report in the Qualtrics survey, you can access the link[ here.](https://oregonstate.qualtrics.com/jfe/form/SV_3aXU2MaGPfYnBLU) [(https://oregonstate.qualtrics.com/jfe/form/SV_3aXU2MaGPfYnBLU) ](https://oregonstate.qualtrics.com/jfe/form/SV_3aXU2MaGPfYnBLU)

Note: ‘Debriefing’ section is intended to help us calibrate the assignments. 
