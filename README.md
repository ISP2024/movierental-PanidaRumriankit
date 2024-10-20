## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
2.1 what refactoring signs (code smells) suggest this refactoring?
- Feature Envy

2.2 what design principle suggests this refactoring? Why?
- Single Responsibility Principle (SRP) because SRP states that a class should have only one reason to change like in the current design that we remove price_code, get_price() and get_rental_points() from Movie class.

5.2 I implement price_code_for_movie as a method in Rental class using High Cohesion. I think implement price_code_for_movie in a class that closely uses the price codes is more suitable than implement it in Movie class which might violate SRP. For implementing price_code_for_movie in PriceStrategy, I found it looks unnecessary complicated and not clean compare to when I implement it in Rental class.
