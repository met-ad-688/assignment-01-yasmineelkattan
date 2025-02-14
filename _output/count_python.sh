#!/bin/bash
# This script counts the number of Python files in the home directory

find $HOME -type f -name "*.py" | wc -l


