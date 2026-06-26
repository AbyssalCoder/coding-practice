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
