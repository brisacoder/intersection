# Intersection Finder

This Python program finds the intersection points between two mathematical functions. It uses numerical methods to solve for intersections and is designed to handle any pair of functions defined by the user.

## Features

- Finds intersection points between two functions.
- Handles invalid guesses gracefully with proper error messages.
- Fully encapsulated and reusable code.
- Designed with PEP8 compliance and robust documentation.

## Installation

1. **Install Dependencies**:  
   Ensure `numpy` and `scipy` are installed. You can install them via pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Define Your Functions

The program is designed so that you can easily change the functions it uses for intersection calculation. To do this, simply modify the lambda functions in the code. For example, the default definitions might look like this:

```python
# Define the functions:
func1 = lambda x: x**10      # Represents x raised to the 10th power
func2 = lambda x: 3**x       # Represents 3 raised to the power x
```

You can replace these functions with any mathematical expressions you need. Here are several examples to help you get started:

- **Exponential Function (e<sup>x</sup>)**:  
  To represent the exponential function \( e^x \), use NumPy’s `exp` function:
  ```python
  import numpy as np

  func1 = lambda x: np.exp(x)  # Represents e^x
  ```

- **Natural Logarithm (ln(x))**:  
  To represent the natural logarithm, use NumPy’s `log` function:
  ```python
  import numpy as np

  func1 = lambda x: np.log(x)  # Represents ln(x)
  ```
  *Note: The input `x` must be positive.*

- **Logarithm Base 10**:  
  To represent log base 10, use NumPy’s `log10` function:
  ```python
  import numpy as np

  func1 = lambda x: np.log10(x)  # Represents log10(x)
  ```
  *Note: The input `x` must be positive.*

- **Trigonometric Functions**:  
  For sine, cosine, etc., use NumPy’s corresponding functions:
  ```python
  import numpy as np

  func1 = lambda x: np.sin(x)  # Represents sin(x)
  func2 = lambda x: np.cos(x)  # Represents cos(x)
  ```

- **Custom Combination**:  
  You can combine operations as needed. For example:
  ```python
  import numpy as np

  func1 = lambda x: x**2 + np.sin(x)  # Represents x^2 + sin(x)
  func2 = lambda x: np.exp(x)         # Represents e^x
  ```

### 2. Run the Program

After updating the functions as desired, run the program with:

```bash
python intersection_finder.py
```

The program will prompt you to enter a domain (for example, `0, 100`) and will then display a default number of points to scan. You will have the option to change this value if needed.

### How It Works

The program scans a user-defined domain for sign changes in the difference between the two functions. When a sign change is found, it brackets the interval and uses Brent’s method (via `scipy.optimize.brentq`) to accurately locate the intersection point.

## Example

Suppose you want to find the intersection between the functions \( f(x) = x^{10} \) and \( g(x) = 3^x \). The code already contains:

```python
func1 = lambda x: x**10      # x raised to the 10th power
func2 = lambda x: 3**x       # 3 raised to the power x
```

Simply run the program, input your desired domain (e.g., `0, 100`), and the program will calculate and display the intersection points.

## Customization

Feel free to modify the functions according to your needs by updating the lambda functions in the code. With the provided examples, you can easily type in exponentials, logarithms, trigonometric functions, or any other mathematical expressions.

---

Happy computing!
