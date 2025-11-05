# Recursive Fibonacci Function
def recursive_fibo(n):
    if n in (0, 1):
        return n
    return recursive_fibo(n-1) + recursive_fibo(n-2)
# Non-Recursive (Iterative) Fibonacci Function
def non_recursive_fibo(n):
    first = 0
    second = 1
    fib_sequence = [first, second]
    for i in range(n - 2):
        third = first + second
        fib_sequence.append(third)
        first = second
        second = third
    return fib_sequence

n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Invalid Input. Please enter a positive integer.")
else:
    # Recursive Approach
    print("\nFibonacci Sequence using Recursion:")
    for i in range(n):
        print(recursive_fibo(i), end=" ")
    # Non-Recursive Approach
    print("\n\nFibonacci Sequence using Non-Recursion:")
    fib_iter = non_recursive_fibo(n)
    for num in fib_iter:
        print(num, end=" ")
-------------------------------------------------------------------------


Time & Space Complexity Analysis
Recursive Fibonacci:
Time Complexity: O(2^n)
Space Complexity: O(n) due to recursion stack
Non-Recursive Fibonacci:
Time Complexity: O(n)
Space Complexity: O(1)
-----------------------------------------
# Recursive Fibonacci Function
def recursive_fibo(n):
if n in (0, 1):
return n
return recursive_fibo(n-1) + recursive_fibo(n-2)

# Non-Recursive (Iterative) Fibonacci Function
def non_recursive_fibo(n):
first = 0
second = 1
fib_sequence = [first, second]
for i in range(n - 2):
third = first + second
fib_sequence.append(third)
first = second
second = third
return fib_sequence

n = int(input("Enter the number of terms: "))
if n <= 0:
print("Invalid Input. Please enter a positive integer.")
else:
# Recursive Approach
print("\nFibonacci Sequence using Recursion:")
for i in range(n):
print(recursive_fibo(i), end=" ")

# Non-Recursive Approach
print("\n\nFibonacci Sequence using Non-Recursion:")
fib_iter = non_recursive_fibo(n)
for num in fib_iter:
print(num, end=" ")
------------------------------------------------------------------------------



Line-by-Line Explanation
Recursive Fibonacci Function
# Recursive Fibonacci Function
def recursive_fibo(n):
Defines a function named recursive_fibo that takes one argument n (the term number).
This function will call itself to calculate Fibonacci numbers recursively.
if n in (0, 1):
return n
This is the base condition — it stops the recursion.
If n is 0 or 1, the function just returns n because:
F(0) = 0
F(1) = 1
These are the first two terms of the Fibonacci series.

return recursive_fibo(n-1) + recursive_fibo(n-2)
This is the recursive step.
The function calls itself twice:
recursive_fibo(n-1) → previous term
recursive_fibo(n-2) → term before the previous
Adds both results to get the current Fibonacci number.Example:
recursive_fibo(4) = recursive_fibo(3) + recursive_fibo(2)
→ which internally calls more recursive functions until base cases are reached.
Non-Recursive (Iterative) Fibonacci Function
def non_recursive_fibo(n):
Defines another function named non_recursive_fibo for iterative (loop-based) Fibonacci.
first = 0
second = 1
Initializes the first two numbers of the Fibonacci sequence.
first → 0
second → 1

fib_sequence = [first, second]
Creates a list called fib_sequence to store the Fibonacci numbers.
Starts the list with [0, 1].

for i in range(n - 2):
Starts a loop to generate the next Fibonacci numbers.
We subtract 2 because the first two terms are already known.
third = first + second
Calculates the next Fibonacci number by adding the previous two numbers.

fib_sequence.append(third)
Adds (appends) the newly calculated Fibonacci number to the list.

first = second
second = third
Updates the two previous terms for the next loop iteration.
Moves the window forward:
first ← second, second ← third

return fib_sequence
Returns the complete list of Fibonacci numbers after the loop finishes.
Main Program (User Input and Output)
n = int(input("Enter the number of terms: "))
Takes an integer input from the user — the number of terms to print.

if n <= 0:
print("Invalid Input. Please enter a positive integer.")
Checks for invalid input (like negative or zero).
Prints an error message and stops if invalid.

