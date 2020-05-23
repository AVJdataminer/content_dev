---
title: Programming as a data scientist
author: Thinkful
team: grading
time: 30 minutes
uuid: cc6f2055-2f42-4f62-abf9-eafd0e4b95eb
timeHours: 0.5
---

## Why Python?

Python is a free, open-source, and super versatile programming language. Python can be used for nearly any programming project imaginable—from web development, to database management, to data science.

Developed in the late 1980s, Python [has exploded](https://www.economist.com/graphic-detail/2018/07/26/python-is-becoming-the-worlds-most-popular-coding-language) in popularity in recent years, particularly in the data science profession. For that reason, it's essential that you hone your Python skills for your future career. 

In this program, you will be programming in Python 3. This is the latest version of the language and the one you'd be most likely to use on the job. However, Python 2 is still used, and it's not always compatible with Python 3! You don't need to understand all [the details](https://wiki.python.org/moin/Python2orPython3) of this incompatibility right now. But you should know this: if you're ever executing code that you found online and it's not working properly, the problem could be that the code was written for Python 2. Before troubleshooting anything else, check whether the code was written for Python 2 or Python 3.
    
## Standard library functions
A feature of modern programming languages is a library of standard functions. This allows users to work with a set of standard, well-tested and optimised functions for performing common tasks rather than writing our own. The use of  libraries results in more efficient programs written in less time.

Python has a substantial [standard library](https://docs.python.org/3/library/) where a slue of pre-built functions are available for use upon installation. An example of a function provided in the standard library is `type()` this function returns the data type of the input object to the user. Functions with similar purposes are organized into *Modules*. For example the Standard Python Library contains the [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).") module which contains the following types of mathematical functions and constants:
-   [Number-theoretic and representation functions](https://docs.python.org/3/library/math.html#number-theoretic-and-representation-functions)
-   [Power and logarithmic functions](https://docs.python.org/3/library/math.html#power-and-logarithmic-functions)
-   [Trigonometric functions](https://docs.python.org/3/library/math.html#trigonometric-functions)
-   [Angular conversion](https://docs.python.org/3/library/math.html#angular-conversion)
-   [Hyperbolic functions](https://docs.python.org/3/library/math.html#hyperbolic-functions)
-   [Special functions](https://docs.python.org/3/library/math.html#special-functions)
-   [Constants](https://docs.python.org/3/library/math.html#constants)

 To organise it, most functionality is arranged into 'modules', with each module providing a range of related functions. Before you program a function, check if there is a library function that can perform the task. 
Search engines are a good way to find library functions, e.g. entering "Is there a Python function to compute the hyperbolic tangent of a complex number" into a search engine will take you to the function `cmath.tanh`. Try this link: http://bfy.tw/7aMc.

## Other libraries - Modules and Packages

The standard library tools are general purpose and will be available in any Python environment.
Specialised tools are usually made available in other libraries (modules). The is a huge range of Python libraries available for specialised problems. We have already used some parts
of NumPy (http://www.numpy.org/), which is specialised library for numerical computation. 
It provides much the same functionality as MATLAB. 

The simplest way to install a non-standard library is using the command `pip`. From the command line, the library NumPy is installed using:

    pip install numpy
    
and from inside a Jupyter notebook use:

    !pip install numpy

NumPy is so commonly used it is probably already installed on computers you will be using.
You will see `pip` being used in some later notebooks to install special-purpose tools.

When developing programs outside of learning exercises,
if there is a no standard library module for a problem you are trying to solve, 
search online for a module before implementing your own.
## Modules - what are they
   Python's large and ever-growing user base has also developed and contributed to thousands of libraries, which are available to Python users like you. These libraries can help with many programming tasks. No matter what your program's objective is, the chances are high that there's a "package" for that!
   
## Interactive python
Python modules that allow for user feedback 
    
## Jupyter notebooks
We will be computing using Jupyter notebooks (http://jupyter.org/) and 
the programming language *Python* (https://www.python.org/).
Jupyter notebooks provide an interactive environment where you can mix text, equations, computer code and visual outputs. This is new technology that is increasingly widely used, and it is all free and open-source. You can run Jupyter and Python locally on your own computer. The _Anaconda_ environment is recommended. It is free and available at [https://www.continuum.io/downloads](https://www.continuum.io/downloads). Make sure you select the Python 3 version.
   + Jupyter lab
   + 
## kernels
    ### what they are
    ### examples
    
## troubleshooting notebooks
    
## Magic Jupyter Functions
#let's learn some cool stuff
## Welcome to Jupyter

Below, you'll see a Jupyter Notebook that has been embedded in the curriculum app. Broadly speaking, Jupyter Notebooks provide an interactive development environment that allows you to create and share code, data, equations, and other technical and nontechnical material. You'll use Jupyter Notebooks in many checkpoints in this program.

Jupyter Notebooks are cloud-based, so you can't save files directly to your computer. Instead, you will download them and then upload them to another service. The next checkpoint will discuss those details—for now, just buckle up and enjoy your journey to Jupyter!

<jupyter notebook-name="jupyter_intro" course-code="DSBC"></jupyter>

## Assignment

To complete this checkpoint, rework this Notebook so that it's a single cell with the following line of code in it:

```
print('Hello world from Jupyter notebooks')
```

Once you've made these changes, save this Notebook locally by clicking **File > Download as > Notebook (.ipynb)** at the top of the Jupyter Notebook interface. You'll save it as the file type `.ipynb`—this is the file type that is used to store Jupyter Notebooks. Save the Notebook on your computer, and name the file *hello_world_from_jupyter.ipynb*. 

Finally, upload your *hello_world_from_jupyter.ipynb* file to a place that is publicly accessible on the web, such as GitHub. Submit a link to it below to show that you're able to run, modify, save, and distribute Jupyter Notebooks.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NjU2ODIzMjUsLTIwMDgwOTYyNzksNz
YwOTYyNjI3LDExNzMwMDEwNzgsLTEzNDM5NjU2ODksMTY0MDYw
ODE3OSwtMjA1OTMyOTY5MCwtMTkzMTAxNDI3NV19
-->