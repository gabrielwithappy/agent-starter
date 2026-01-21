---
name: hello-world
description: A simple hello-world skill that outputs an input string using Python
---

# Hello World Skill

This is a simple test skill that demonstrates how to use Python to output an input string.

## Purpose

This skill accepts a string input and outputs it using a Python script. It's designed to test the basic skill functionality.

## Usage

When you need to output a string using this skill:

1. Call the Python script located at `scripts/hello.py`
2. Pass the input string as a command-line argument
3. The script will output the string to stdout

## Instructions

To use this skill:

```bash
python scripts/hello.py "Your message here"
```

The script will output the exact string you provide.

## Example

Input: "Hello, World!"
Output: "Hello, World!"
