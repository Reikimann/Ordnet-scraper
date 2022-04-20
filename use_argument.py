
# https://docs.python.org/3/howto/argparse.html#id1

# These are just a few examples
# See the link above for options like [default, action and more]

import argparse 

parser = argparse.ArgumentParser(description="Program to help me learn")
# Exclusive groups
testGroup = parser.add_mutually_exclusive_group()
testGroup.add_argument("-a", "--argument", type=str, help="adds argrument")
testGroup.add_argument("-y", "--yeet", type=str, help="yeets word")
# Positional arguments
parser.add_argument("example", type=str, help="something example")
# Other arguments, also optional arguments
parser.add_argument("-e", "--echo", type=str, help="echos the specified word")
# True/false
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
# Choices
parser.add_argument("-c", "--choices", type=int, choices=[0, 1, 2],
                    help="example of choice flag")
# Easy way to access args
args = parser.parse_args()
# Assign args to keywords
echo = args.echo
verbose = args.verbose

# if arg true, then ..
if verbose:
    print(args.example)


# if choice == something, then
if args.choices == 2:
    ...
elif args.verbosity == 1:
    ...
else:
    ...
