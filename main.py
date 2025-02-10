import numpy as np
from scipy.optimize import brentq

# Define the functions:
func1 = lambda x: x**10      # Represents x raised to the 10th power
func2 = lambda x: np.exp(x)   # Represents exp(x), i.e., e^x

class IntersectionFinder:
    """
    A class to find the intersection points of two mathematical functions.
    """

    def __init__(self, func1, func2):
        """
        Initialize the class with two functions.
        :param func1: The first function (callable).
        :param func2: The second function (callable).
        """
        self.func1 = func1
        self.func2 = func2

    def _equation(self, x):
        """
        Defines the equation for the difference between the two functions.
        The intersection occurs where f(x) = func1(x) - func2(x) = 0.
        :param x: The input value.
        :return: The difference between func1(x) and func2(x).
        """
        try:
            return self.func1(x) - self.func2(x)
        except Exception as e:
            raise ValueError(f"Error evaluating the functions at x={x}: {e}")

    def find_intersections_by_scan(self, domain, num_points, tol=1e-6):
        """
        Automatically finds intersections by scanning the specified domain.
        :param domain: A tuple (xmin, xmax) specifying the domain to search.
        :param num_points: Number of points to sample in the domain.
        :param tol: Tolerance for checking convergence and uniqueness.
        :return: A list of tuples (x, y) representing the intersection points.
        """
        xmin, xmax = domain
        x_grid = np.linspace(xmin, xmax, num_points)
        f_values = []

        # Evaluate f(x) on the grid
        for x in x_grid:
            try:
                f_val = self._equation(x)
            except Exception:
                f_val = np.nan
            f_values.append(f_val)
        f_values = np.array(f_values)

        intersections = []
        # Look for sign changes in f(x)
        for i in range(len(x_grid) - 1):
            if np.isnan(f_values[i]) or np.isnan(f_values[i+1]):
                continue
            if f_values[i] == 0:
                x_root = x_grid[i]
            elif f_values[i] * f_values[i+1] < 0:
                try:
                    x_root = brentq(self._equation, x_grid[i], x_grid[i+1], xtol=tol)
                except Exception:
                    continue
            else:
                continue

            # Ensure uniqueness of the intersection point.
            if not any(abs(x_root - existing_x) < tol for existing_x, _ in intersections):
                y_root = self.func1(x_root)  # At an intersection, func1(x) equals func2(x)
                intersections.append((x_root, y_root))
        return intersections

def main():
    # Updated header message to match the defined functions.
    print("Finding intersections between f(x) = x^10 and g(x) = exp(x)...\n")
    
    # Create an instance of IntersectionFinder using the defined functions.
    finder = IntersectionFinder(func1, func2)
    
    # Prompt the user for the domain.
    while True:
        domain_input = input("Enter the domain as two numbers separated by a comma (e.g., 0, 100): ").strip()
        try:
            parts = domain_input.split(',')
            if len(parts) != 2:
                raise ValueError("Please enter exactly two numbers separated by a comma.")
            xmin = float(parts[0].strip())
            xmax = float(parts[1].strip())
            if xmin >= xmax:
                raise ValueError("The first number must be less than the second number.")
            domain = (xmin, xmax)
            break
        except Exception as e:
            print(f"Invalid input: {e}. Please try again.\n")
    
    # Set a default number of points and allow the user to change it.
    default_points = 1000
    print(f"\nThe domain is set to {domain[0]} to {domain[1]} with a default of {default_points} points.")
    change_points = input("Would you like to change the number of points? (y/n): ").strip().lower()
    if change_points == 'y':
        while True:
            points_input = input("Enter the desired number of points (e.g., 2000): ").strip()
            try:
                num_points = int(points_input)
                if num_points < 2:
                    raise ValueError("Number of points must be at least 2.")
                break
            except Exception as e:
                print(f"Invalid input: {e}. Please try again.\n")
    else:
        num_points = default_points

    # Find and display the intersection points.
    intersections = finder.find_intersections_by_scan(domain, num_points)
    print("\nResults:")
    if intersections:
        print("Intersection points (rounded to one decimal place):")
        for x, y in intersections:
            print(f"x: {x:.1f}, y: {y:.1f}")
    else:
        print("No intersections found.")

if __name__ == "__main__":
    main()
