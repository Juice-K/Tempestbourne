# tkinter_patch.py - Python 3.13 compatibility patch
import tkinter

# Add the missing _flatten function if it doesn't exist
if not hasattr(tkinter, '_flatten'):
    def _flatten(seq):
        """Flatten a sequence of sequences into a single sequence."""
        result = []
        for item in seq:
            if isinstance(item, (list, tuple)):
                result.extend(_flatten(item))
            else:
                result.append(item)
        return result
    
    tkinter._flatten = _flatten

# Add the missing _join function if it doesn't exist
if not hasattr(tkinter, '_join'):
    def _join(seq):
        """Join a sequence of strings with spaces."""
        return ' '.join(str(item) for item in seq)
    
    tkinter._join = _join

# Add the missing _stringify function if it doesn't exist
if not hasattr(tkinter, '_stringify'):
    def _stringify(value):
        """Convert a value to string for Tcl."""
        if isinstance(value, (list, tuple)):
            return ' '.join(_stringify(item) for item in value)
        return str(value)
    
    tkinter._stringify = _stringify

# Add the missing _splitdict function if it doesn't exist
if not hasattr(tkinter, '_splitdict'):
    def _splitdict(tk, v, cut_minus=True, cut_underscore=True):
        """Split a dictionary into Tcl-compatible format."""
        result = []
        for key, value in v.items():
            if cut_minus and key.startswith('-'):
                key = key[1:]
            if cut_underscore:
                key = key.replace('_', '')
            result.extend(['-' + key, str(value)])
        return result
    
    tkinter._splitdict = _splitdict

print("Applied complete tkinter patch for Python 3.13 compatibility")