else:
If the input is valid, it runs both the recursive and non-recursive parts.
Recursive Output Section
print("\nFibonacci Sequence using Recursion:")
Prints a heading before showing the recursive Fibonacci numbers.
for i in range(n):
print(recursive_fibo(i), end=" ")
Loops from 0 to n-1.
Calls the recursive function for each term.
Prints all Fibonacci numbers in one line separated by spaces.
Non-Recursive Output Section
print("\n\nFibonacci Sequence using Non-Recursion:")
Prints a heading for the non-recursive output.
fib_iter = non_recursive_fibo(n)
Calls the iterative function to get a list of Fibonacci numbers and stores it in fib_iter.
for num in fib_iter:
print(num, end=" ")
Loops through the list and prints each Fibonacci number with a space.

Method	Time Complexity	Space Complexity	Notes
Recursive	O(2ⁿ)	O(n)	Many repeated function calls
Non-Recursive	O(n)	O(1)	Uses a simple loop, faster and memory-efficient
-----------------------------------------------------------------------------------------




Question
Q1. What is the Fibonacci series?
The Fibonacci series is a sequence where each number is the sum of the previous two numbers.
Example: 0, 1, 1, 2, 3, 5, 8, 13, …
Q2. What are the first two numbers of the Fibonacci series?
 0 and 1.
Q3. How is each new term generated in the Fibonacci series? By adding the two previous terms:
F(n) = F(n-1) + F(n-2)
Q4. Why do we study Fibonacci numbers in programming?To understand recursion, iteration, and performance differences between them.
Q5. What is recursion?
 Recursion is a process where a function calls itself directly or indirectly to solve a smaller version of the same problem
Q6. What is the base condition in your recursive Fibonacci function?
 if n in (0, 1): return n
This stops infinite recursion.
Q7. Why do we need a base condition in recursion?
Without it, the function would call itself infinitely and cause a stack overflow error.
Q8. What happens when you call recursive_fibo(4)? It breaks down as:
F(4) = F(3) + F(2)
F(3) = F(2) + F(1)
F(2) = F(1) + F(0)
→ Finally gives 3
Q9. What is the time complexity of recursive Fibonacci? Why?
 O(2ⁿ) — because it recomputes the same subproblems many times.
Q10. What is the space complexity of recursive Fibonacci?
 O(n) — because of the recursion call stack.
Q11. Why is recursion slower than iteration here?
Because recursion repeatedly calls functions and recalculates the same results many times.
Q12. What is iteration?
 Repeating a block of code using loops (like for or while) until a condition is met.
Q13. How does your non-recursive Fibonacci code work?
 It starts with 0 and 1, then uses a loop to calculate the next term by adding the previous two.
Q14. What is the time complexity of the iterative version?
 O(n) — the loop runs once for each term.
Q15. What is the space complexity of the iterative version?
 O(1) — it uses only a few variables (first, second, third).
Q16. Which version is better for large n and why? The non-recursive version — because it’s faster and uses less memory.
Q17. Can we improve the recursive version? How?
Yes, by using memoization or dynamic programming to store already computed results.Q18. What happens if the user enters 0 or a negative number? The program prints: “Invalid Input. Please enter a positive integer.”
Q19. What will be the output for n = 10?
 0 1 1 2 3 5 8 13 21 34
Q20. Why are there two print() sections in your program?
 To separately show output from the recursive and non-recursive functions for comparison.
Q21. What is the difference between recursion and iteration?
Feature	Recursion	Iteration
Control	Function calls itself	Uses loops
Memory use	More (stack frames)	Less (fixed variables)
Speed	Slower	Faster
Termination	Base condition	Loop condition

Q22. What is a stack overflow error?
 It happens when too many recursive calls fill up the memory stack — usually due to missing base condition or large n.
Q23. Can recursion be converted to iteration?
Yes. Every recursive logic can be rewritten using loops and stacks.
Q24. Why does recursion take more memory?
Each function call creates a new stack frame storing variables and return addresses.
Q25. What type of recursion is used in Fibonacci?
 Tree recursion — because each call branches into two more calls.
