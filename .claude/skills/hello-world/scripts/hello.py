#!/usr/bin/env python3
"""
Hello World Skill Script
A simple script that outputs an input string.
"""

import sys


def main():
    """
    Main function that outputs the input string.
    If no argument is provided, it prompts for input.
    """
    if len(sys.argv) > 1:
        # Get the input string from command-line arguments
        message = ' '.join(sys.argv[1:])
    else:
        # Prompt for input if no argument is provided
        message = input("Enter a message: ")
    
    # Output the string
    print(message)


if __name__ == "__main__":
    main()
