# run-js
> Goal: The Easiest Way to Run JavaScript in Python

# features
- Stateless
- Async JS Functions
- No Intermediary Files
- Functional Programming
- CommonJS and ES6 Modules
- Automatic JSON Conversion
- Clear Installation Prompts

# install
```bash
pip install run-js
```

# usage
```python
# import the package name from js
from js import lodash

# access the function as an attribute
result = lodash.uniq([1, 2, 2, 3, 3, 3])
// result is [1, 2, 3]
```

# Frequently Asked Questions
### what if my JavaScript package has a dash in the name?
Python doesn't allow - in import statements, so we can access the library as a dictionary lookup.
```python
import js

fastMin = js['fast-min']

result = fastMin([1, 2, 2, 3, 3, 3])
// result is 1
```

# limitations
## json-serializable input
run-js currently only supports running functions that accept JSON-serialized input. 
In other words, you can only call a function that accepts numbers, string, arrays, and object.
You can't pass a Python Function as a parameter.
## stateless
For security reasons, run-js doesn't keep a JavaScript process running the background.  Therefore,
you can't chain JavaScript function calls.

# support
Email the library author at daniel.j.dufour@gmail.com or post an issue at https://github.com/DanielJDufour/run-js/issues
