import os, sys

# clears terminal
os.system("cls||clear")

print(f"{'='*30}main.py{'='*30}")

# code imported from a module is executed, even when doing 'from module1 import x'
# __name__ is no longer __main__, but 'module1' (when run from outside of module1)
import module1

# namespace
# when importing a module - a reference (in the namespace) will be created to sys.modules
print(globals())
print(globals()["module1"])

# when importing a module - it will be stored in sys.modules
print("sys.modules")
print(sys.modules["module1"])

# from math import sqrt: all math module will be in sys.modules, but only sqrt will be in namespace

# namespace is a dictionary, tracking variables
print(f"\n{'='*30}end main{'='*30}")