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
# import the package from JavaScript into Python
from js import lodash

# access a function as an attribute
result = lodash.uniq([1, 2, 2, 3, 3, 3])
# result is [1, 2, 3]
```

# Frequently Asked Questions
### what if my JavaScript package has a dash in the name?
Python doesn't allow `-` in import statements, so `js` is also a dictionary.
```python
import js

fastMin = js['fast-min']

result = fastMin([1, 2, 2, 3, 3, 3])
// result is 1
```
### do I need to understand JavaScript packaging?
If you try to run a JavaScript package and it isn't installed, run-js will automatically
provide you a prompt to install it.  You don't have to learn NPM's [package.json format](https://docs.npmjs.com/files/package.json/).

### do I need to install NodeJS?
Yes, you currently must install NodeJS on your system before using run-js.  The NPM CLI is also required, but usually comes with the NodeJS installation.  If you are using MacOS, you can install it with `brew install node`.  We will try to add friendly prompts to install NodeJS in the future.  (It's a little complicated because of all the different platforms to support.)

# limitations
## only json-serializable input
run-js currently only supports running functions that accept JSON-serializable input. 
In other words, you can only call a function that accepts numbers, string, arrays, and simple objects.
You can't pass functions or sets as a parameter. (We may try to fix this in the future, but only if it can be done securely.)

## stateless
For security reasons, run-js doesn't keep a JavaScript process running in the background.  Therefore,
you can't chain JavaScript function calls.

# more examples
```python
import js

# calculate statistics
js['calc-stats']([291, 1723, 74, 741, 93, 84, 19])
{ "min": 1, "max": 100, "mean": 66.25, "median": 70, "mode": 95, "modes": [90, 100], "sum": 328350, "histogram": { ... } }

# run-length decoding
js['fast-rle/decode']([5, 3, 1, 8, 2, 0])
[3, 3, 3, 3, 3, 8, 0, 0]

# reprojecting geospatial bounding boxes
js["reproject-bbox"]({"bbox": [-122.51, 40.97, -122.34, 41.11], "from": 4326, "to": 3857})
[-13637750.817083945, 5007917.677222896, -13618826.503649088, 5028580.202823918 ]

# clipping hyperrectangle (multi-dimensional rectangle) from imagery data
js['xdim'].clip({ "data": [0, 123, 123, 255, ...], "layout": "[row,column,band]", "sizes": {"band": 4, "row": 768, "column": 1024 }, "rect": { "band": [2,2], "row": [20, 219], "column": [47, 211]}})
[213, 542, 521, 481, ...]
```

# necessary disclaimer
Use at your own risk.

# thanks
This project was partially inspired by the awesome Python package called [sh](https://github.com/amoffat/sh).

# support
Email the library author at daniel.j.dufour@gmail.com or post an issue at https://github.com/DanielJDufour/run-js/issues
