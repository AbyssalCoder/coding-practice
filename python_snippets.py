## Palindrome — Two-pointer Approach

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

Runs in O(n/2) comparisons with O(1) extra space.

## Armstrong Number

An Armstrong number is a number that equals the sum of its digits each raised to the power of the number of digits.

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

# Examples: 153 = 1^3 + 5^3 + 3^3
print(is_armstrong(153))  # True
print(is_armstrong(370))  # True
```


<!-- indent fix -->

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

## Binary Search

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

sorted_arr = [1, 3, 5, 7, 9, 11]
print(binary_search(sorted_arr, 7))  # 3
```

Requires sorted input. Time complexity: O(log n).

## Binary Search

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

sorted_arr = [1, 3, 5, 7, 9, 11]
print(binary_search(sorted_arr, 7))  # 3
```

Requires sorted input. Time complexity: O(log n).

## Array Traversal Patterns

```python
arr = [10, 20, 30, 40, 50]

# Forward
for val in arr:
    print(val)

# With index
for i, val in enumerate(arr):
    print(f'Index {i}: {val}')

# Reverse
for val in reversed(arr):
    print(val)
```

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
