import textwrap

def print_description(header: str, description: str) -> None:
    """
    Print a formatted description with a header.
    """
    
    dedented_description = textwrap.dedent(description).strip()
    print("----------------------------------------------------------------")
    print(header)
    print("----------------------------------------------------------------")
    # for line in dedented_description.splitlines():
    #     print(textwrap.fill(line, width=80))
    for line in description.splitlines():
        print(line.strip())
    print("")

print_description("Numeric types",
    '''
    * int: Positive or negative whole numbers 
    * float: Real numbers with a decimal point 
    * complex: Real and imaginary numbers (out of scope for this course)
    '''
)
i: int = 10
f: float = 3.14
print("Numeric values:")
print(f"* Integer: {i}\n* Float: {f}")

print_description("Boolean type", 
                  "Represents truth values, which can be either True or False.")
t1: bool = True
f1: bool = False
t2: bool = True
print(f"Boolean values:\nt1={t1}\nf1={f1}\nt2={t2}\n")
print(
    '''
    Boolean operators:
    t1 AND f1: {}
    t1 OR f1: {}
    t1 NOR f1: {}
    t1 XOR t2: {}
    '''.format(t1 and f1, t1 or f1, not (t1 and f1), t1 ^ t2)
)
t2: bool = True

print_description("Set type",
    '''
    An unordered collection of unique elements. Sets are mutable,
    meaning you can add or remove elements after creation. In Python, sets
    are defined using curly braces {} or the  set() constructor."
    '''
)
set1: set[str] = {"apple", "banana", "orange"}
set1.add("kiwi")  # Add a new element to the set
set1.update({"melon", "orange"})  # Add multiple elements to the set
set1.remove("banana")  # Remove an element from the set (raises KeyError if it doesn't exist)
set1.discard("banana")  # Remove an element from the set (no error if it doesn't exist)
print(f"Set: {set1}")

print_description("List type",
    '''  
    An ordered collection of elements that can contain duplicates.
    Lists are mutable, meaning you can change their contents after creation
    '''
)
list1: list[str] = ["apple", "banana", "orange"]
list1.append("kiwi")  # Add a new element to the end of the list
list1.extend(["melon", "orange"])
list1.insert(0, "grape")
print(f"List: {list1}")


print_description("Tuple type",
    '''
    An ordered collection of elements that can contain duplicates.
    Tuples are immutable, meaning you cannot change their contents after creation
    '''
)
tuple1: tuple = ("apple",)
# This will create a new tuple and reassign the variable tuple1 to it
tuple1 = ("banana", 2, "orange", 3,) 
print(f"Tuple: {tuple1}")


print_description("Dictionary type",
    '''
    A collection of key-value pairs, where each 
    key is unique and maps to a value. Dictionaries are mutable,
    meaning you can change their contents after creation. Note: Other
    programming languages may refer to this data structure as a
    hashmap or associative array. In Python, dictionaries
    are defined using curly braces {} and key-value pairs are
    separated by colons (:)
    '''
)
dict1: dict[str, int] = {
    "apple": 1, 
    "banana": 2,
}

# Add a new key-value pair to the dictionary
dict1["orange"] = 3

# Add multiple key-value pairs to the dictionary using the update() method
dict1.update({"apple": 4, "kiwi": 5})  

# Only add if melon doesn't already exist
dict1.setdefault("melon", 6) 
dict1.setdefault("melon", 7) # This will not update the value for "melon" since it already exists
print(f"Dictionary: {dict1}\n")
    