import argparse
import os

def get_vm_path(alias):
    # Read the configuration file and look for the specified alias
    with open('C:/Program Files/VMwrap/dist/vm_config.txt', 'r') as f:
        for line in f:
            parts = line.strip().split('=')
            if parts[0] == alias: 
                return parts[1]

    # If the alias is not found in the configuration file, raise an error
    raise ValueError(f'Error: Invalid alias "{alias}"')

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Wrapper for vmrun utility')
    parser.add_argument('arg', choices=['start', 'stop', 'reset'],
                        help='operation to perform on the VM')
    parser.add_argument('alias', help='alias of the VM')    
    parser.add_argument('option', nargs='?', default="", help='option for the start/stop/reset operations (gui/nogui, soft/hard)')
    args = parser.parse_args()

    # Call the appropriate function based on the argument
    vm_path = get_vm_path(args.alias)
    os.system(f'vmrun.exe {args.arg} {vm_path} {args.option}')

if __name__ == '__main__':
    main()
