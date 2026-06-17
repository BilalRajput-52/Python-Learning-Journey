# Modules in Python

A module is a Python file that contains functions, variables, and classes which can be reused in other Python programs.

Modules help organize code, improve readability, and promote code reusability.

## Types of Modules in Python

There are two main types of modules in Python:

### 1. Built-in Modules

Built-in modules are pre-installed with Python. You can use them directly by importing them into your program.

**Example:**

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Output:

```text
5.0
3.141592653589793
```

### 2. External Modules

External modules are not included with Python by default. They must be installed using `pip` before they can be used.

**Example:**

```bash
pip install requests
```

```python
import requests

response = requests.get("https://www.google.com")
print(response.status_code)
```

## Import Specific Function

Instead of importing the entire module, you can import only the required function.

```python
from math import sqrt

print(sqrt(49))
```

Output:

```text
7.0
```

## Benefits of Modules

* Code Reusability
* Better Organization
* Easier Maintenance
* Reduced Development Time
* Simplifies Large Projects
* Encourages Modular Programming
