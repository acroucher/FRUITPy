# What is FRUITPy?

FRUITPy is a module for building and running Fortran unit tests using a Python interface to the [FRUIT](http://sourceforge.net/projects/fortranxunit/) library, as a simple alternative to some of the original Ruby tools provided with FRUIT.

Enjoy a slice of FRUITPy while maintaining Fortran!

[![Build Status](https://travis-ci.org/acroucher/FRUITPy.svg)](https://travis-ci.org/acroucher/FRUITPy)

# Installing FRUITPy:

First, you need to have FRUIT itself installed on your machine. If you want to use FRUITPy for parallel unit testing using MPI, you will need FRUIT version 3.3.0 or later.

All you really need are the main FRUIT source files, fruit.f90 and fruit_util.f90 (for newer versions of FRUIT, the util module was integrated into fruit.f90 so there is no fruit_util.f90) and fruit_mpi.f90 for parallel unit testing. You need to be able to link your Fortran unit test code to these files. You can either compile them in directly (as suggested by the FRUIT developers) or you may prefer to compile these two files into a library that you can link to. A makefile for doing that is included with FRUITPy (fruit_makefile)- just copy this to the FRUIT base directory, rename it as 'makefile' and type `make` and then `make install`. (You can edit the INSTALL_DIR and INCL_DIR in the makefile if you want the library and Fortran module files installed somewhere different from the defaults.)

FRUITPy can be installed via `pip`, e.g. `pip install FRUITPy`.

Alternatively, it is possible to either download the zip file and unzip it, or clone the FRUITPy Git repository, as you prefer. Then you may install it by running `python setup.py install`, in the FRUITPy directory.

# Running Fortran unit tests using FRUITPy:

Create a Python script that imports the FRUIT module, and creates a `test_suite` object to control the unit tests. You can use its `build_run()` method to write the test driver Fortran program, build it and run it. Or if you prefer, you may use the `write()`, `build()` and `run()` methods individually.

Here's a simple example FRUITPy script, testing two Fortran modules:

```python
from FRUIT import *

test_modules = ["test_orange.F90", "test_banana.F90"]
driver = "test_driver.F90"
build_command = "make test_driver"

suite = test_suite(test_modules)
suite.build_run(driver, build_command)
suite.summary()
```

An example using FRUITPy to run the original 'FRUIT in 3 minutes' example can be found on the [FRUITPy wiki](https://github.com/acroucher/FRUITPy/wiki).

# Conventions for test modules to be run by FRUITPy

FRUITPy assumes the following conventions for your Fortran test modules:

* each test module should contain a 'use fruit' line, and a use statement for the module being tested

* after the 'contains' statement, put your tests into subroutines, with no arguments (with or without brackets)

* each test subroutine name should start with 'test_'

* the title of each test (to be displayed in the test results) can optionally be put as a comment in the first non-blank line of the subroutine (otherwise the subroutine name will be used in output)

* end each subroutine with an 'end subroutine' statement (with the subroutine name optionally at the end)

* refer to the FRUIT documentation for usage of FRUIT commands (assert_true() etc.)  in the subroutines

* one of your modules may contain subroutines called 'setup' and 'teardown', to be called respectively before and after all the tests are run (these subroutines can optionally be in their own module, with no test subroutines in it- useful for setup/ teardown of multiple test modules)

* each module may also have its own module-specific setup and teardown routines, to be called before and after the tests for that module are run. The name of a module setup routine must contain '\_setup' or 'setup\_', and the name of a module teardown routine must contain '\_teardown' or 'teardown\_'.

# Files created by FRUITPy

When you call the `build_run()` method of a `test_suite` object, it will create a Fortran driver source file for the suite of tests, and build it into a driver executable. Specify the desired driver source file name in your call to build_run(), along with the command for building the driver. This could be e.g. a make command if you have a makefile to build the driver.

If the driver program is successfully built, it will have a name based on the driver source file name (with a *.exe extension added on Windows systems). Note that this naming convention must be respected in your build command (e.g. makefile). Your makefile or other build command will also need to specify how to link to your code under test, to your test modules and to FRUIT (see above for methods of linking to FRUIT).

If all goes well, the driver program will run and FRUIT will carry out the tests. The FRUIT console output is not displayed automatically, but is saved in the `test_suite` `output` property, and is also written to an output file (with same base name as the driver program, but with a '.out' extension).

FRUITPy does not support the optional XML output that FRUIT can produce. Unfortunately this XML output is not well-formed, according to Python's XML parser.

# Output from FRUITPy

The `test_suite` `build_run()` method returns True if all tests were built and passed successfully, and False otherwise. (You can check the `test_suite` `built` property to see if the test were built successfully, independently of whether they passed or not.)

You can also access summary statistics via the `test_suite` properties `asserts` and `cases`, which have their own properties `success`,`total` and `percent`. The test failure messages are accessible via the test_suite `messages` property (a list of strings).

You can print a summary of the results by using the `test_suite` `summary()` method.

Anything printed to standard output during the tests (e.g. FRUIT output, and anything your unit tests might print) can be accessed via the `test_suite` `output_lines` property (a list of strings).

# Parallel unit testing using FRUITPy

If you have FRUIT version 3.3.0 or later, you can use FRUITPy to do parallel unit testing using MPI. The procedure to follow is mostly the same as for serial unit testing, with these differences:

- add the `num_procs` parameter to the `build_run()` (or `run()`) command and specify the number of processors to use, an integer value greater than 1

- include commands for initializing and finalizing MPI in your `setup()` and `teardown()` Fortran routines (e.g. `call MPI_init(ierr)` and `call MPI_finalize(ierr)`)

- use an MPI wrapper compiler in your makefile to build the test suite, e.g. `mpif90`

If you want to force using MPI even on one processor, set the optional parameter `mpi = True` in the `build_run()` (or `run()`) calls. This can avoid rebuilding the test executable between runs with one and more than one processor.

# Licensing

FRUITPy is free software, distributed under the GNU General Public License (GPL).

# Issues

FRUITPy should work on most computing platforms, but has so far only been tested on Linux.
