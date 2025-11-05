# Fractional Knapsack using Greedy Method
def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = []
    # Calculate value/weight ratio and store items as tuples
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i], i))  # store index too
    # Sort items in descending order of ratio
    items.sort(reverse=True, key=lambda x: x[0])
    total_value = 0
    fractions = [0] * n   # To store fraction of each item taken
    for ratio, value, weight, index in items:
        if capacity >= weight:
            # Take full item
            capacity -= weight
            total_value += value
            fractions[index] = 1
        else:
            # Take fractional part
            fraction = capacity / weight
            total_value += value * fraction
            fractions[index] = fraction
            break   # Knapsack is full
    return total_value, fractions
# Driver Code
if __name__ == "__main__":
    values = [60, 100, 120]  # Values of items
    weights = [10, 20, 30]   # Weights of items
    capacity = 50            # Maximum capacity of knapsack
    max_value, fractions_taken = fractional_knapsack(values, weights, capacity)
    print("Maximum Value in Knapsack =", max_value)
    print("Fractions of items taken =", fractions_taken)


 Line-by-Line Explanation
# Fractional Knapsack using Greedy Method 
def fractional_knapsack(values, weights, capacity):
Defines a function to calculate maximum profit.
    n = len(values)
    items = []
n = number of items, items list to store ratio + value + weight.
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))
Calculates value/weight ratio for each item and stores all info.
    items.sort(reverse=True, key=lambda x: x[0])
Sorts items in descending order of ratio (Greedy step — highest ratio first)
    total_value = 0
    fractions = [0] * n
total_value stores answer; fractions tracks which fraction of each item we take.
    for ratio, value, weight in items:
        if capacity >= weight:
Loop through items, check if full item can fit.
            capacity -= weight
            total_value += value
            fractions[values.index(value)] = 1
If yes → add full item (fraction = 1)
        else:
            fraction = capacity / weight
            total_value += value * fraction
            fractions[values.index(value)] = fraction
            break
Else → take only the fraction that fits, then stop (bag full)
    return total_value, fractions
Return max value & fractions list
________________________________________
 Driver Code Output Explanation
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
Sorted by ratio:
Item	V	W	Ratio
60	10	10	6
100	20	20	5
120	30	30	4
Knapsack capacity = 50
•	Take item1 completely → 10kg
•	Take item2 completely → 20kg
•	Left capacity = 20, item3 weight = 30 → take 20/30 fraction
Final Output:
Max value = 240
Fractions taken = [1, 1, 0.6666]
________________________________________ 
Questions
Q1: What is the Fractional Knapsack problem?
Ans: It maximizes profit by taking whole or fractional parts of items based on value/weight ratio.
Q2: Why is the greedy approach used?
Ans: Because choosing the highest value/weight ratio first always gives optimal solution.
Q3: Difference between 0/1 Knapsack & Fractional Knapsack?
0/1 Knapsack	Fractional Knapsack
Can't break items	Items can be divided
Uses DP	Uses Greedy
Not always greedy optimal	Greedy gives optimal
Q4: Time complexity?
Ans: O(n log n) due to sorting.
Q5: Real-life example?
Ans: Filling a bag with gold/sand — you can take fractions to maximize value.
Q1. What is the Fractional Knapsack problem?
It is a problem where we can take fractions of items to maximize total profit within a given weight capacity.
Q2. Why do we use Greedy Approach here?
Because selecting items based on the highest value/weight ratio first gives the optimal solution for this problem.
Q3. Difference between 0/1 Knapsack & Fractional Knapsack?
0/1 Knapsack	Fractional Knapsack
Can't take fraction	Can take fraction
DP required	Greedy is optimal
More complex	Simple & faster

