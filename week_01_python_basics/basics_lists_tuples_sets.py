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
# WHY SOME OPERATIONS WORK FOR ALL TYPES & OTHERS DON'T?
# ============================================================================
# The difference lies in Python's DATA MODEL and which SPECIAL METHODS each class implements.
#
# OPERATIONS REQUIRING __getitem__() METHOD (Sequence Protocol):
#    • Indexing [0], Slicing [1:3], Finding position .index()
#    • Lists and Tuples implement __getitem__() → enables indexed access
#    • Sets do NOT implement __getitem__() → no indexed access
#    • Why? Because __getitem__() requires POSITIONAL/ORDERED access, and Sets are UNORDERED
#
# OPERATIONS WORKING FOR ALL THREE (Iterable Protocol):
#    • Membership 'in', Length len(), Min/Max, Count .count(), Sum sum()
#    • All three implement __iter__() and/or __contains__() → enables iteration
#    • These don't depend on POSITION or ORDER
#
# PYTHON'S CLASS STRUCTURE:
#    • List & Tuple: Implement SEQUENCE PROTOCOL (__getitem__, __len__, __iter__)
#    • Set: Implements only SET PROTOCOL (__iter__, __contains__)
#
# PRACTICAL EXAMPLE:
#    • my_set[0] → ERROR (TypeError: 'set' object is not subscriptable)
#    • my_list[0] → WORKS (has __getitem__ method)
#    • 'element' in my_set → WORKS (has __contains__ method for all types)
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
#    c. Finding position (index)
#    d. Checking membership (in)
#    e. Length (len)
#    f. Minimum & Maximum (min, max)
#    g. Counting items (count)
#    h. Sum (Sum)
# ❗ Note: Sets do NOT support Indexing, Slicing and Finding position.

# 3. Adding Elements and Combining collections (Mutability - Applies to Lists & Sets)
#    a. Add single element
#        i. List → .append() or .insert()
#        ii. Set → .add()
#    b. Add multiple elements
#        i. List → .extend()
#        ii. Set → .update()
#    c. Concatenation of collections
#        i. List → list1 + list2 or .extend()
#        ii. Set → .union()
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

# 6. Set Operations (Unique to Sets)
#    a. Intersection
#    b. Difference

# 7. Iteration (Loops Across Collections)
#    a. Basic for loop
#    b. enumerate()
#    c. enumerate(start=1)
#    d. zip()
#    e. zip() with different length lists

# 8. Transforming Collections (Applies mainly to Lists)
#    a. List comprehensions
#    b. Splitting strings into lists
#    c. Joining lists into strings

# 9. Empty Collections
#    a. Empty List []
#    b. Empty Tuple ()
#    c. Empty Set set() (not {}!)

# 10. Clear all elements from collections
# ============================================================================

# ============================================================================
# 1. CREATING COLLECTIONS (ALL TYPES)
# ============================================================================
print("\n" + "="*80)
print("1. CREATING COLLECTIONS (ALL TYPES)")
print("="*80)
# Create simple examples of list, tuple and set
general_courses_list = ['Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science']
print("String list general courses:", general_courses_list)
general_courses_tuple = ('Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science')
print("String tuple general courses:", general_courses_tuple)
general_courses_set = {'Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science'}
print("String set general courses:", general_courses_set)
extend_course_list = ['Mechanical System', 'Engineering Drawing']
print("String list extended course:", extend_course_list)
extend_course_set = {'Mechanical System', 'Engineering Drawing'}
my_num_list = [1, 2, 3, 4, 5]
print("Number list:", my_num_list)
my_num_tuple = (1, 2, 3, 4, 5)
print("Number tuple:", my_num_tuple)
my_num_set = {1, 2, 3, 4, 5}
print("Number set:", my_num_set)

# ============================================================================
# 2. Accessing & Reading Data(Applies mainly to Lists & Tuples)
# ============================================================================
print("\n" + "="*80)
print("2. Accessing & Reading Data")
print("="*80)
print("a. Indexing(List and Tuple) - Accessing elements using index(+ and -)")
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
print("   Count elements in list:", general_courses_list.count("Spanish"))                              # Output: 1
print("   Count elements in tuple", my_num_tuple.count(4))                                              # Output: 4

print("\ng. Finding index of element in collection(List and Tuple)")
print("   Index of 'Hindi' in the list:", general_courses_list.index('Hindi'))                          # Output: 3
print("   Index of 'Social Science' in the tuple:", general_courses_tuple.index('Social Science'))      # Ouput: 6

