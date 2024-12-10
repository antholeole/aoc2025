import argparse
import importlib
import sys
import os
from typing import Callable, Any

def run_aoc_day():
    parser = argparse.ArgumentParser(
        description="Run an Advent of Code solution for a specified day.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    _ = parser.add_argument(
        "day", 
        type=int, 
        help="The day number to run (e.g., 1 for day1/day1.py)."
    )
    
    _= parser.add_argument(
        "input_path", 
        type=str, 
        help="The path to the input file for that day."
    )
    
    args = parser.parse_args()
    
    day_number: int = args.day # noqa
    input_path: str = args.input_path # noqa
    
    try:
        with open(input_path, 'r') as f:
            input_content = f.read().strip()
    except FileNotFoundError:
        print(f"Error: Input file not found at path: {input_path}")
        sys.exit(1)

    # Use 'dayN.dayN' as the module name
    module_name = f"day{day_number}.day{day_number}"
    
    try:
        # We need to add the *parent* directory of the 'dayN' directory to sys.path
        # to allow the relative import structure to work. We set this to the current directory.
        sys.path.append(os.getcwd())
        
        # Import the full submodule: 'day1.day1'
        solution_module = importlib.import_module(module_name)
        
    except ModuleNotFoundError:
        print(f"Error: Solution module '{module_name}' not found.")
        print(f"Make sure you have a directory 'day{day_number}' containing a file 'day{day_number}.py'.")
        sys.exit(1)
    
    try:
        solve_function: Callable[[str], Any] = getattr(solution_module, "solve")
    except AttributeError:
        print(f"Error: Module '{module_name}' must define a function named 'solve(input_data: str)'.")
        sys.exit(1)
        
    
    try:
        result = solve_function(input_content)
        print("\n" + "="*40)
        print(f"         ✨ RESULT (Day {day_number}) ✨")
        print("="*40)
        print(f"{result}")
        print("="*40)
    except Exception as e:
        print(f"\nAn error occurred during execution of the solution for Day {day_number}: {e}")

if __name__ == "__main__":
    run_aoc_day()
