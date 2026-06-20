# Pattern Printing in Python

## Introduction

Pattern printing Python mein Loops aur Nested Loops ko samajhne ka best way hai.

Patterns solve karne se:

* Loop concepts strong hote hain.
* Nested loops samajh aate hain.
* Logic building improve hoti hai.
* Problem-solving skills better hoti hain.

---

# 1. Square Pattern

## Pattern

```text
*****
*****
*****
*****
*****
```

## Working

* Rows fixed hain.
* Columns bhi fixed hain.
* Har row mein same number of stars print hote hain.

## Logic

```python
for row in range(5):
    for column in range(5):
```

Outer loop rows control karta hai.

Inner loop columns control karta hai.

---

# 2. Right Triangle Pattern

## Pattern

```text
*
**
***
****
*****
```

## Working

* Har new row mein stars ki quantity increase hoti hai.
* Row number aur stars ki quantity same hoti hai.

## Logic

```python
for row in range(1, 6):
```

Row 1 → 1 star

Row 2 → 2 stars

Row 3 → 3 stars

---

# 3. Inverted Triangle Pattern

## Pattern

```text
*****
****
***
**
*
```

## Working

* Har new row mein stars decrease hote hain.
* Pehli row mein maximum stars hote hain.

## Logic

```python
for row in range(5, 0, -1):
```

Row 5 → 5 stars

Row 4 → 4 stars

Row 3 → 3 stars

---

# 4. Number Triangle Pattern

## Pattern

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

## Working

* Har row mein row number print hota hai.
* Row number jitni baar repeat hota hai.

## Logic

```python
print(row)
```

Agar row = 3 hai to 3 teen baar print hoga.

---

# 5. Increasing Number Triangle

## Pattern

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

## Working

* Har row 1 se start hoti hai.
* Numbers gradually increase karte hain.

## Logic

```python
for column in range(1, row + 1):
```

Har row previous row se ek number zyada print karti hai.

---

# 6. Alphabet Pattern

## Pattern

```text
A
A B
A B C
A B C D
A B C D E
```

## Working

* Numbers ki jagah alphabets print hote hain.
* ASCII values ko characters mein convert kiya jata hai.

## Logic

```python
chr()
```

Examples:

```python
chr(65)  # A
chr(66)  # B
chr(67)  # C
```

---

# 7. Pyramid Pattern

## Pattern

```text
    *
   ***
  *****
 *******
*********
```

## Working

Pyramid do cheezon se banta hai:

1. Spaces
2. Stars

Har row mein:

* Spaces decrease hote hain.
* Stars increase hote hain.

## Formula

```python
spaces = rows - row - 1
stars = (2 * row) + 1
```

Example:

```text
Row 0 → 4 spaces, 1 star
Row 1 → 3 spaces, 3 stars
Row 2 → 2 spaces, 5 stars
```

---

# 8. Reverse Pyramid Pattern

## Pattern

```text
*********
 *******
  *****
   ***
    *
```

## Working

Ye Pyramid ka ulta version hai.

Har row mein:

* Spaces increase hote hain.
* Stars decrease hote hain.

## Formula

```python
spaces = row
stars = (2 * (rows - row)) - 1
```

---

# 9. Diamond Pattern

## Pattern

```text
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

## Simplest Logic

Diamond ko yaad karne ka easiest rule:

```text
Diamond
=
Pyramid
+
Reverse Pyramid
```

Bas pehle Pyramid print karo.

Phir uske niche Reverse Pyramid print karo.

---

## Diamond Working

### Upper Part

```text
    *
   ***
  *****
 *******
*********
```

Yeh Pyramid hai.

---

### Lower Part

```text
 *******
  *****
   ***
    *
```

Yeh Reverse Pyramid hai.

---

## Formula

### Upper Pyramid

```python
spaces = rows - row - 1
stars = (2 * row) + 1
```

### Lower Pyramid

```python
spaces = rows - row - 1
stars = (2 * row) + 1
```

Sirf loop reverse direction mein chalta hai.

---

# Golden Rule

```text
Square      → Fixed Rows + Fixed Columns

Triangle    → Stars Increase

Inverted    → Stars Decrease

Pyramid     → Spaces Decrease + Stars Increase

Reverse     → Spaces Increase + Stars Decrease

Diamond     → Pyramid + Reverse Pyramid
```

## Summary

Pattern printing ka core concept:

1. Outer Loop → Rows
2. Inner Loop → Columns
3. Spaces Pattern ko shape deti hain.
4. Stars ya Numbers actual pattern banate hain.

Agar aap Square, Triangle aur Pyramid samajh gaye, to baaki almost saare patterns aasani se bana sakte hain.