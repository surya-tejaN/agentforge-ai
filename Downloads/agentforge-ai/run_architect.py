#!/usr/bin/env python3
"""Simple wrapper for JAC to call Backboard Architect"""
import sys
from backboard_client import design_architecture

if __name__ == "__main__":
    requirement = sys.argv[1] if len(sys.argv) > 1 else "Build a blog API"
    result = design_architecture(requirement)
    print(result)
