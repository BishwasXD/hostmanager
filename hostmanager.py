import os
import sys
"""
A cli tool which loops backs the site to local machine my manipulating ect/hosts
"""

filepath = '/etc/hosts'

args = sys.argv
command = args[1]
site = args[2]

if site is None:
    print("Error: Site name not provided")

if os.getuid() != 0:
    raise PermissionError("This script must be run as a root.")


def block(filepath, site):
    write_this = f"\n 127.0.0.1 www.{site}.com"
    try:
        with open(filepath, 'a') as file:
            file.write(write_this)

    except PermissionError:
        print("Permission denied. Try running this script as sudo.")

    except Exception as e:
        print(f"Error occured: {e}")


def unblock(filepath, site):
    pass


def main():
    if command == "block":
        block(filepath, site)

    elif command == "unblock":
        unblock(filepath, site)

    else:
        print("Command not recognized")


if __name__ == "__main__":
    main()
