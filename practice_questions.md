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


<!-- formatting -->


<!-- updated examples -->

## Nested Loop — Multiplication Table

```python
for i in range(1, 6):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
    print('---')
```

Useful for practising nested iteration and formatting.