Q26. What is memoization? A technique to store results of previous computations to avoid recomputation.
Q27. How can memoization improve Fibonacci recursion?
 It reduces the time complexity from O(2ⁿ) to O(n).
________________________________________
Q1. What is the Fibonacci series?
It’s a sequence of numbers in which each term is the sum of the previous two terms.
Example: 0, 1, 1, 2, 3, 5, 8, 13, 
Q2. Who discovered the Fibonacci series?
 It was discovered by Leonardo Pisano Bogollo, also known as Fibonacci.
Q3. What is the general formula for the Fibonacci sequence?
 F(n) = F(n-1) + F(n-2)
with base values F(0) = 0 and F(1) = 1.
Q4. What is meant by “n-th Fibonacci number”? It’s the value at the nth position in the Fibonacci sequence.
Q5. Give an example calculation.
 If F(0) = 0, F(1) = 1, then
F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, F(6) = 8.
Q6. What is recursion?
 Recursion is a process where a function calls itself until a base condition is met
Q7. What is iteration (non-recursion)?
 Iteration uses loops (for or while) to repeat a process instead of function calls
Q8. What are the base conditions in the recursive Fibonacci function?
 When n <= 1, return n.
Q9What is the purpose of the base condition?
 To stop further recursive calls and prevent infinite recursion.
Q10. What happens when you call recur_fibo(5)?
 It breaks into smaller calls:
F(5) = F(4) + F(3) → F(3) + F(2) → … until base cases 0 and 1.
Q11. What is the time complexity of your recursive code?
 O(2ⁿ) — exponential, because each call generates two more calls.
Q12. What is the space complexity of recursive Fibonacci?
 O(n) — due to the recursion stack memory.
Q13. What is the time complexity of your non-recursive code?
O(n) — it calculates each term only once.
Q14. What is the space complexity of non-recursive Fibonacci?
 O(1) — only a few variables are used.
Q15. Which approach is more efficient and why?
 The non-recursive (iterative) approach is more efficient because it uses less time and memory.
Q16. Explain the working of the iterative algorithm.
Start with two variables n1 = 0, n2 = 1.
Print these two values.
Repeat:
nth = n1 + n2
Update n1 = n2, n2 = nth.
Continue until n terms are printed.
Q17. Explain the recursive algorithm using steps.
If n <= 1, return n.
Else, return fibo(n-1) + fibo(n-2).
Function keeps calling itself until base case reached.
Q18. Draw or explain the flowchart for both methods.
Non-recursive: Has a loop checking i <= n.
Recursive: Has a decision block checking n <= 1 and calls itself twice.
Q19. Why is the recursive Fibonacci slower?
Because it recalculates the same values multiple times (overlapping subproblems).
Q20. How can we optimize the recursive Fibonacci?
Using Memoization or Dynamic Programming to store previously computed results.
Q21. What is memoization?
It’s a technique of caching function results to avoid redundant computations.
Q22. Explain why iterative method has O(1) space complexity.
 Because it uses only fixed variables, not recursive calls or extra memory.
Q23. What is the importance of Fibonacci sequence in real life?

Found in nature (flower petals, shells, pinecones).
Used in computer algorithms and cryptography.
Used in finance (Fibonacci retracement levels in trading).
Q24. What are some mathematical properties of the Fibonacci sequence?
Ratio of consecutive numbers approaches the Golden Ratio (1.618).
It can be expressed using Binet’s formula.
Q25. What are the limitations of recursion?

Slower execution for large n.
High memory usage (stack overflow risk).
Harder to debug than iteration.
Q26. What is the prerequisite for this assignment?

Basic Python/Java programming.
Knowledge of recursion and loops.
Understanding of time and space complexity.
Q27. What is the objective of this assignment?
 To understand and implement both recursive and non-recursive Fibonacci programs and compare their performance (time & space complexity).
Q28. What is the conclusion of this assignment?
 We learned how Fibonacci series can be implemented recursively and iteratively, and understood the differences in their time and space efficiency.
