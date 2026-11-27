from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from itertools import combinations, combinations_with_replacement, groupby, permutations, product

def demo_itertools_product() -> None:
    """Cartesian product (order matters, replacement allowed across iterables or repeat)."""
    print("=== itertools.product ===")

    # Cartesian product of two iterables: (x, y) for x in [0, 1] and y in ['a', 'b']
    pairs = list(product([0, 1], ["a", "b"]))
    print("Product ([0, 1], ['a', 'b']):", pairs)

    # All 2-character combinations with replacement from 'AB' (equivalent to repeat=2)
    two_letter_codes = ["".join(chars) for chars in product("AB", repeat=2)]
    print("Length-2 products of 'AB':", two_letter_codes)

def demo_itertools_permutations() -> None:
    """Ordered arrangements of length r without repeating the same index/element slot."""
    print("\n=== itertools.permutations ===")

    # All 2-element ordered permutations of ['a', 'b', 'c'] -> 3! / (3-2)! = 6
    perms_2 = list(permutations(["a", "b", 'c'], 2))
    print("2-permutations of ['a', 'b', 'c']:", perms_2)

    # All full-length permutations (r defaults to len(iterable)) -> 3! = 6
    perms_all = ["".join(p) for p in permutations("abc")]
    print("All permutations of 'abc':", perms_all)

def demo_itertools_combinations() -> None:
    """Order-preserving r-element subsequences chosen by index without replacement."""
    print("\n=== itertools.combinations ===")

    # All 2-element combinations of 'ABCD' -> 4! / (2! * 2!) = 6
    combs_2 = ["".join(c) for c in combinations("ABCD", 2)]
    print("2-combinations of 'ABCD':", combs_2)
    
    combs_r_2 = ["".join(c) for c in combinations_with_replacement("ABCD", 2)]
    print("2-combinations with replacement of 'ABCD':", combs_r_2)

    # Duplicate values yield distinct index-based combinations that may look identical
    dup_combs = list(combinations([1, 1, 3, 3, 3], 4))
    print("4-combinations of [1, 1, 3, 3, 3] (count =", len(dup_combs), "):", dup_combs)

def demo_groupby() -> None:
    """Group consecutive elements sharing a key (sort first to merge non-adjacent keys)."""
    print("\n=== itertools.groupby ===")

    # Consecutive runs only: 'A' appears in two separate runs separated by 'B' and 'C'
    consecutive_runs = [(key, list(group)) for key, group in groupby("AAABBCAA")]
    print("Consecutive runs in 'AAABBCAA':", consecutive_runs)

    # Run-length encoding pattern (e.g., HackerRank 'Compress the String!')
    digits = "1222311"
    encoded = [(len(list(group)), int(digit)) for digit, group in groupby(digits)]
    print("Run-length encoded '1222311':", encoded)

    # Sort by key first when grouping non-adjacent items by a shared attribute/key
    words = ["banana", "apple", "apricot", "blueberry", "cherry"]
    sorted_words = sorted(words, key=lambda w: w[0])
    by_initial = {
        initial: list(group)
        for initial, group in groupby(sorted_words, key=lambda w: w[0])
    }
    print("Grouped by initial letter after sorting:", by_initial)

def demo_counter() -> None:
    """Frequency counting with dictionary-like access and useful helper methods."""
    print("\n=== collections.Counter ===")

    text = "banana"
    counts = Counter(text)
    print("Counts for 'banana':", dict(counts))
    print("Most common 2:", counts.most_common(2))
    print("Missing key defaults to 0 (no KeyError):", counts["z"])

    # Multiset arithmetic: subtract occurrences
    needed = Counter("aab")
    remaining = counts - needed
    print("Remaining after subtracting 'aab':", dict(remaining))

