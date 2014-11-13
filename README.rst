This package does nothing more than save a few utilities for
using python scripts and devtools to build packages whose source
lies in this directory to whatever library is default.

To create a devtools skeleton of a new package::
   python Rcr.py packagename

To do a fresh documentation run and install of a package without forcing
NAMESPACE delete::
   python Rmk.py packagename

Occasionally roxygen2 seems to get something mangled in the NAMESPACE,
in which case you can precede the documentation run above with a forced
delete by adding the `--dns` option::
   python Rmk.py packagename --dns

You can also get help::
   python Rmk.py -h
   python Rcr.py -h
