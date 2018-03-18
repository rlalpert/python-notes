These are just some random bits and bobs about Python.

<!-- START TOC -->
* [JSON](#json)
	* [JSON Links](#json-links)
* [Dictionaries](#dictionaries)
* [Logic Operations](#logic-operations)
* [Lists](#lists)
	* [Making a unique copy of a list](#making-a-unique-copy-of-a-list)
	* [Reversing the order of a list](#reversing-the-order-of-a-list)
	* [Flattening Lists](#flattening-lists)
* [Packages](#packages)
	* [Package Links](#package-links)
	* [Package Directory Structure](#package-directory-structure)
	* [From Package Import *](#from-package-import-*)
* [Misc](#misc)
	* [Transposing a matrix](#transposing-a-matrix)
* [Links](#links)
<!-- END TOC -->

# JSON

## JSON Links
* [Official Docs](https://docs.python.org/3.6/library/json.html)
* [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/scenarios/json/)
* [Python Cookbook, 3rd Edition](https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html) - Paywall

**Quick Notes**

**Writing JSON data to a file:**
```python
with open('data.json', 'w') as f:
     json.dump(data, f)
```

**Reading JSON data from a file:**
```python
with open('data.json', 'r') as f:
     data = json.load(f)
```

---

Writing JSON **that an actual human can read** to a file:

```python
with open('target_file.json', 'w') as file:
    json.dump(data, file, sort_keys=True, indent=4)
```

# Dictionaries

**Quick Notes**

To initialize the value of a dictionary key as a list you can just use:

`dict_name.setdefault('key_name', [])`

You can even begin adding values to said list by chaing `.append(value)` at the end.

However, to do the same for a set, you can't simply use brackets `{}` because those are reserved for dictionary assignment and will just set the value of that key to a dictionary.

To initialize the value of a dictionary key as a *set*, you must use:

`dict_name.setdefault('key_name', set())`

At that point, you can chain `.add(value)` to add values.

# Logic Operations

**Quick Notes**

The `is` operator compares the internal `id` *(retrieved with the built-in `id()` function)* of two values when checking for equivalency, whereas `==` compares the two values directly.

# Lists

### Making a unique copy of a list

To make a unique copy of a list that doesn't refer to the original list object:

```python
my_list = [1, 2, 3, 4]
new_list = my_list[:]
```

You can now `my_list.append(5)` and `my_list` will return `[1, 2, 3, 4, 5]`, but `new_list` will remain `[1, 2, 3, 4]`.

### Reversing the order of a list

To reverse the order of a list:

```python
cat_jam = ['cat', 2, 3, 4, 5, 'jam']
jam_cat = cat_jam[::-1]
```

`jam_cat` will now return `['jam', 5, 4, 3, 2, 'cat']`.

Works on strings, as well.

### Flattening Lists

```python
>>> a = [[1, 2], [3, 4], [5, 6]]
>>> list(itertools.chain.from_iterable(a))
[1, 2, 3, 4, 5, 6]

>>> sum(a, [])
[1, 2, 3, 4, 5, 6]

>>> [x for l in a for x in l]
[1, 2, 3, 4, 5, 6]

>>> a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
>>> [x for l1 in a for l2 in l1 for x in l2]
[1, 2, 3, 4, 5, 6, 7, 8]

>>> a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
>>> flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
>>> flatten(a)
[1, 2, 3, 4, 5, 6, 7, 8]
```
*from [30 Python Language Features and Tricks You May Not Know About](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html)*

# Packages

## Package Links
* [Official Docs](https://docs.python.org/3/tutorial/modules.html#tut-packages)

## Package Directory Structure

`__init__.py` file (even blank) is required to make Python treat the directory as containing a package. Subfolders containing `__init__.py` files can be imported with dot notation:

```
flameskull/
  __init__.py
  badass/
    __init__.py
    purple_fire.py
    metal_af.py
  weak/
    __init__.py
    flame_is_unicorn_tears.py
    enya.py
```

So you can `import flameskull.badass.metal_af` or `from flameskull.weak import enya` etc.

## From Package Import *

You can explicitly define what is imported with `from package import *` in the `__init__.py` file for that package by assigning them to a list named `__all__`

# Misc

### Transposing a matrix

```python
mommas_groovy_matrix = [[1, 2, 3], [4, 5, 6]]
mommas_transposed_matrix = zip(*mommas_groovy_matrix)
such_wow = list(mommas_transposed_matrix)
```
`such_wow` now returns `[(1, 4), (2, 5), (3, 6)]`

**Quick Notes**

You can check all of the attributes and methods of any object in Python (and everything is an object) by calling `dir()` on it.

Then, you can check to see if any of those items are callable by running `callable()` on them. 

---

If you call the `dir()` function with no arguments, it will return a list of everything in the current namespace.

---

You can call `help()` on a function to get a quick description of it. hit `q` to quit out of the description window.

---

Get the current time in ISO-8601 format: 

```python
import datetime
datetime.datetime.utcnow().isoformat()
```

# Links
**General:**
* [r/python](https://www.reddit.com/r/Python/)

**Resource Lists:**
* [Awesome Python](https://github.com/vinta/awesome-python#admin-panels) - *"A curated list of awesome Python frameworks, libraries, software and resources."*
* [r/learnpython Wiki](https://www.reddit.com/r/learnpython/wiki/index)
* [Full Stack Python - Resources List](https://www.fullstackpython.com/best-python-resources.html)

**Learning Now**
* [Django](https://docs.djangoproject.com/)

**To Read/Watch/Tutorials**:

* [Python and JSON: Working with large datasets using Pandas](https://www.dataquest.io/blog/python-json-tutorial/) -- possible idea for deity project?
* [A Simple Step-by-Step Reportlab Tutorial](https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/)
* [pythonprogramming.net](https://pythonprogramming.net/)
* [Intro and Getting Stock Price Data - Python Programming](https://pythonprogramming.net/getting-stock-prices-python-programming-for-finance/)
* [The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/index.html)
* [What does it take to be an expert at Python? (Video)](https://www.youtube.com/watch?v=4m9ukNTD6-E)
* [Cracking Codes with Python](http://inventwithpython.com/cracking/)
* [How To Train an Object Detection Classifier Using TensorFlow 1.5 (GPU) on Windows 10](https://www.youtube.com/watch?v=Rgpfk6eYxJA)
* [Use Python to Load & Prepare Data Analytics](https://youtu.be/nO78ECRighw)