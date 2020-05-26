---
title: Objects and modules
author: Thinkful
team: grading
time: 120 minutes
uuid: 186cc634-f4ac-4ead-8502-90eb3357e4c2
timeHours: 2
---
## Working with Modules
Knowing what modules are and working with them can be two different things all together. So, let's breakdown how you work with modules. 

Check to see if the module you would like is installed. `
pip list | grep <module_name_you_want_to_check>
` If you installed Python using Anaconda many common packages you will want to use such as Numpy will already be installed. You can get the entire list of modules installed in your current Python environment using `pip list`. 
### Installing modules
Let's say you wanted to install the Geopandas module for working with spatial data in Python. There are three essential ways to install a package and the one you choose depends on your current Python management setup and preferrence. 

 1. If you use the conda package manager `conda install geopoandas`
 2. If you prefer pip `pip install geopandas`
 3. Finally if you'd like to install directly from the source. 

### Loading modules
 

### Dependencies
Some packages will have dependencies, i.e. other modules they depend on in order to run properly. You can check the dependencies of a package using the `pip show` command. 
    
-   Module loading errors

## Objects
It's time to talk about something you've been using every time you write Python, but that you may not have been thinking about: objects.

You've been using objects all along because _everything in Python_ is an object. 

Integers? Objects. 

Strings? Objects. 

Lists, dictionaries, Booleans... even functions. All of these are objects.

Objects and "object-oriented programming" are deep topics that cut to the core of Python and computer science. 

Mainly, you need to recognize objects when you see them and know how to interact with them in your code. Let's practice in the below notebook.

<jupyter notebook-name="working_with_objects_modules_libraries" course-code="DSBC"></jupyter>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI4NzcxMzI4Myw1NjkyNjMwNDRdfQ==
-->