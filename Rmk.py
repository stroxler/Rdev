"Python utility to re-document/re-build/re-install R packages from the shell"
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(
    description=('Make an R package from a development root. Place this file '
                 'inside a source directory - of which the subpackages should '
                 'be R package sources - and use this command to re-build and '
                 're-install them. Optionally delete the NAMESPACE file '
                 '(which seems to get corrupted sometimes) before building.')
)
parser.add_argument('packagename',
                    help=('name of package to document / build / install. '
                          'Must be a sub-directory of the directory where '
                          'this file is located.'))
parser.add_argument('--dns', dest='delete_namespace',
                    action='store_true',
                    help='Should NAMESPACE file be deleted?')

args = parser.parse_args()
current_directory = os.path.dirname(os.path.realpath(__file__))
package_path = os.path.join(current_directory, args.packagename)

R_cmd = (
    "library(devtools); document('%s'); install('%s')" % (package_path,
                                                          package_path)
)

if args.delete_namespace:
    filename = os.path.join(package_path, 'NAMESPACE')
    if os.path.isfile(filename):
        os.remove(filename)

subprocess.call(['R', '-e', R_cmd])
