Mission 1: Python Fundamentals
This section covers core syntax, conditional execution pathways, functional modules, and basic file operations. I built a Fibonacci sequence generator that uses a sequential calculation array to resolve values without deep recurrence overhead. Alongside this, I engineered a primality testing module that optimizes runtime by only evaluating factors up to the square root of the target integer. Finally, I implemented persistent file handling routines designed to systematically write data matrices to disk and retrieve them from a plain text file named sample.txt.

To execute this segment, change directories into W1_Fundamentals and run the script utilizing the command python mission1.py.

Mission 2: OOP and Data Structures
This phase focuses on the shift from procedural programming to scalable, object-oriented code architecture. I designed a digital Library Management System organized around a modular hierarchy. The script implements inheritance mechanics by using the super initialization function to pass core attributes from a parent entity down to specific child modules without duplicating code logic. To optimize internal lookups, the system stores active instances inside a native dictionary framework, maintaining consistent access speeds even as the inventory grows. To protect the application from unexpected crashes, I wrapped user data collection steps in standard try and except handling blocks to intercept structural input errors.

To execute this segment, change directories into W2_OOP_DataStructures and run the script utilizing the command python mission2.py.

Mission 3: Practical Automation
This project shifts toward applying programmatic logic to resolve actual workflow bottlenecks. I built an Automated File Organizer utility designed to sweep targeted local directories. The system relies on the built-in operating system and shell utility engines to cross-reference file extension types against an internal destination matrix. The script incorporates directory mapping logic to skip over nested subfolders automatically, preventing recursive loop issues. It also handles absolute system paths safely across different operating systems by generating paths programmatically instead of relying on fixed relative directory strings.

To execute this segment, change directories into W3_Project_Development and run the script utilizing the command python organizer.py.

Mission 4: Code Quality Testing and Portfolio Packaging
To transition these independent projects into production-ready software, this final phase applied engineering benchmarks across the codebase. I introduced automated unit testing using the pytest framework to programmatically validate core logic, isolate edge cases, and catch potential regression bugs during code updates. Every class, method, and function was updated to adhere to PEP 257 docstring standards, explicitly detailing input parameters, variable data types, return behaviors, and operational constraints. Furthermore, the complete repository underwent structured refactoring to systematically eliminate duplicate execution blocks, enforce self-documenting variable naming conventions, and improve overall readability. This packaging phase ensures the repository functions as a highly presentation-ready portfolio demonstrating rigorous developer standards.

To run the automated test suite, ensure the pytest library is installed locally, navigate to the project directory, and execute the command pytest.