Explain the logic of the recursive Fibonacci program.
It calls itself twice: F(n) = F(n-1) + F(n-2) until n <= 1, where it returns n.
What happens if you input n = 0 or a negative number?
The program prints “Please enter a positive integer”.
What is the base case in your recursive function?
if n <= 1: return n
What is the output for nterms = 7?
0, 1, 1, 2, 3, 5, 8
What is the time and space complexity of this recursive code?
Time: O(2^N) (exponential)
Space: O(N) (recursive stack)
Why is recursion inefficient for large n?
Because it recalculates the same values repeatedly.
How can you optimize it?
By using Dynamic Programming (DP) or memoization to store previously calculated results.
Which method has the best time complexity?
The optimized matrix and direct formula methods — O(log n).
Difference between recursion and DP?
Recursion: Recomputes values → exponential time.
DP: Stores results → linear time O(n).
What is space optimization in DP?
It reduces space from O(n) to O(1) by storing only the last two computed Fibonacci numbers.
Which method has O(log n) time complexity and how?
The matrix exponentiation method — it uses matrix power to compute Fibonacci efficiently.
Explain the matrix method.
It uses the matrix
[
\begin{bmatrix}1 & 1\ 1 & 0\end{bmatrix}^n
]
to derive the nth Fibonacci number using fast exponentiation.
What is the Fibonacci Sequence?
A series where each term is the sum of the previous two: 0, 1, 1, 2, 3, 5, 8, …
How does the Fibonacci series work mathematically?
F(n) = F(n−1) + F(n−2), with F(0)=0, F(1)=1.
What is the Golden Ratio?
The ratio of two successive Fibonacci numbers as n → ∞ ≈ 1.618.
What is the Fibonacci Search technique?
A search algorithm that divides the array into sections based on Fibonacci numbers, used in sorted arrays.
Real-life applications of Fibonacci series:
Nature (plant patterns, shells)
Music and art
Computer algorithms
Stock market (retracement levels)
Cryptography and quantum physics
How is it used in finance?
In Fibonacci retracement levels for predicting market corrections in trading.
Two scientific applications:
Used in quantum mechanics and cryptography.
Conclusion of your experiment/report:
The Fibonacci series was explored using recursive and non-recursive methods, understanding both time and space complexities.
What is T(2^N) exponential time?
It means execution time doubles with each increase in input size — very slow growth.
Write the iterative version (briefly):
a, b = 0, 1
for i in range(n):
print(a)
a, b = b, a + b
Difference between iterative and recursive approaches:
Iterative: Faster, uses loops, O(n) time, O(1) space.
Recursive: Slower, uses function calls, O(2^n) time, O(n) space.
Define Dynamic Programming.
A technique that solves problems by breaking them into overlapping subproblems and storing results.
How does memoization help?
It caches previously computed results, reducing time complexity from O(2^n) to O(n).
________________________________________


Code With Recursion : 
def recursive_fibo(n): 
if n in (0,1): 
return n 
return recursive_fibo(n-1) + recursive_fibo(n-2) 
n = 10 
if n < 0: 
print("Invalid Input") 
exit() 
print("Fibonacci Sequence :", end = " ") 
for i in range(n): 
print(recursive_fibo(i), end = ' ') 

Code Without Recursion : 
first = 0 
second = 1 
n = 10 
print("Fibonacci Sequence :", end = " ") 
print(first, second, end = ' ') 
for i in range(n-2): 
third = first + second 
print(third, end = ' ') 
first = second 
second = third

        ┌──────────────┐
        │  Start F(n)  │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Read n     │
        └──────┬───────┘
               │
 ┌─────────────▼─────────────────────────┐
 │ Initialize: F[0]=0, F[1]=1, i = 2     │
 └─────────────┬─────────────────────────┘
               │
        ┌──────▼────────┐
        │ i <= n-1 ?    │
        └──────┬────────┘
         Yes   │    No
        ┌──────▼─────┐   ┌──────────────┐
        │ F[i] =     │   │ return F[n-1]│
        │ F[i-1] +   │   └──────┬───────┘
        │ F[i-2]     │          │
        └──────┬─────┘     ┌────▼─────┐
               │            │ Stop     │
        ┌──────▼─────┐     └──────────┘
        │ i = i + 1  │
        └──────┬─────┘
               │
               └───(Loop back to condition)


