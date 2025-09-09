#!/usr/bin/env python3
"""
Test runner script showing different ways to run tests with imports
"""
import sys
import os
import subprocess

def run_tests():
    """Run tests using different methods"""
    
    print("=== Running Tests with Different Import Methods ===\n")
    
    # Method 1: Run test directly (uses absolute imports)
    print("1. Running test directly:")
    try:
        result = subprocess.run([sys.executable, "test/unit_test.py"], 
                              capture_output=True, text=True, cwd=os.getcwd())
        print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        print("Return code:", result.returncode)
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Method 2: Run as module (enables relative imports)
    print("2. Running as module (enables relative imports):")
    try:
        result = subprocess.run([sys.executable, "-m", "test.unit_test"], 
                              capture_output=True, text=True, cwd=os.getcwd())
        print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        print("Return code:", result.returncode)
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Method 3: Run with unittest discovery
    print("3. Running with unittest discovery:")
    try:
        result = subprocess.run([sys.executable, "-m", "unittest", "discover", "test"], 
                              capture_output=True, text=True, cwd=os.getcwd())
        print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        print("Return code:", result.returncode)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_tests()

