"Python utility to create R package directories from the shell"
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(
    description=('Create an Rpackage in a development root. Calls R and then '
                 'devtools::create()')
)
parser.add_argument('packagename',
                    help=('name of package to create. '))

args = parser.parse_args()
current_directory = os.path.dirname(os.path.realpath(__file__))
package_path = os.path.join(current_directory, args.packagename)

R_cmd = (
    "library(devtools); create('%s')" % package_path
)

subprocess.call(['R', '-e', R_cmd])
