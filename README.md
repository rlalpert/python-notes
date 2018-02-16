# Python Notes

These are just some random bits and bobs about Python.

* [JSON](#json)
* [Dictionaries](#dictionaries)
* [Logic Operations](#logic-operations)
* [Lists](#lists)
* [Misc](#misc)

# JSON

## Links
* [Official Docs](https://docs.python.org/3.6/library/json.html)
* [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/scenarios/json/)
* [Python Cookbook, 3rd Edition](https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html) - Paywall

## Quick Notes

```python
# Writing JSON data
with open('data.json', 'w') as f:
     json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
     data = json.load(f)
```

*from [Python Cookbook, 3rd Edition](https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html)*

# Dictionaries

## Quick Notes

To initialize the value of a dictionary key as a list you can just use:

`dict_name.setdefault('key_name', [])`

You can even begin adding values to said list by chaing `.append(value)` at the end.

However, to do the same for a set, you can't simply use brackets `{}` because those are reserved for dictionary assignment and will just set the value of that key to a dictionary.

To initialize the value of a dictionary key as a *set*, you must use:

`dict_name.setdefault('key_name', set())`

At that point, you can chain `.add(value)` to add values.

# Logic Operations

## Quick Notes

The `is` operator compares the internal `id` *(retrieved with the built-in `id()` function)* of two values when checking for equivalency, whereas `==` compares the two values directly.

# Lists

##  Quick Notes

### Making a unique copy of a list

To make a unique copy of a list that doesn't refer to the original list object:

```python
my_list = [1, 2, 3, 4]
new_list = my_list[:]
```

You can now `my_list.append(5)` and `my_list` will return `[1, 2, 3, 4, 5]`, but `new_list` will remain `[1, 2, 3, 4`.

### Reversing the order of a list

To reverse the order of a list:

```python
cat_jam = ['cat', 2, 3, 4, 5, 'jam']
jam_cat = ascending_order[::-1]
```

`jam_cat` will now return `['jam', 5, 4, 3, 2, 'cat']`.

Works on strings, as well.

# Misc

## Quick Notes

You can check all of the attributes and methods of any object in Python (and everything is an object) by calling `dir()` on it.

Then, you can check to see if any of those items are callable by running `callable()` on them. 

---

If you call the `dir()` function with no arguments, it will return a list of everything in the current namespace.

---

You can call `help()` on a function to get a quick description of it. hit `q` to quit out of the description window.