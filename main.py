"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	if n<= 1:
		return n

	return a*simple_work_calc(n//b, a, b) + n

	# TODO
	pass

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n<= 1:
		return f(n)
	
	return a*work_calc(n//b, a, b, f) + f(n)
	pass


def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n <= 1:
		return f(n)

	return span_calc(n // b, a, b, f) + f(n)
	pass

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Params:
	work_fn1....a curried version of work_calc expecting a single input n
	work_fn2....a curried version of work_calc expecting a single input n
	sizes.......list of values for n to compare these two work functions.

	Returns:
	A list of tuples of the form
	[(n, work_fn1(n), work_fn2(n)), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_work_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def print_span_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'S_1', 'S_2'],
							floatfmt=".3f",
							tablefmt="github"))
def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	
    work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: 1)
    work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x)
    work_fn3 = lambda n: work_calc(n, 2, 2, lambda x: x**2)

    # Generate tables to copy into answers.md
    print("\n--- f(n)=1 vs f(n)=n ---")
    print_work_results(compare_work(work_fn1, work_fn2, sizes=[1, 2, 4, 8, 16, 32, 64, 128]))

    print("\n--- f(n)=n vs f(n)=n^2 ---")
    print_work_results(compare_work(work_fn2, work_fn3, sizes=[1, 2, 4, 8, 16, 32, 64, 128]))

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different span recurrences for 
	given input sizes.

	Params:
	span_fn1....a curried version of span_calc expecting a single input n
	span_fn2....a curried version of span_calc expecting a single input n
	sizes.......list of values for n to compare these two span functions.

	Returns:
	A list of tuples of the form
	[(n, span_fn1(n), span_fn2(n)), ...]
	
	"""
	result = []
	for n in sizes:
		# compute S(n) using current a, b, f
		result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result

def test_compare_span():
    # Curry span_calc for a=2, b=2 across the three f(n) functions
    span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: 1)
    span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: x)
    span_fn3 = lambda n: span_calc(n, 2, 2, lambda x: x**2)

    sizes = [1, 2, 4, 8, 16, 32, 64, 128]

    # Generate Github-formatted tables to copy into answers.md for Problem 7
    print("\n--- SPAN: f(n)=1 vs f(n)=n ---")
    print_span_results(compare_span(span_fn1, span_fn2, sizes=sizes))

    print("\n--- SPAN: f(n)=n vs f(n)=n^2 ---")
    print_span_results(compare_span(span_fn2, span_fn3, sizes=sizes))

#test_compare_work()
test_compare_span()
