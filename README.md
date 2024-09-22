# Portfolio 3 - Knowledge Question  

1. Describe what sorting is in general?
- Sorting is the method that we used to helps us to organize the elements of a list or an array based on a comparison 
  operator on the elements, for example to show a list of character in increasing order.

2. Research sorting algorithms. Describe advantages and disadvantages for at least three different sorting algorithms.
- Selection sort = In this technique that we find the minimum element in every iteration and place it in the array
  beginning from the first index. 
    - Advantages: is simple and easy to understand, and works well with small datasets.
    - Disadvantages: does not work well on large datasets, and does not preserve the relative order of items with equal
      keys which means it is not stable.
  
- Bubble sort = This is the simplest technique that works by repeatedly swapping the adjacent element if they are in the 
  wrong order.
   - Advantages: is easy to understand and implement, it does not require any additional memory space, and it is a stable
     algorithm, that means that the elements with the same key value maintain their relative order in the sorted output.
   - Disadvantages: it is slow for large data sets, it requires a comparison operator, it can limit the efficiency of
     the algorithm in certain cases.
  
- Insertion sort = Is a simple sorting that works with the virtual array split into a sorted and an unsorted part, the
  elements from the unsorted part are picked and placed at the correct position in the sorted part.
   - Advantages: is simple and easy to implement, is a stable algorithm, efficient for small lists and nearly sorted
     lists, space-efficient and adoptive.
   - Disadvantages: is inefficient for large lists, and not as efficient as other algorithms.

3. Describe why you generally need comparison operators to successfully sort a list of objects. In addition, describe
   how you could sort a list of objects without adding comparison operators.
- We generally need a comparison operator because they define how the object are compared to each other. In some cases
  when we cannot use or just do not use the comparison operators we can sort the list of object by using a key function,
  the key function extracts a comparison key from each list element for example the sort() function or if we do not use
  the sort() function we can sort a list using a nested loop which will be compare each element in the list one by one
  and swap it.

# References 
GeeksforGeeks. “Sorting Algorithms - GeeksforGeeks.” GeeksforGeeks, 5 Apr. 2024, www.geeksforgeeks.org/sorting-algorithms/.

“Selection Sort Algorithm.” GeeksforGeeks, 31 Jan. 2014, www.geeksforgeeks.org/selection-sort-algorithm-2/.

“Bubble Sort Algorithm.” GeeksforGeeks, 2 Feb. 2014, www.geeksforgeeks.org/bubble-sort-algorithm/.

“Insertion Sort Algorithm.” GeeksforGeeks, 7 Mar. 2013, www.geeksforgeeks.org/insertion-sort-algorithm/.

“Sorting HOW to — Python 3.10.2 Documentation.” Docs.python.org, docs.python.org/3/howto/sorting.html.

Python, Real. “How to Use Sorted() and Sort() in Python – Real Python.” Realpython.com, realpython.com/python-sort/.
“Sort a List in Python without Sort Function.” GeeksforGeeks, 24 Aug. 2023, www.geeksforgeeks.org/sort-a-list-in-python-without-sort-function/.
