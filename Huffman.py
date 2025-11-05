
import heapq
#Imports a min-heap library used for priority queue operations.
#Huffman coding needs a min-heap to always pick the lowest-frequency characters first.
from collections import Counter
# Node structure for Huffman Tree
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    # For heapq to compare nodes
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree (Greedy)
def build_huffman_tree(text):
    frequency = Counter(text)  # Count frequency of each character
    heap = [Node(char, freq) for char, freq in frequency.items()]#Creates a Node object for each character and frequency.
    heapq.heapify(heap)  # Converts the list into a min-heap (priority queue).
    while len(heap) > 1:#Repeat until only one node remains 
        # Extract two nodes with smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)#Pop the two smallest frequency nodes 
        # Merge nodes
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)#Push the merged node back into heap
    return heap[0]  # Root of the Huffman tree

# Function to generate Huffman Codes
def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node is None:
        return code_map
    if node.char is not None:  # Leaf node
        code_map[node.char] = prefix
    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)#Left edge adds 0,Right edge adds 1

    return code_map
# Function to encode text
def huffman_encode(text):
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes
# Function to decode text
def huffman_decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_text = ""
    temp = ""
    for bit in encoded_text:
        temp += bit
        if temp in reverse_codes:
            decoded_text += reverse_codes[temp]
            temp = ""
    return decoded_text
# Driver Code
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    print("Original Text:", text)
    print()
    encoded_text, codes = huffman_encode(text)
    print("Huffman Codes:", codes)
    print()
    print("Encoded Text:", encoded_text)
    print()
    decoded_text = huffman_decode(encoded_text, codes)
    print("Decoded Text:", decoded_text)
---------------------------------------------------------------------

EXPLANATION
Importing Libraries
import heapq
from collections import Counter
heapq: provides min-heap (priority queue) used for greedy selection of smallest frequencies
Counter: counts frequency of each character in the text

Node Class for Huffman Tree
class Node:
def __init__(self, char=None, freq=0):
self.char = char
self.freq = freq
self.left = None
self.right = None
Defines a node in the Huffman tree
Stores:
char → character
freq → frequency of character
left & right pointers for binary tree structure
Comparison Logic for Heap

def __lt__(self, other):
return self.freq < other.freq
__lt__ = less than
It defines how to compare two objects when using the < operator.

Build Huffman Tree
def build_huffman_tree(text):
frequency = Counter(text) 
Counts frequency of each character in input text.
heap = [Node(char, freq) for char, freq in frequency.items()]
Creates a Node object for each character and frequency.
heapq.heapify(heap)
Converts the list into a min-heap (priority queue).
while len(heap) > 1:
Repeat until only one node remains (root of tree)
left = heapq.heappop(heap)
right = heapq.heappop(heap)
Pop the two smallest frequency nodes (Greedy choice)
merged = Node(freq=left.freq + right.freq)
merged.left = left
merged.right = right
Create a new internal node with combined frequency
Attach left & right children
heapq.heappush(heap, merged)
Push the merged node back into heap
return heap[0]
When loop ends → only root node remains

Generate Huffman Codes
def generate_codes(node, prefix="", code_map=None):
if code_map is None:
code_map = {}
Start recursion from the root node
prefix stores the binary code being built
code_map will store codes for each character
if node is None:
return code_map
Base case — empty node
if node.char is not None:
code_map[node.char] = prefix
If node has a character (leaf) → store the binary code
generate_codes(node.left, prefix + "0", code_map)
generate_codes(node.right, prefix + "1", code_map)
Recursive call:
Left edge adds 0
Right edge adds 1

Encode Function
def huffman_encode(text):
root = build_huffman_tree(text)
Build Huffman tree#Creates tree nodes
codes = generate_codes(root)
Traverse the tree
Assign binary codes
Left child → 0
Right child → 1
encoded_text = ''.join(codes[char] for char in text)
This replaces each character in text with its Huffman code.
return encoded_text, codes

Return encoded string & code dictionary
Decode Function
reverse_codes = {v: k for k, v in codes.items()}
Reverse mapping (binary→character)#We reverse because during decoding, we read bits 
#and try to match codes to get characters.
decoded_text = ""
temp = ""
decoded_text → final decoded output string
temp → stores bits until they match a codefor bit in encoded_text:
temp += bit#We add bits one by one and check if they form a valid code.
if temp in reverse_codes:
decoded_text += reverse_codes[temp]
temp = ""
#Convert bits to character,Add to decoded_text,Reset temp to read next bits

Main Program
text = "this is an example for huffman encoding"
Input string
encoded_text, codes = huffman_encode(text)
Encode text
decoded_text = huffman_decode(encoded_text, codes)
Decode to verify correctness
-----------------------------------------------------------------------------


