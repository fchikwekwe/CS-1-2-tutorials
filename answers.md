1. What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?
- Right now the application has the ability to create a histogram in the form of a dictionary. This Dictogram class is in its own file. I'm currently working on a Listogram class that does the same in list form in its own file. A third file will contain a markov class that imports the Dictogram class and uses that to create markov generated "sentences".

2. Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?
- I think that for the most part, my variables are understandable, but I could do a better job of using variable names that are semantic, unique and descriptive.

3. What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?
- The only global variables that I have right now are imports, but even those can still be minimized to a greater extent.

4. Are the functions small and clearly specified, with as few side effects as possible?
- This can definitely be improved upon. I am working on going back through all of my usable code and making it more concise, with as few side effects as possible.

5. Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?
6. Can files be used as both modules and as scripts?
- 

7. Do modules all depend on each other or can they be used independently?
- There are some modules that depend on the others, but even these can be used with various other modules to perform their functions.
