#### Modules & Packages

---

#### Modules

A module is simply a separate python file that holds related code. A module is one file that is meant to be imported by other files. It holds functions, variables, or classes that other files can make use of.
Not to be mistaken with a script. A script is meant to be run directly.
But the same file can do both. In practice, people say module when they mean a file designed to be imported and script when they mean a file designed to be run.

There are different ways to import:
1. Import the whole module 

import filename

2. Import just the function you need

from filename import function function_name

- this method is only handy when you need one thing

3. Import and rename it
import filename as diff_name
- this is best for when the filename is long


---

#### Packages

A package is a folder that holds multiple modules. For python to recognize a folder as a package, it must have the file __init__.py inside it. The file can be empty, it just tells python that this folder is a package. 

*So you actually do not need this in later python files, but it is good to always just have it.*

---

#### Built in modules

Python comes with over 20 module ready to use. 

For example:
- math 
- random
- datetime

Packaging and modeling
Does this mean when we're working with pandas and numpy, we are importing functions?