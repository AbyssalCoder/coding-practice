## File Handling in Python

```python
# Writing
with open('output.txt', 'w') as f:
    f.write('Hello, file!\n')
    f.write('Second line\n')

# Reading
with open('output.txt', 'r') as f:
    content = f.read()
    print(content)

# Reading line by line
with open('output.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

Always use `with` statements — they handle closing automatically.

## Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
```

Worst case O(n²), best case O(n) with early exit.

## Count vowels and consonants

```python
def count_vc(s):
    vowels = set('aeiouAEIOU')
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

print(count_vc('Hello World'))  # (3, 7)
```

## Fibonacci Sequence

### Iterative approach

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for i in range(10):
    print(fibonacci(i), end=' ')
# 0 1 1 2 3 5 8 13 21 34
```

**Key takeaway:** The iterative version runs in O(n) time and O(1) space.

## Fibonacci — Recursive with Memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Without memoization, the recursive version is O(2^n). With `lru_cache` it becomes O(n).

## Python Dictionary Practice

```python
# Word frequency counter
text = 'the cat sat on the mat the cat'
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# Using collections.Counter
from collections import Counter
print(Counter(text.split()))
```


<!-- updated examples -->

## Linear Search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

nums = [4, 2, 7, 1, 9]
print(linear_search(nums, 7))  # 2
print(linear_search(nums, 5))  # -1
```

Time complexity: O(n). Works on unsorted arrays.


<!-- updated examples -->
