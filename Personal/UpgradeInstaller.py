from os import path, listdir, environ
from subprocess import run, PIPE

# the well known path to the upgrade daemon
UPGRADEDM_PATH = path.join(environ['PROGRAMFILES(X86)'], r'Cordic\Upgrade\UpgradeDM.exe')
# the properly formatted command
APPLY_PACKAGE_FILE = r'/cmd applypackagefile /file:'
APPLY = '/apply'
VERIFY = '/verify'
EXTENSION = '.zip'

# need to known the location of the upgrade packages
package_path = input('Enter the path to the upgrade package(s): ')
package_path = package_path.lower().rstrip()
apply_verify = input('Enter apply or verify: ')
if apply_verify == 'apply':
    apply_verify = APPLY
else:
    apply_verify = VERIFY

# get a list of files in the specified location with .zip extensions
found_files = [fn for fn in listdir(package_path) if fn.lower().endswith(EXTENSION)]

# pump the files into the UpgradeDM cli
for file in found_files:
    file_path = '"{0}"'.format(path.join(package_path, file))
    command = '"{path}" {command}{file} {apply}'.format(path=UPGRADEDM_PATH,
                                                        command=APPLY_PACKAGE_FILE,
                                                        file=file_path,
                                                        apply=apply_verify)
    # command = ['{0}'.format(UPGRADEDM_PATH),
    #            '{0}{1}'.format(APPLY_PACKAGE_FILE, file_path),
    #            '{0}'.format(apply_verify)]

    print(command)
    process = run(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if process.returncode == 0:
        print(process.stdout)
    else:
        print(process.stderr)
