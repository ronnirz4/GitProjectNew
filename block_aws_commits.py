#!/usr/bin/env python
import sys

AWS_KEYWORDS = ['AWS']  # Add more keywords as needed

def main(argv=None):
    if argv is None:
        argv = sys.argv

    commit_msg_file = argv[1]
    with open(commit_msg_file, 'r') as f:
        commit_msg = f.read()

    for keyword in AWS_KEYWORDS:
        if keyword in commit_msg:
            print(f"Commit message contains AWS keyword '{keyword}'.")
            print("Commit rejected.")
            return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