Questions
Q1: What is Huffman Encoding?
Huffman encoding is a lossless compression algorithm that assigns shorter binary codes to frequent characters and longer codes to less frequent ones.
Q2: Why is Huffman coding a greedy algorithm?
Because at each step, it selects the two smallest frequency nodes and merges them — a greedy choice.
Q3: What data structure is used here?
A min-heap (priority queue) is used to always pick the smallest frequency nodes.
Q4: What is the time complexity?
Time complexity: O(n log n)
(Heap operations for n characters)
Q5: Why do we assign 0 to left and 1 to right?
It's a convention that helps generate unique prefix codes (no code is prefix of another).
Q6: What does Counter() do?
Counter() counts the frequency of each character in the input string.
Q7: What is the purpose of the Node class?
Node represents a tree node storing:
•	character
•	frequency
•	left and right child pointers
Q8: Why do we override __lt__ (less-than) method?
To allow comparing nodes by frequency inside the heap.
Q9: What does heapq.heapify() do?
It converts the list into a min-heap, allowing efficient extraction of minimum frequency items.
Q10: What does huffman_encode() return?
It returns:
1.	Encoded binary string
2.	Dictionary {char: code}
Q11: Why do we use recursion in generate_codes()?
To traverse the tree and generate binary codes for each character.
Q12: Why do we reverse dictionary in decoding?
To map code → character during decoding efficiently.
Q13: What is the difference between encoding and decoding?
Encoding: convert characters → binary
Decoding: convert binary → characters
Q14: Is Huffman coding prefix-free?
Yes, no Huffman code is a prefix of another — ensures unique decoding.
Q15: Where is Huffman coding used in real life?
•	ZIP/RAR file compression
•	JPEG/MPEG media compression
•	Network compression
Q16: Can Huffman coding handle space and punctuation?
Yes, it treats them like regular characters.
Q17: What happens if all characters have same frequency?
Tree shape changes but still valid — each gets equal-length code.
Q18: What happens if there is only one character?
It assigns code 0.
Q19: Is this algorithm static or dynamic?
This implementation is static Huffman coding.
Q20: Why do we merge the smallest two frequencies?
To minimize total code length — optimal prefix tree.

1. What is a Greedy Method?
A greedy method is an approach for solving optimization problems by selecting the best option available at each step, hoping that this local choice will lead to a globally optimal solution.
It always chooses the best immediate solution without worrying about future consequences.
2. What are the advantages of the Greedy Approach?
1.	It is simple and easy to understand.
2.	It requires less computational time compared to other algorithms.
3.	It is efficient for problems where local optimization leads to global optimization.
3. What are the drawbacks of the Greedy Approach?
The greedy approach does not always produce the optimal global solution.
It may get stuck at a local optimum because it never revises previous choices.
4. What is Huffman Encoding?
Huffman Encoding is a lossless data compression algorithm that uses variable-length codes for characters. Characters that occur more frequently are assigned shorter codes, while rare characters get longer codes.
It is based on the Greedy method.
5. What is the Huffman Rule?
Huffman coding follows the prefix rule, meaning no code assigned to a character is a prefix of the code for another character.
This prevents any ambiguity during decoding.
6. What are the main steps in Huffman Coding?
1.	Calculate the frequency of each character.
2.	Sort the characters in increasing order of frequency.
3.	Create a leaf node for each character.
4.	Combine the two nodes with the smallest frequency into a new node (sum of both).
5.	Repeat until only one node remains — this becomes the Huffman Tree.
6.	Assign binary codes (0 to left, 1 to right) to each edge.
7. How does Huffman Encoding achieve compression?
By assigning shorter codes to frequent characters and longer codes to rare ones, Huffman Encoding reduces the total number of bits needed to represent data, thus achieving lossless compression.
8. What is the time complexity of Huffman Coding?
If there are n characters,
•	Building the priority queue: O(n)
•	Extracting and merging nodes: O(n log n)
Overall time complexity = O(n log n)
9. What are the applications of Huffman Encoding?
Used in file compression (e.g., ZIP files).
•	Multimedia formats like JPEG, MP3, and PNG.
•	Data transmission where efficient encoding saves bandwidth.
10. Why is Huffman Encoding considered a Greedy Algorithm?
11. What is meant by a prefix code?
Answer:
A prefix code ensures that no code is a prefix of another code, making decoding unambiguous and efficient
 12. What programming languages can be used to implement Huffman Encoding?
It can be implemented using Python, Java, or C++
 13. What was the objective of your assignment?
The objective was to understand and implement Huffman Encoding using the Greedy Method, and to learn how data compression can be achieved efficiently.
14. Give a real-life example of Huffman Encoding.
Sppose a text string has characters A, B, and C with frequencies 5, 9, and 12.
Using Huffman Encoding, shorter codes are assigned to the most frequent characters, reducing total bit size — hence saving storage space.
 15. What is the output of your Python program?
The program outputs the Huffman codes for each character and the compressed encoded string.