def demo_set() -> None:
    """Unordered unique elements with O(1) average lookup and set algebra."""
    print("\n=== set ===")

    vowels = {"a", "e", "i", "o", "u"}
    letters_in_word = set("banana")
    print("Unique letters in 'banana':", sorted(letters_in_word))
    print("Is 'a' in vowels?:", "a" in vowels)

    # Set operations
    print("Vowels in 'banana' (intersection):", sorted(vowels & letters_in_word))
    print("Consonants in 'banana' (difference):", sorted(letters_in_word - vowels))

    letters_in_word.add("v")
    letters_in_word.update([1, 2, 3, 4])
    letters_in_word.discard(1)  # If element 1 does not exist, it does not raise a KeyError
    letters_in_word.remove(3)   # If element 3 does not exist, it raises a KeyError
    letters_in_word.pop()       # Remove and return an arbitrary element from the set

    vowels.union(letters_in_word)
    vowels.intersection(letters_in_word)
    vowels.difference(letters_in_word)  # use ^ or symmetric_difference for symmetric difference

def demo_defaultdict() -> None:
    """Dictionary that automatically initializes missing keys via a factory function."""
    print("\n=== collections.defaultdict ===")

    # Group indices by character (similar to index lookups)
    indices_by_char = defaultdict(list)
    for idx, ch in enumerate("aabab"):
        indices_by_char[ch].append(idx)
    print("Indices grouped by char in 'aabab':", dict(indices_by_char))

    # Count occurrences using int (default factory returns 0)
    freq = defaultdict(int)
    for ch in "mississippi":
        freq[ch] += 1
    print("Char counts using defaultdict(int):", dict(freq))

def demo_namedtuple() -> None:
    """Tuple subclass with named fields for readable, immutable records."""
    print("\n=== collections.namedtuple ===")

    Point = namedtuple("Point", ["x", "y"])
    p1 = Point(3, 4)
    p2 = Point._make([7, 1])

    print("Point p1:", p1, f"(x={p1.x}, y={p1.y})")
    print("Point p2 from iterable:", p2)
    print("Unpacked coordinates:", *p1)

def demo_ordereddict() -> None:
    """Dictionary subclass with explicit order-repositioning methods like move_to_end."""
    print("\n=== collections.OrderedDict ===")

    od = OrderedDict([("first", 1), ("second", 2), ("third", 3)])
    od["fourth"] = 4

    # Move an existing key to the end (or beginning with last=False)
    od.move_to_end("first")
    print("After move_to_end('first'):", list(od.items()))

    od.move_to_end("fourth", last=False)
    print("After move_to_end('fourth', last=False):", list(od.items()))

    # Pop from either end: last=True (LIFO) or last=False (FIFO)
    popped_oldest = od.popitem(last=False)
    print("Popped oldest item:", popped_oldest, "-> remaining:", list(od.items()))

def demo_deque() -> None:
    """Double-ended queue with O(1) appends and pops from both ends, rotation, and maxlen."""
    print("\n=== collections.deque ===")

    dq = deque(["b", "c"])
    dq.append("d")      # Right end: deque(['b', 'c', 'd'])
    dq.appendleft("a")  # Left end:  deque(['a', 'b', 'c', 'd'])
    print("After append and appendleft:", list(dq))

    popped_right = dq.pop()      # Removes 'd' from right
    popped_left = dq.popleft()   # Removes 'a' from left
    print("Popped right/left:", popped_right, popped_left, "-> remaining:", list(dq))

    # Positive rotates right (toward end); negative rotates left (toward front)
    dq.rotate(1)
    print("After rotate(1):", list(dq))
    dq.rotate(-1)
    print("After rotate(-1):", list(dq))

    # Bounded deque automatically evicts from the opposite end when full
    window = deque(maxlen=3)
    for num in [10, 20, 30, 40]:
        window.append(num)
    print("Sliding window (maxlen=3) after [10, 20, 30, 40]:", list(window))

if __name__ == "__main__":
    demo_itertools_product()
    demo_itertools_permutations()
    demo_itertools_combinations()
    demo_groupby()
    demo_counter()
    demo_set()
    demo_defaultdict()
    demo_namedtuple()
    demo_ordereddict()
    demo_deque()
