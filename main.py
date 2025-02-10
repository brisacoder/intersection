import numpy as np
from scipy.optimize import fsolve

class IntersectionFinder:
    """
    A class to find the intersection points of two mathematical functions.
    """

    def __init__(self, func1, func2):
        """
        Initialize the class with two functions.

        :param func1: The first function, defined as a callable (e.g., lambda or function).
        :param func2: The second function, defined as a callable.
        """
        self.func1 = func1
        self.func2 = func2

    def _equation(self, x):
        """
        Define the equation for the difference between the two functions.
        The intersection occurs where func1(x) = func2(x), i.e., func1(x) - func2(x) = 0.

        :param x: The input value for the equation.
        :return: The difference between func1(x) and func2(x).
        """
        try:
            return self.func1(x) - self.func2(x)
        except Exception as e:
            raise ValueError(f"Error evaluating the functions: {e}")

    def find_intersections(self, initial_guesses, tol=1e-6):
        """
        Find all intersection points using a list of initial guesses.

        :param initial_guesses: A list of initial guesses for the solver.
        :param tol: The tolerance for checking if intersections are valid.
        :return: A list of tuples containing the x and y coordinates of intersection points.
        """
        intersections = []
        for guess in initial_guesses:
            try:
                # Solve for x where func1(x) = func2(x)
                x_intersection = fsolve(self._equation, guess, xtol=tol)[0]

                # Verify the solution by recalculating the difference
                if abs(self.func1(x_intersection) - self.func2(x_intersection)) < tol:
                    y_intersection = self.func1(x_intersection)  # Same as func2(x_intersection)

                    # Check if this intersection is already in the list (within tolerance)
                    if not any(abs(x - x_intersection) < tol for x, _ in intersections):
                        intersections.append((x_intersection, y_intersection))
            except Exception as e:
                print(f"Failed to find intersection near guess {guess}: {e}")
        return intersections


def main():
    """
    Main function to demonstrate the IntersectionFinder class.
    """
    print("Finding intersections between f(x) = x^3 and g(x) = 3^x...\n")

    # Define the two functions
    func1 = lambda x: x**3
    func2 = lambda x: 3**x

    # Create an instance of IntersectionFinder
    finder = IntersectionFinder(func1, func2)

    # Define a range of initial guesses
    initial_guesses = [2, 2.5, 3, 4, 5]  # Refined guesses based on graph behavior

    # Find the intersection points
    intersections = finder.find_intersections(initial_guesses)

    # Display the results
    if intersections:
        print("Intersection points (rounded to one decimal place):")
        for point in intersections:
            x, y = point
            print(f"x: {x:.1f}, y: {y:.1f}")
    else:
        print("No intersections found.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
