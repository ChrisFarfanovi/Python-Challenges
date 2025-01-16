# 🐍 Python Challenges

## 👋Intro

The idea here is to provide some simple puzzles to stretch our scripting muscles.

These challenges are mostly inspired by the Contracts found in [Bitburner](https://store.steampowered.com/app/1812820/Bitburner/)

## 🚦 Getting Started

To get started - simply fork this repo for yourself.

From there you can make any changes you like and use Github to track your own code.

Make sure to sync your fork periodically so that any new challenges get added automatically.

If you have any questions or suggestions just message me, [open a discussion](https://github.com/ChrisFarfanovi/Python-Challenges/discussions/new/choose) or [open a new issue](https://github.com/ChrisFarfanovi/Python-Challenges/issues/new?template=Blank+issue).

## 🏗️ Structure

🔢 Each challenge is numbered, but the number is not particularly indicative of difficulty. Each one contains the following:

| Document | Purpose |
|-:|:-|
| `briefing.md` | A document describing the challenge and any relevant information |
| `challenge.py` | This script is used to generate data for, and check solutions for, each challenge. |
| `my_solution.py` | This is where you write your own solution. Some challenges may come with some information pre-populated. |
| `community_solutions.py` | [optional] A folder for community solutions |
| `example_solution.ipynb` | [optional] Some Challenges may include an example/worked solution (these will typically be `.ipynb` notebooks) |
| `solver_stress_tester.py` | [optional] This script allows you to check your solver dynamically and stress-test it against thousands of versions of the challenge. |

⛔ ***Do not*** modify the `challenge.py` script as this may break the challenges. You ***can***, however, analyse the code found here to help you with certain challenges.

💪 Give each challenge a good old college-try, but if you struggle, don't worry, you may learn a technique in a following challenge that ends up helping you with previous ones.

📬 Don't be afraid to get in touch if you encounter any issues.

📓 I'd recommend using `Jupyter`/`ipynb` for working through some of these problems as more complex problems can be hard to keep track of.

## 📑 Challenge List

### ✅ Done

[00-Getting_familiar](/00-Getting_familiar/briefing.md)

#### 🔢 Maths

[01-Prime_Factor](/Maths/01-Maths-Prime_Factor/briefing.md)

#### 🔐 Cryptography

[01-Caesar_Cipher_I](/Cryptography/01-Caesar_Cipher_I/briefing.md)

### 🛠️ WIP

[0?-Close-enough_Prime](/WIP/0?-Closest_Prime/briefing.md)

### ❓ To-do

#### Parsing integer sequences

Taking a string formatted like this `1,4-6,33,50` and making a list of all the integers this string refers to.

#### Parsing parentheses I

(inspired by [Bitburner - Sanitize Parenthesis in expression](#sanitize-parentheses-in-expression))

Taking a string and determining if the parentheses `()` are all closed or not.

#### Parsing parentheses II

As with [Parsing parentheses I](#parsing-parentheses-i)

Now with brackets `[]` and braces `{}`

#### Parsing parentheses III

As with [Parsing parentheses II](#parsing-parentheses-ii)

Removing empty pairs to reduce the complexity of the expression.

### 🔥 Bitburner Challenges

Mostly from [here](https://github.com/bitburner-official/bitburner-src/blob/stable/src/data/codingcontracttypes.ts)

#### ✅ Largest Prime Factor ([01-Maths-Prime_Factor](/01-Maths-Prime_Factor/briefing.md))

Given a number, find its largest prime factor. A prime factor is a factor that is a prime number.

#### Sub-array with Maximum Sum

Given an array of integers, find the contiguous sub-array (containing at least one number) which has the largest sum and return that sum.

#### Total Ways to Sum I

Given a number, how many different distinct ways can that number be written as a sum of at least two positive integers?

#### Total Ways to Sum II

You are given an array with two elements. The first element is an integer n.

The second element is an array of numbers representing the set of available integers.

How many different distinct ways can that number n be written as a sum of integers contained in the given set?

You may use each integer in the set zero or more times.

#### Spiral-ise Matrix

Given an array of array of numbers representing a 2D matrix, return the elements of that matrix in clockwise spiral order.

Example: The spiral order of

`[ 1, 2, 3, 4]`  
`[ 5, 6, 7, 8]`  
`[ 9,10,11,12]`

is

`[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]`

#### Array Jumping Game I

You are given an array of integers where each element represents the maximum possible jump distance from that position. For example, if you are at position i and your maximum jump length is n, then you can jump to any position from i to i+n.

Assuming you are initially positioned at the start of the array, determine whether you are able to reach the last index of the array.

#### Array Jumping Game II

You are given an array of integers where each element represents the maximum possible jump distance from that position. For example, if you are at position i and your maximum jump length is n, then you can jump to any position from i to i+n.

Assuming you are initially positioned at the start of the array, determine the minimum number of jumps to reach the end of the array.

If it’s impossible to reach the end, then the answer should be 0.

#### Merge Overlapping Intervals

Given an array of intervals, merge all overlapping intervals. An interval is an array with two numbers, where the first number is always less than the second (e.g. [1, 5]).

The intervals must be returned in ASCENDING order.

Example:

```txt
[1, 3], [8, 10], [2, 6], [10, 16]
```

Looks like:

```txt
1 2 3
              8 9 10
  2 3 4 5 6
                  10 11 12 13 14 15 16
```

Merges into:

```txt
1 2 3 4 5 6 |
            | 8 9 10 11 12 13 14 15 16
            |
          (Gap)
```

Becomes:

```txt
[1, 6], [8, 16]
```

#### Generate IP address

Given a string containing only digits, return an array with all possible valid IP address combinations that can be created from the string.

An octet in the IP address cannot begin with ‘0’ unless the number itself is actually 0. For example, “192.168.010.1” is NOT a valid IP.

Examples:

`25525511135` => `[255.255.11.135, 255.255.111.35]`

`1938718066` => `[193.87.180.66]`

#### Algorithmic Stock Trader I

You are given an array of numbers representing stock prices, where the i-th element represents the stock price on day i.

Determine the maximum possible profit you can earn using at most one transaction (i.e. you can buy an sell the stock once). If no profit can be made, then the answer should be 0. Note that you must buy the stock before you can sell it.

#### Algorithmic Stock Trader II

You are given an array of numbers representing stock prices, where the i-th element represents the stock price on day i.

Determine the maximum possible profit you can earn using as many transactions as you’d like. A transaction is defined as buying and then selling one share of the stock. Note that you cannot engage in multiple transactions at once. In other words, you must sell the stock before you buy it again. If no profit can be made, then the answer should be 0.

#### Algorithmic Stock Trader III

You are given an array of numbers representing stock prices, where the i-th element represents the stock price on day i.

Determine the maximum possible profit you can earn using at most two transactions. A transaction is defined as buying and then selling one share of the stock. Note that you cannot engage in multiple transactions at once. In other words, you must sell the stock before you buy it again. If no profit can be made, then the answer should be 0.

#### Algorithmic Stock Trader IV

You are given an array with two elements. The first element is an integer k. The second element is an array of numbers representing stock prices, where the i-th element represents the stock price on day i.

Determine the maximum possible profit you can earn using at most k transactions. A transaction is defined as buying and then selling one share of the stock. Note that you cannot engage in multiple transactions at once. In other words, you must sell the stock before you can buy it. If no profit can be made, then the answer should be 0.

#### Minimum Path Sum in a Triangle

You are given a 2D array of numbers (array of array of numbers) that represents a triangle (the first array has one element, and each array has one more element than the one before it, forming a triangle). Find the minimum path sum from the top to the bottom of the triangle. In each step of the path, you may only move to adjacent numbers in the row below.

#### Unique Paths in a Grid I

You are given an array with two numbers: [m, n]. These numbers represent a m x n grid. Assume you are initially positioned in the top-left corner of that grid and that you are trying to reach the bottom-right corner. On each step, you may only move down or to the right.

Determine how many unique paths there are from start to finish.

#### Unique Paths in a Grid II

You are given a 2D array of numbers (array of array of numbers) representing a grid. The 2D array contains 1’s and 0’s, where 1 represents an obstacle and

0 represents a free space.

Assume you are initially positioned in top-left corner of that grid and that you are trying to reach the bottom-right corner. In each step, you may only move down or to the right. Furthermore, you cannot move onto spaces which have obstacles.

Determine how many unique paths there are from start to finish.

#### Shortest Path in a Grid

Assume you are initially positioned in top-left corner of that grid and that you are trying to reach the bottom-right corner. In each step, you may move to the up, down, left or right. Furthermore, you cannot move onto spaces which have obstacles.

Determine if paths exist from start to destination, and find the shortest one.

Examples:

```txt
[[0,1,0,0,0],  
 [0,0,0,1,0]]

= "DRRURRD"
```

```txt
[[0,1],
 [1,0]]

= “”
```

#### Sanitize Parentheses in Expression

Given a string with parentheses and letters, remove the minimum number of invalid
parentheses in order to validate the string. If there are multiple minimal ways
to validate the string, provide all of the possible results.

The answer should be provided as an array of strings. If it is impossible to validate
the string, the result should be an array with only an empty string.

Examples:

```txt
()())() -> [()()(), (())()]

(a)())() -> [(a)()(), (a())()]

)( -> [“”]
```

#### Find All Valid Math Expressions

You are given a string which contains only digits between 0 and 9 as well as a target
number. Return all possible ways you can add the +, -, and * operators to the string
of digits such that it evaluates to the target number.

The answer should be provided as an array of strings containing the valid expressions.

NOTE: Numbers in an expression cannot have leading 0’s
NOTE: The order of evaluation expects script operator precedence

Examples:

```txt
Input: digits = “123”, target = 6
Output: [1+2+3, 1*2*3]

Input: digits = “105”, target = 5
Output: [1*0+5, 10-5]
```

#### HammingCodes: Integer to Encoded Binary

You are given a decimal value.

Convert it into a binary string and encode it as a ‘Hamming-Code’. eg:

Value 8 will result into binary ‘1000’, which will be encoded with the pattern ‘pppdpddd’, where p is a paritybit and d a databit,  or ‘10101’ (Value 21) will result into (pppdpdddpd) ‘1001101011’.

NOTE: You need an parity Bit on Index 0 as an ‘overall’-paritybit.

NOTE 2: You should watch the [HammingCode-video from 3Blue1Brown](https://youtu.be/X8jsijhllIA?si=R7-8k3qSxQxaiAyb), which explains the ‘rule’ of encoding, including the first Index parity-bit mentioned on the first note.

Now the only one rule for this encoding:

It’s not allowed to add additional leading ‘0’s to the binary value That means, the binary value has to be encoded as it is

#### HammingCodes: Encoded Binary to Integer

You are given an encoded binary string.

Treat it as a Hammingcode with 1 ‘possible’ error on an random Index.

Find the ‘possible’ wrong bit, fix it and extract the decimal value, which is hidden inside the string.

Note: The length of the binary string is dynamic, but it’s encoding/decoding is following Hammings ‘rule’.

Note 2: Index 0 is an ‘overall’ parity bit. Watch the [Hammingcode-video from 3Blue1Brown](https://youtu.be/X8jsijhllIA?si=R7-8k3qSxQxaiAyb) for more information.

Note 3: There’s a ~55% chance for an altered Bit. So… MAYBE there is an altered Bit 😉.

Extra note for automation: return the decimal value as a string.

#### Proper 2-Colouring of a Graph

You are given data, representing a graph. Note that “graph”, as used here, refers to the field of graph theory, and has no relation to statistics or plotting.

The first element of the data represents the number of vertices in the graph. Each vertex is a unique number between 0 and ${data[0] - 1}. The next element of the data represents the edges of the graph.

Two vertices u,v in a graph are said to be adjacent if there exists an edge [u,v].

Note that an edge [u,v] is the same as an edge [v,u], as order does not matter.

You must construct a 2-coloring of the graph, meaning that you have to assign each vertex in the graph a “color”, either 0 or 1, such that no two adjacent vertices have the same color. Submit your answer in the form of an array, where element i represents the color of vertex i. If it is impossible to construct a 2-coloring of the given graph, instead submit an empty array.

Examples:

```txt
Input: [4, [[0, 2], [0, 3], [1, 2], [1, 3]]]
Output: [0, 0, 1, 1]

Input: [3, [[0, 1], [0, 2], [1, 2]]]
Output: []
```

#### Compression I: RLE Compression

Run-length encoding (RLE) is a data compression technique which encodes data as a series of runs of a repeated single character. Runs are encoded as a length, followed by the character itself. Lengths are encoded as a single ASCII digit; runs of 10 characters or more are encoded by splitting them into multiple runs.

You are given a string as input. Encode it using run-length encoding with the minimum possible output length.

Examples:

```txt
aaaaabccc -> 5a1b3c
aAaAaA -> 1a1A1a1A1a1A
111112333 -> 511233
zzzzzzzzzzzzzzzzzzz -> 9z9z1z (or 9z8z2z, etc.)
```

#### Compression II: LZ Decompression

Lempel-Ziv (LZ) compression is a data compression technique which encodes data using references to earlier parts of the data. In this variant of LZ, data is encoded in two types of chunk. Each chunk begins with a length L, encoded as a single ASCII digit from 1 - 9, followed by the chunk data, which is either:

1. Exactly L characters, which are to be copied directly into the uncompressed data. 2. A reference to an earlier part of the uncompressed data. To do this, the length is followed by a second ASCII digit X: each of the L output characters is a copy of the character X places before it in the uncompressed data.

For both chunk types, a length of 0 instead means the chunk ends immediately, and the next character is the start of a new chunk. The two chunk types alternate, starting with type 1, and the final chunk may be of either type.

You are given an LZ-encoded string. Decode it and output the original string.
Example:

```txt
decoding ‘5aaabb450723abb’ chunk-by-chunk
5aaabb -> aaabb
5aaabb45 -> aaabbaaab
5aaabb450 -> aaabbaaab
5aaabb45072 -> aaabbaaababababa
5aaabb450723abb -> aaabbaaababababaabb
```

#### Compression III: LZ Compression

For both chunk types, a length of 0 instead means the chunk ends immediately, and the next character is the start of a new chunk. The two chunk types alternate, starting with type 1, and the final chunk may be of either type.

You are given a string as input. Encode it using Lempel-Ziv encoding with the minimum possible output length.

Examples (some have other possible encodings of minimal length):

```txt
abracadabra -> 7abracad47
mississippi -> 4miss433ppi
aAAaAAaAaAA -> 3aAA53035
2718281828 -> 627182844
abcdefghijk -> 9abcdefghi02jk
aaaaaaaaaaaa -> 3aaa91
aaaaaaaaaaaaa -> 1a91031
aaaaaaaaaaaaaa -> 1a91041
```

#### ✅ Encryption I: Caesar Cipher ([Cryptography/01-Caesar_Cipher_I](/Cryptography/01-Caesar_Cipher_I/briefing.md))

Caesar cipher is one of the simplest encryption technique. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and A would become X (because of rotation).

You are given an array with two elements. The first element is the plaintext, the second element is the left shift value. Return the ciphertext as uppercase string.

Spaces remain the same.

#### Encryption II: Vigenère Cipher

Vigenère cipher is a type of polyalphabetic substitution. It uses the Vigenère square to encrypt and decrypt plaintext with a keyword.

Vigenère square:

```txt
  | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
——+————————————————————————————————————————————————————
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

For encryption each letter of the plaintext is paired with the corresponding letter of a repeating keyword. For example, the plaintext DASHBOARD is encrypted with the keyword LINUX:

```txt
Plaintext: DASHBOARD
Keyword: LINUXLINU
```

So, the first letter D is paired with the first letter of the key L. Therefore, row D and column L of the Vigenère square are used to get the first cipher letter O. This must be repeated for the whole ciphertext.

You are given an array with two elements. The first element is the plaintext, the second element is the keyword. Return the ciphertext as uppercase string.