print("\ng. Sum of all elements in the collection")
print("   Sum of elements in the list:", sum(my_num_list))                                              # Output: 15
print("   Sum of elements in the tuple:", sum(my_num_tuple))                                            # Output: 15
print("   Sum of elements in the set:", sum(my_num_set))                                                # Output: 15


# ============================================================================
# 3. Adding Elements (Mutability - Applies to Lists & Sets)
# ============================================================================
print("\n" + "="*80)
print("3. Adding Element (Lists and Sets)")
print("="*80)
print("a. Add elements to lists and sets") 
general_courses_list.append('Arts')
print("   Add 'Arts' to the list =>", general_courses_list)                                             # Output: ['Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science', 'Arts']
general_courses_list.insert(0, 'Biology')
print("   Add 'Biology' to the list =>", general_courses_list)                                          # Output: ['Biology', 'Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science', 'Arts']
general_courses_set.add('Chemistry')
print("   Add 'Chemistry' to the set =>", general_courses_set)                                          # Output: {'Chemistry', 'Spanish', 'Social Science', 'Physics', 'Math', 'English', 'Science', 'Hindi'}
print("\nb. Add mulitple items to lists and sets")
general_courses_list.extend(extend_course_list)
print("   Add extended courses list to general courses list =>", general_courses_list)                  # Output: ['Biology', 'Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science', 'Arts', 'Mechanical System', 'Engineering Drawing']
general_courses_set.update(extend_course_set)
print("   Add extended courses set to general courses set =>", general_courses_set)                     # Output: {'Engineering Drawing', 'Physics', 'Chemistry', 'Spanish', 'English', 'Math', 'Hindi', 'Science', 'Social Science', 'Mechanical System'}
print("\nc. Concatenation of lists and sets")
final_course_list = general_courses_list + extend_course_list
print("   Concatenation of lists =>", final_course_list)                                                # Output: ['Biology', 'Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science', 'Arts', 'Mechanical System', 'Engineering Drawing', 'Mechanical System', 'Engineering Drawing']
final_course_set = general_courses_set.union(extend_course_set).union({'Engineering Mechanics'})
print("   Concatenation of sets =>", final_course_set)


# ============================================================================
# 4. Removing Elements (Mutability - Applies to Lists & Sets)
# ============================================================================
print("\n" + "="*80)
print("4. Removing Elements (Lists and Sets)")
print("="*80)
print("a. Remove by value from lists and sets")
general_courses_list.remove("Engineering Drawing")
print("   Remove 'Engineering Drawing' from the list =>", general_courses_list)                         # Output: ['Biology', 'Math', 'Science', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science', 'Arts', 'Mechanical System']
general_courses_set.remove("Mechanical System")
print("   Remove 'Mechanical System' element from the set =>", general_courses_set)                     # Output: {'Social Science', 'Math', 'Science', 'Engineering Drawing', 'Chemistry', 'Physics', 'English', 'Spanish', 'Hindi'}
general_courses_set.discard("Engineering Drawing")
print("   Discard 'Engineering Drawing' element from the set =>", general_courses_set)                  # Output: {'Social Science', 'Math', 'Science', 'Chemistry', 'Physics', 'English', 'Spanish', 'Hindi'}
print("\nb. Remove by index from lists and sets")
general_courses_list.pop(2)
print("   Remove index 2 element from the list =>", general_courses_list)                               # Output: ['Biology', 'Math', 'English', 'Hindi', 'Physics', 'Spanish', 'Social Science', 'Arts', 'Mechanical System']
del general_courses_list[2]
print("   Delete element from list index 2 =>", general_courses_list)                                   # Output: ['Biology', 'Math', 'Hindi', 'Physics', 'Spanish', 'Social Science', 'Arts', 'Mechanical System']


# ============================================================================
# 10. Ordering & Rearranging (Mainly Lists)
# ============================================================================
print("\n" + "="*80)
print("4. Ordering and Rearranging of list.")
print("="*80)
print("a. ")
# 5. Ordering & Rearranging (Mainly Lists)
#    a. Sorting (.sort(), sorted())
#    b. Reversing (.reverse())


# ============================================================================
# 10. Clear all elements from list and set
# ============================================================================
print("\n" + "="*80)
print("4. Clearing Elements from Lists and Sets")
print("="*80)
print("a. Clear all element from Lists and Sets")
general_courses_list.clear()
print("   Clear all elements from list:", general_courses_list)
general_courses_set.clear()
print("   Clear all elements from set:", general_courses_set)