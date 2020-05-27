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
    
## The Python Standard Library functions
A feature of modern programming languages is a library of standard functions built-in. This allows users to work with a set of standard, well-tested and optimised functions for performing common tasks rather than writing our own. The use of  libraries results in more efficient programs written in less time.

Python has a substantial [standard library](https://docs.python.org/3/library/) where a slue of pre-built functions are available for use upon installation. An example of a function provided in the standard library is `type()` this function returns the data type of the input object to the user. Functions with similar purposes are organized into *Modules*. For example the Standard Python Library contains the [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).") module which contains the following types of mathematical functions and constants:

 - `math.exp()`
 -  `math.log()`
 -  `math.sqrt()`
 -  `math.cosine()`
 -  `math.pi()`

 The list above is a tiny sampling of the functions available in the `math` module and there are many more modules as well in the standard Python library. It is good to familiarize yourself with the functions available, spend some time reviewing the documentation and using the base Python functions.
 
## Other libraries - Modules and Packages
 As we mentioned earlier because Python is Open-Source and has a large and ever-growing user base, there are thousands of libraries that have been developed and contributed to the community of Python users like you. These libraries are often developed around solving specialized problems and commonly referred to as packages or modules. When developing programs
if there is a no standard library module for a problem you are trying to solve, search online for a module before implementing your own. There is a wide range of Python libraries available for specialised problems. 

Check out the [Python Package Index (PyPI)](https://pypi.org/), a repository of software for Python. Search for different libraries — you’ll find software to help you with everything from sending emails to composing music.

## Interactive python [IPython](url)
IPython is a library that provides a rich toolkit to help users work with Python interactively, similar to a scientfic programming environment like MATLAB. It is made of these components: 
-   A powerful interactive shell.
-   A kernel for  [Jupyter](https://jupyter.org/).
-   Support for interactive data visualization and use of  [GUI toolkits](https://ipython.org/ipython-doc/stable/interactive/reference.html#gui-event-loop-support).
-   Flexible,  [embeddable](https://ipython.org/ipython-doc/stable/interactive/reference.html#embedding-ipython)  interpreters to load into your own projects.
-   Easy to use, high performance tools for  [parallel computing](https://ipyparallel.readthedocs.io/en/latest/).  

## Kernels
The *kernel for Jupyter* is what provides the interactive Python programming environment we use in this course **Jupyter Notebooks**.   A kernel in computer science is the core of the  operating system that allows communication between the user in software applications and the hardware components. In data science kernels have a front-end user side that allows for your programming to be written and pased to the back end host side through this connection. In addition to Jupyter Notebooks you will see the term for running kernels on [Kaggle](https://www.kaggle.com/notebooks) when you open a new notebook to view or compete in data science competitions.

## Jupyter notebooks
 [Jupyter notebooks](http://jupyter.org/)  provide an interactive environment where you can mix text, equations, computer code and visual outputs. The flexibility of this tool has led to it  becoming the standard in data analytics and data science for project development work.  Check out the latest development of Jupyter notebboks, with more functionality [Jupyter Labs](https://jupyter.org/) works in the same way as Jupyter notebooks by creating a connection for user to run code and generate interactive results.
    
## Troubleshooting notebooks
The most common problem you will encouter with Jupyter notebooks is a disconnect from the back end server, the fix is to reload the page. If your notebook does not return the expected results based on your code, double check your code and if you still don't see the problem reload the kernel.  Remember that all the code is dependent on the current kernel, therefore you must run all the previous cells in your notebook for the current one to run properly. Everytime you re-open your notebook you're creating a new kernel connection and must run all the preceding cells to work on a later cell in your notebook. Think of it as a top to bottom operation where sequential cells are executed in order.

## Have you seen my kernel ?
If you see this error simply click the blue button to reload the kernel connection and you should be good start running some code.
![JupyterHub Error] (/Images/server_load_error.png)
    
## Magic Commands
There are some add-ons to Ipython known as Magic Comands that are meant to solve common problems faced by users of the kernel. Some examples include; running an external script `%run myscript.py`, timing a function `%timeit`, and plotting matplotlib figures inline `%matplotlib inline` for viewing. Learn more by reviewing the [docs](https://ipython.readthedocs.io/en/stable/interactive/magics.html).


## Welcome to Jupyter

Below, you'll see a Jupyter Notebook that has been embedded in the curriculum app.  You'll use Jupyter Notebooks in many checkpoints in this program.

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
eyJoaXN0b3J5IjpbNTMyMjI2MjU0LC0yMTE2MDM1OTIxLC0xNj
c1MjE2NjQyLDE2NDI1MjAzNzcsLTE0NDUzODc1LDkxOTI1ODQ2
Miw0MjUyMjM5MDksLTU4MTA2NzQ5OSwxNDgxNjcxMDgsLTE1OT
UwNTMwMDcsLTE2NTI5NjkyMzAsLTIwMDgwOTYyNzksNzYwOTYy
NjI3LDExNzMwMDEwNzgsLTEzNDM5NjU2ODksMTY0MDYwODE3OS
wtMjA1OTMyOTY5MCwtMTkzMTAxNDI3NV19
-->