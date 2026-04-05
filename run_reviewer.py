#!/usr/bin/env python3
"""Simple wrapper for JAC to call Backboard Reviewer"""
import sys
from backboard_client import review_code

if __name__ == "__main__":
    code_summary = sys.argv[1] if len(sys.argv) > 1 else "Express + MongoDB"
    result = review_code(code_summary)
    print(result)
