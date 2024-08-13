# Number and formating
```python
a = (-3) // 2
b = int((-3) / 2)
print(a, b)
```
a prints -2, while b prints -1. 
- Because `\\` is a floor division, it divides the number and then floors the result to the nearest integer** less than or equal to **the result.
- The int() function, on the other hand, simply **truncates the decimal part** of a floating-point number, effectively rounding towards zero.