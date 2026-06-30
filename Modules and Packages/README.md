#### Modules & Packages

---

#### Modules

A module is simply a separate python fule  that holds related code. A module is one file
You can import files from a different python file into other files.  When you do so, the pattern is filename.functionname()

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

---

#### Built in modules

Python comes with over 20 module ready to use. 

For example:
- math 
- random
- datetime

Packaging and modeling
Does this mean when we're working with pandas and numpy, we are importing functions?