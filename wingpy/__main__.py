import subprocess
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('file', metavar='f', help='file with list of packages')
args = parser.parse_args()


def command_exists(command, error='is not recognized'):
    command = [command, '--verison']
    return error not in subprocess.getoutput(command)


def open_txt(path):
    with open(path, 'r') as file:
        return [i.strip() for i in file.readlines()]


def install(package):
    print()
    print(f'Installing {package}...')
    try:
        message = subprocess.run(['winget', 'install', package], check=True)
        return {package: 'Installed'}
    except:
        return {package: 'Not Installed'}


def install_from_file(path):
    packages = open_txt(path)
    output = {}
    for package in packages:
        output.update(install(package))
    return output


def _run():
    if command_exists('winget'):
        output = install_from_file(args.file)
        print()
        for package, status in output.items():
            print(f'{package}: {status}')
        installed = len(
            [package for package, output in output.items() if output == 'Installed'])
        not_installed = len(
            [package for package, output in output.items() if output != 'Installed'])
        print()
        if installed:
            print(
                f'{installed} package{"s" if installed!=1 else ""} installed successfully')
        if not_installed:
            print(
                f'{not_installed} package{"s" if not_installed!=1 else ""} failed to install')
    else:
        print('winget not installed, exiting...')
    print(input('Press Enter to continue...'))


if __name__ == '__main__':
    _run()
