from collections import Counter, OrderedDict, defaultdict, namedtuple
from itertools import permutations, product


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
    perms_2 = list(permutations(["a", "b", "c"], 2))
    print("2-permutations of ['a', 'b', 'c']:", perms_2)

    # All full-length permutations (r defaults to len(iterable)) -> 3! = 6
    perms_all = ["".join(p) for p in permutations("abc")]
    print("All permutations of 'abc':", perms_all)


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

if __name__ == "__main__":
    demo_itertools_product()
    demo_itertools_permutations()
    demo_counter()
    demo_set()
    demo_defaultdict()
    demo_namedtuple()
    demo_ordereddict()
