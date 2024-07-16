# Functions and control flow

## Objectives

* To use `if` statements to write branching logic
* To appropriately use `for-of` or `while` loops to perform computations on arrays of values
* To design solutions to complex problems using the constructs above
* To implement those solutions in functions
* To critically examine inequities in access to K-12 CS Education in the state of California

## Overview

We've learned a number of Python programming constructs this quarter.
* Statements and expressions
* Data types and variables
* `if`, `else`, and `else-if` statements
* Functions

In this lab, we're going to put these constructs together to create solutions to increasingly complex problems. Like the previous lab, we'll study data about enrollments in CS classes in California schools.

## Instructions

Read these questions and hints carefully. You will use your knowledge of array operations to successfully complete these tasks. Please use the section on **Useful functions** at the end of this page as a reference to aid you.

### Part 1

In `index.py`, you've been given the same data-set as you had in Lab 3. That is, you have:
* `CALIFORNIA_COUNTIES`, an array of `string`s representing names of counties in California.
* `PERCENT_SCHOOLS_OFFERING_CS`, an array of `number`s representing the percentages of schools in a given county that offer any CS courses.

The two arrays are ordered "in parallel", i.e., `"Contra Costa"` county is the sixth county in the `CALIFORNIA_COUNTIES` array, and roughly 52% of its schools offer CS courses, since `0.524590` is the sixth number in the `PERCENT_SCHOOLS_OFFERING_CS` array.

**Take care not to re-order these arrays!**

**Core task:** Write _functions_ that answer the following questions. Each function should take two input parameters: one for the array of counties, and one for the array of percentages.

1. **What are the 5 counties with the _highest_ percentages of schools offering CS courses?**

Name your function `counties_with_most_cs`, and give it the following parameters (in order): `counties`, `percentages`.

Test your code using print statements.

2. **What are the 5 counties with the _lowest_ percentages of schools offering CS courses?**

Name your function `counties_with_least_cs`, and give it the following parameters (in order): `counties`, `percentages`.

Remember to be mindful of the types of each parameter. Notice that these two questions are not asking for a single county or percentage as a result, but rather _five_ county names. What data type can hold five names?

#### Implementation hints 
As always, first come up with a plan to solve the problem. Consider question 1 first.

In the previous lab, you used `max()` to find the highest percentage, and then used `index()` to match that value with a particular county. We need to do something similar this time, except we need to find the _top 5_ or _bottom 5_ values.

Here are some hints:
* We can still use `max()` and `min()` to solve these problems. We just need to ensure that each subsequent call to `max()` or `min()` returns the _next highest_ or _next lowest_ value from the original list.
* The first time we call `max()`, we want to obtain the highest percentage of schools offering CS. The next time we call `max()`, we want to obtain the second-highest percentage of schools offering CS, and so on. We want to do this a total of 5 times (for the top 5 or bottom 5 counties). Remember `while` loops?
* See the descriptions of `index()` and `pop()` in the **Useful functions** section below. Can you think of ways to use those two functions together to your goal?

(Note that if you modify the original arrays while solving the problem, you'll want to work with _copies_ of the original arrays. See the `.copy()` function below.)

### Part 2

3. We would like to know about counties that should receive the most resources for increasing their CS offerings. **Write a function that returns a list of names of counties that have a lower percentage of CS-offering schools than the California average.**

Name your function `lower_than_avg_cs_counties`. Like the others, it should take two arrays as parameters: one for `counties` and one for `percentages`. Like the others, it should _not_ modify those arrays!

Take some time to think about what this question is asking. What are the sub-goals involved in approaching this problem? If the sub-goals are reasonably complicated, it may make sense to abstract them out into their own functions, which can be called in your `lower_than_avg_cs_counties` function.

**Write out your sub-goals as `# comments` in plain English before implementing the function.**

## Useful functions

Consider the following useful operations you can perform on an array:

**`index()`**

The `index()` function can be used to find the position of a particular item in an array. It takes one parameter:
* `element`, the item to search for

There are other optional parameters which we won't be using.

_Example_:

Suppose you've created an array like so: `fruit[] = ["apple", "banana", "orange"]`. The function call `fruit.index("banana")` will return the value `1`, because `"banana"` is an position `1` in the array.

**`pop()`**

The `pop()` function can be used to remove items at a given position in an array. It takes one optional parameter:
* a `position` value that indicates the index corresponding to the value that will be removed.

If no position is inputted, pop() will remove the last value in the array.

_Example_: 

Suppose you've created an array like so: `fruit[] = ["apple", "banana", "orange"]` You can remove `"banana"` from the array by doing `fruit.pop(1)`.

**Note that this function modifies the array!**

**`.copy()`**

The `.copy()` function returns a copy of an array. It takes no parameters.

_Example_:

Suppose you've created an array like so: `fruit[] = ["apple", "banana", "orange", "peach", "avocado"]`. The function call `fruit.copy()` will return a copy of the array `["apple", "banana", "orange", "peach", "avocado"]`. 

We can assign this copy to another array: `fruit_copy[] = fruit.copy()`. Any changes made to this copy will not affect the original `fruit` array.
