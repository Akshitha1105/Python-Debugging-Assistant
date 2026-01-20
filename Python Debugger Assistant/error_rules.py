ERROR_EXPLANATIONS = {
    "SyntaxError": {
        "cause": "You wrote Python code that breaks grammar rules.",
        "fix": "Check for missing colons, brackets, or wrong indentation."
    },
    "TypeError": {
        "cause": "You used incompatible data types together.",
        "fix": "Make sure variables are of the correct type before using them."
    },
    "IndexError": {
        "cause": "You tried to access an index that doesn't exist in a list.",
        "fix": "Check list length before accessing elements."
    },
    "KeyError": {
        "cause": "You tried to access a key that does not exist in a dictionary.",
        "fix": "Verify the key exists using `in` before accessing it."
    },
    "NameError": {
        "cause": "You used a variable that was never defined.",
        "fix": "Make sure the variable is defined before using it."
    },
    "IndentationError": {
        "cause": "Your indentation is incorrect.",
        "fix": "Ensure consistent spacing (prefer 4 spaces)."
    }
}