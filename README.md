# Quick-Calc

Quick-Calc is a simple calculator application that supports addition, subtraction, multiplication, division, and a clear function. It is built in Python.

## Setup Instructions

1. Make sure Python 3 is installed
2. Install pytest by running: pip install pytest
3. Clone this repository
4. Navigate into the folder

## How to Run Tests

pytest tests/

## Testing Framework Research

Python has two widely used testing frameworks: Pytest and Unittest. Unittest is built into Python's standard library so no installation is needed. It uses a class-based structure which can feel verbose for simple projects.

Pytest allows tests to be written as plain functions without any class structure. It has cleaner output and is easier to read. It also automatically finds test files without extra configuration.

For this project Pytest was chosen because Quick-Calc is a small application where simplicity matters. The straightforward function-based syntax of Pytest makes tests easier to write and understand.