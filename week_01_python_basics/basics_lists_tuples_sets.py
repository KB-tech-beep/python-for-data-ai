# Basics of Lists, Tuples, and Sets in Python
# Lists, tuples, and sets are built-in data structures in Python used to store collections of items.
# Each has its own characteristics and use cases.

# ============================================================================
# Collection     |   Mutable   |   Ordered.  |   Allows Duplicates
# ============================================================================
# List           |    Yes      |     Yes     |        Yes
# Tuple          |    No       |     Yes     |        Yes
# Set            |    Yes      |     No      |        No
# ============================================================================

# ============================================================================
# INDEX - Topics Covered in This File
# ============================================================================
# 1. Creating Collections (All Types)
#    a. Creating Lists
#    b. Creating Tuples
#    c. Creating Sets

# 2. Accessing & Reading Data(Applies mainly to Lists & Tuples)
#    a. Indexing (including negative indexing)
#    b. Slicing ([:])
#    c. Checking membership (in)
#    d. Length (len)
#    e. Minimum & Maximum (min, max)
#    f. Counting items (count)
#    g. Finding position (index)
# ❗ Note: Sets do NOT support indexing or slicing.

# 3. Adding Elements (Mutability - Applies to Lists & Sets)
#    a. Add single element
#        i. List → .append()
#        ii. Set → .add()
#    b. Add multiple elements
#        i. List → .extend()
#        ii. Set → .update()
# ❗ Tuples are immutable → no adding items.

# 4. Removing Elements (Mutability - Applies to Lists & Sets)
#    a. Remove by value
#        i. List → .remove()
#        ii. Set → .remove() / .discard()
#    b. Remove by position (Lists only)
#        i. .pop()
#        ii. del
#    c. Clear entire collection (.clear() - works for all three)

# 5. Ordering & Rearranging (Mainly Lists)
#    a. Sorting (.sort(), sorted())
#    b. Reversing (.reverse())

# 6. Combining Collections (Applies to Lists & Sets)
#    a. Concatenation
#        i. List → list1 + list2 or .extend()
#        ii. Set → .union()

# 7. Set Operations (Unique to Sets)
#    a. Union
#    b. Intersection
#    c. Difference

# 8. Iteration (Loops Across Collections)
#    a. Basic for loop
#    b. enumerate()
#    c. enumerate(start=1)
#    d. zip()
#    e. zip() with different length lists

# 9. Transforming Collections (Applies mainly to Lists)
#    a. List comprehensions
#    b. Splitting strings into lists
#    c. Joining lists into strings

# 10. Empty Collections
#    a. Empty List []
#    b. Empty Tuple ()
#    c. Empty Set set() (not {}!)
# ============================================================================

# ============================================================================
# 1. CREATING COLLECTIONS (ALL TYPES)
# ============================================================================
print("\n" + "="*80)
print("1. CREATING COLLECTIONS (ALL TYPES)")
print("="*80)
# Create simple examples of list, tuple and set
general_courses_list = ['Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science']
print("String list:", general_courses_list)
general_courses_tuple = ('Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science')
print("String tuple:", general_courses_tuple)
general_courses_set = {'Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science'}
print("String set", general_courses_set)
my_num_list = [1, 2, 3, 4, 5]
print("Number list:", my_num_list)
my_num_tuple = (1, 2, 3, 4, 5)
print("Number tuple:", my_num_tuple)
my_num_set = {1, 2, 3, 4, 5}
print("Number set:", my_num_set)

# ============================================================================
# 1. Accessing & Reading Data(Applies mainly to Lists & Tuples)
# ============================================================================
print("\n" + "="*80)
print("1. Accessing & Reading Data")
print("="*80)
print("\na. Indexing(List and Tuple) - Accessing elements using index(+ and -)")
print("   Get element from list at index 0:", general_courses_list[0])                                  # Output: Math
print("   Get element from tuple at index 0:", general_courses_tuple[0])                                # Output: Math
print("   Get last element from list using -1:", general_courses_list[-1])                              # Output: Social Science
print("   Get last element from tuple using -1:", general_courses_tuple[-1])                            # Output: Social Science

print("\nb. Slicing(List and Tuple) - Accessing group of item using index range")
print("   Get first three elements from the list:", general_courses_list[:3])                           # Output: [Math, Science, English]
print("   Get third and forth element from the tuple:", general_courses_tuple[2:4])                     # Output: (English, Hindi)
print("   Get last two elements from the list:", general_courses_list[-2:])                             # Output: [Spanish, Social Science]
print("   Get last four elements from the tuple:", general_courses_tuple[3:])                           # Output: (Hindi, Physics, Spanish, Social Science)

print("\nc. Checking membership - Checking the presence of an element in collection")
print("   Is 'Spanish' part of the list?", ('Spanish' in general_courses_list))                         # Output: True
print("   Is 'French' part of the tuple?", ('French' in general_courses_tuple))                         # Output: False
print("   Is 'social science' part of the set?", ('social science'.title() in general_courses_set))     # Output: True

print("\nd. Check length of the collection")
print("   Length of the list:", len(general_courses_list))                                              # Output: 7
print("   Length of the tuple:", len(general_courses_tuple))                                            # Output: 7
print("   Length of the set:", len(general_courses_set))                                                # Output: 7

print("\ne. Minimum and Maximum from the collection")
print("   Maximum from the list:", max(general_courses_list))                                           # Output: Spanish
print("   Maximum from the tuple:", max(my_num_tuple))                                                  # Output: 5
print("   Minimum from the set:", min(general_courses_set))                                             # Output: English

print("\nf. Counting collection element(List and Tuple)")
print("   Count elements in list:", general_courses_list.count("Spanish"))                                       # Output: 1
print("   Count elements in tuple", my_num_tuple.count(4))                                                       # Output: 4


#    g. Finding position (index)