Q4. What is the greedy strategy used?
Sort items by value/weight ratio in descending order and pick maximum possible from each item
Q5. Real Life Example?
Filling a bag with gold powder or rice — you can take fractions to maximize value.Q6. Why do we calculate value/weight ratio?
To determine which item gives maximum profit per unit weight.
Q7. Why do we sort items?
To always pick the best (highest ratio) item first — greedy choice.
Q8. What does fractions list store?
It stores how much portion of each item we took:
1 → full item taken
0.x → fraction taken
0 → not taken
Q9. Time complexity?
O(n log n) due to sorting.
Q10. Can greedy fail for knapsack problems?
Yes
Greedy works only for Fractional Knapsack.
For 0/1 Knapsack, greedy can fail — need Dynamic Programming.
Q11. Why do we break after taking a fractional part?
Because the knapsack is full after taking the remaining capacity — no more items can fit.
Q12. What happens if two items have same ratio?
Either can be chosen first — result remains optimal.
Q13. For values = [60,100,120], weights=[10,20,30], capacity=50
Answer:
Take items	Weight	Value
Whole #1	10	60
Whole #2	20	100
⅔ of #3	20	80
Total value = 240
________________________________________
1. What is Greedy Approach?
Answer:
A greedy approach is an algorithmic strategy for solving optimization problems by making a sequence of choices, each of which looks the best at the moment.
At every step, it chooses the option that provides the most immediate benefit without reconsidering previous choices.
Although it may not always produce the global optimum, it is often efficient and simple to implement.
Advantages:
•	Easy to describe and implement.
•	Often faster than other algorithms (e.g., dynamic programming).
Disadvantages:
•	Does not always produce an optimal solution for all problems.
•	Works best for problems with the greedy choice property and optimal substructure.
2. Explain concept of Fractional Knapsack.
Answer:
The fractional knapsack problem is a variation of the 0/1 knapsack problem where items can be divided into smaller parts.
The goal is to maximize the total value in a knapsack of limited capacity by taking fractions of items if taking the whole item would exceed the capacity.
Example:
If the remaining capacity is 10 kg and the next item weighs 20 kg, you can take half of it.
Formula:
[
\text{Maximize } \sum \frac{v_i}{w_i} \text{ (value per unit weight)}
]
3. Differentiate between Fractional and 0/1 Knapsack.
Feature	Fractional Knapsack	0/1 Knapsack
Item Selection	Items can be divided (take fractions)	Items cannot be divided (take all or none)
Approach	Solved using Greedy Method	Solved using Dynamic Programming
Time Complexity	( O(n \log n) )	( O(nW) )
Optimal Solution	Always optimal	May need exhaustive or dynamic approach
Example	Can take ½ of an item	Must take full item or none

4. Solve one example based on Fractional Knapsack (Other than Manual).
Item	Weight	Value
1	10	60
2	20	100
3	30	120
Knapsack Capacity (W) = 50
Step 1: Compute Value/Weight ratio:
Item 1 → 6, Item 2 → 5, Item 3 → 4
Step 2: Sort in decreasing order of ratio:
(1), (2), (3)
Step 3: Fill the knapsack:
•	Take full Item 1 (weight = 10, value = 60)
•	Take full Item 2 (weight = 20, value = 100)
•	Remaining capacity = 20 kg
→ Take 20/30 of Item 3 = (20/30) × 120 = 80
Total Value = 60 + 100 + 80 = 240
Maximum profit = 240 units
5. What is the Time Complexity of Fractional Knapsack using Greedy Method?
Answer:
The main time complexity arises from sorting items by their value/weight ratio.
•	Sorting takes: ( O(n \log n) )
•	Filling the knapsack takes: ( O(n) )
 Total Time Complexity = O(n log n)
________________________________________
6. Write a Python Program for Fractional Knapsack using Greedy Method.
Answer:
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractionalKnapsack(W, arr):
    # Sort items by value/weight ratio
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)

    final_value = 0.0

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            final_value += item.value
        else:
            final_value += item.value * (W / item.weight)
            break

    return final_value

# Driver Code
if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    print("Maximum value we can obtain =", fractionalKnapsack(W, arr))
✅ Output:
Maximum value we can obtain = 240.0
________________________________________
