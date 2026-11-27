#!/bin/python3

# You are given a function f(X) = X^2. You are also given K lists. The i-th list consists of N_i elements.
# You have to pick one element from each list so that the value from the equation below is maximized:
#
#   S = (f(X_1) + f(X_2) + ... + f(X_k)) % M
#
# X_i denotes the element picked from the i-th list. Find the maximized value S_max obtained.
# % denotes the modulo operator.
#
# Note that you need to take exactly one element from each list, not necessarily the largest element.
# You add the squares of the chosen elements and perform the modulo operation. The maximum value that you
# can obtain, will be the answer to the problem.
#
# Input Format
#   The first line contains 2 space separated integers K and M.
#   The next K lines each contains an integer N_i, denoting the number of elements in the i-th list,
#   followed by N_i space separated integers denoting the elements in the list.
#
# Constraints
#   - 1 <= K <= 7
#   - 1 <= M <= 1000
#   - 1 <= N_i <= 7
#   - 1 <= Magnitude of elements in list <= 10^9
#
# Output Format
#   Output a single integer denoting the value S_max.
#
# Sample Input
#   3 1000
#   2 5 4
#   3 7 8 9
#   5 5 7 8 9 10
#
# Sample Output
#   206

# python3 maximize_it.py

def max_modulo_square_sum(lists: list[list[int]], m: int) -> int:

    # Start with remainder 0 before picking from any list
    reachable = {0}

    for values in lists:
        # Only unique (x * x) % m values matter for transitions
        mod_squares = {(x * x) % m for x in values}

        # Advance reachable remainders mod m by one list:
        #   Each old remainder `rem` combined with each new square `sq` produces
        #   a new remainder `(rem + sq) % m`. Using a fresh `next_reachable` set
        #   prevents reusing a remainder added during this same list step (so we
        #   pick at most one element per list) and deduplicates identical remainders
        #
        # Example (m = 10, 
        #          List 1 = [5, 4] -> mod_squares = {5, 6},
        #          List 2 = [7, 8] -> mod_squares = {4, 9}):
        #   Start:   reachable = {0}
        #   List 1:  (0 + 5) % 10 = 5, (0 + 6) % 10 = 6 -> reachable = {5, 6}
        #   List 2:  from 5 -> 9, 4; from 6 -> 0, 5     -> reachable = {9, 4, 0, 5}
        
        next_reachable = set()
        for rem in reachable:
            for sq in mod_squares:
                next_reachable.add((rem + sq) % m)

        reachable = next_reachable

    return max(reachable)

if __name__ == "__main__":
    k, m = map(int, input().split())
    lists = []
    
    for _ in range(k):
        parts = list(map(int, input().split()))
        lists.append(parts[1:])

    print(max_modulo_square_sum(lists, m))
