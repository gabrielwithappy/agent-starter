#!/usr/bin/env python3
import sys

def main():
    try:
        # Example logic
        if len(sys.argv) > 1:
            print(f"Received argument: {sys.argv[1]}")
        else:
            print("Hello from the new skill!")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
