# JSON

## Links
* [Official Docs](https://docs.python.org/3.6/library/json.html)
* [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/scenarios/json/)

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