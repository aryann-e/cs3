Annex C
---
Code Quality Assessment Worksheet
---
Section: Samat Score:____________

C# / Name: #8 / Aryann Theodore Millo    Date: 8/16/2026
Groupmates: Aryann Theodore Millo and Giovanni Roliz Gamboa


Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


*PseudoCode 1:*


Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm


*PseudoCode 2:*


Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm



*1. Efficiency*
Which algorithm is faster when the list of numbers is very large? Why?

Pseudocode 1 is faster because it is shorter than pseudocode 2, using only one loop. While pseudocode 2 uses two loops, making more comparisons than Pseudocode 1.



*2. Readability*
Which algorithm is easier to understand at first glance? What makes it clearer?

Pseudocode 1 is easier to read because it has less lines of code and is more simple. It tracks the biggest number it finds and only updates when its found a bigger one.



*3. Maintainability*
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

If we had to add new features to the code, pseudocode 1 would be easier, as it only has one loop. Instead of having 2 loops to worry about, like in pseudocode 2.



*4. Testability*
Which algorithm is easier to test with different inputs? Why?

Pseudocode 1 is easier to test than pseudocode 2 because it is very straightforward and has a simpler structure overall.




*5. Security*
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

The algorithm should check if the list is valid, for example, if it isn't empty, to not try to access numbers[0] with no elements.


 

*6. Final Answer*
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

Overall, the best algorithm to use is algorithm 1; this is because it is overall simpler to understand and quicker to use. If we ever need to adjust something or maybe want to change something for whatever reason, we can easily do it.
