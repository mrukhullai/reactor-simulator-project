# Code ERRORs

## Recent issue

### Return Type None @ Array Conversion and Mapping

#### *Error Dialogue*

When attempting to convert split string values into a processed numeric NumPy array using `map()`, the resulting array contained only `None` elements rather than the converted numbers.
eg.

```python
import numpy as np
from Parametric_store_house import *

def arraying(t):
    l_a = []
    values = t.strip().split(" ")
    print(values)
    a = np.array(list(map(numeric_converter, values)))
    print("array",a)

Mass = "10 20 30 40 "
arraying(Mass)

```

The output is as follows :

```python
['10', '20', '30', '40']
array [None None None None]
array([None, None, None, None], dtype=object)

```

As seen, the code runs without throwing a direct syntax exception, but the output fails to return the processed values. The root cause of this error stems from the absence of explicit `return` statements within both the inner `numeric_converter` function and the outer wrapper function `arraying()`, causing Python to default to a `NoneType` return value. Additionally, Jupyter Notebook cached older module definitions, preventing updated code execution until the kernel or module was reloaded.

#### *Possible Fixes (PF)*

PF 1.
Ensure explicit `return` statements are included within the loop/try blocks and wrapper functions, and reload the external module to clear the cache. For example:

```python
def numeric_converter(t):
    counter = 0
    while True:
        try:
            s = float(t)
            s = round(s, 2)
            return s  # Explicit return on success
        except:
            print("Error\nInput not a numeric value")
            t = input("Input a numeric value\n")
            counter += 1
            if counter == 10:
                print("Errors made too many")
                break
    return None

def arraying(t):
    l_a = []
    values = t.strip().split(" ")
    print(values)
    a = np.array(list(map(numeric_converter, values)))
    print("array", a)
    return a  # Explicit return of the final array

Mass = "10 20 30 40 "
arraying(Mass)

```

This modification clears up the error and the end result of a test using the `tester.ipynb`nfie proves this

- **Note**:
When working with externel files content in a jupyter notebook please ensure to restart the kernel once any modification is made to the external file as the notebook wont recognise it otherwise.
