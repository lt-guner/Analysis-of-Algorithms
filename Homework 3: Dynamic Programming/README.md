Assignment: Dynamic Programming 

1. **Solve a problem using top-down and bottom-up approaches of Dynamic Programming technique** 

DNA sequence is made of characters A, C, G and T, which represent nucleotides. A sample DNA string can be given as ‘ACCGTTTAAAG’. Finding similarities between two DNA sequences is a critical computation problem that is solved in bioinformatics. 

![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.001.png) Given two DNA strings find the length of the longest common string alignment between them (it need not be continuous). Assume empty string does not match with anything. 

Example: DNA string1: ATAGTTCCGTCAAA    ;     DNA string2: GTGTTCCCGTCAAA 

A  T  A  G  T  T  C  C  G T  C  A  A  A ![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.002.png)![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.003.png)G T  G  T  T ![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.004.png)C  C  C  G T  C  A  A  A ![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.005.png)![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.006.png)![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.007.png)![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.008.png)![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.009.png)![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.010.png)![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.011.png)![](Aspose.Words.6afd4164-15db-41f6-8acb-306dee9baf87.012.png)

Length the best continuous length of the DNA string alignment: 12 (TGTTCCGTCAAA) 

1. Implement a solution to this problem using Top-down Approach of Dynamic Programming, name your function **dna\_match\_topdown(DNA1, DNA2)** 
1. Implement a solution to this problem using Bottom-up Approach of Dynamic Programming, name your function **dna\_match\_bottomup(DNA1, DNA2)** 
1. Explain how your top-down approach different from the bottom-up approach? 
1. What is the time complexity and Space complexity using Top-down Approach 
1. What is the time complexity and Space complexity using Bottom-up Approach 
1. Write the subproblem and recurrence formula for your approach. If the top down and bottom-up approaches have the subproblem recurrence formula you may write it only once, if not write for each one separately.  

Name your file **DNAMatch.py** 

2. **Solve Dynamic Programming Problem and Compare with Naïve approach** 

You are playing a puzzle. A random number N is given, you have blocks of length 1 unit and 2 units. You need to arrange the blocks back to back such that you get a total length of N units. In how many distinct ways can you arrange the blocks for given N. 

1. Write a description/pseudocode of approach to solve it using Dynamic Programming paradigm (either top-down or bottom-up approach) 
1. Write pseudocode/description for the brute force approach 
1. Compare the time complexity of both the approaches 
1. Write the recurrence formula for the problem 

Example 1: 

Input: N=2, Result: 2 

Explanation: There are two ways. (1+1 , 2) 

Example 2: 

Input: N=3, Result: 3 

Explanation: There are three ways (1+1+1, 1+2, 2+1) 

Debriefing (required!): -------------------------- Report: 

Fill the report in the Qualtrics survey, you can access the link[ here.](https://oregonstate.qualtrics.com/jfe/form/SV_6As0QKSDULDVnLg) 

[(https://oregonstate.qualtrics.com/jfe/form/SV_6As0QKSDULDVnLg ](https://oregonstate.qualtrics.com/jfe/form/SV_6As0QKSDULDVnLg)) 

Note: ‘Debriefing’ section is intended to help us calibrate the assignments. 
