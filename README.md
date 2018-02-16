# Python Notes

These are just some random bits and bobs about Python.

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