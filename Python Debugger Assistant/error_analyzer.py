from error_rules import ERROR_EXPLANATIONS

def analyze_error(error_trace, execution_trace=None):
    for error_type in ERROR_EXPLANATIONS:
        if error_type in error_trace:
            explanation = ERROR_EXPLANATIONS[error_type]
            return {
                "error_type": error_type,
                "cause": explanation["cause"],
                "fix": explanation["fix"],
                "context": execution_trace
            }

    return {
        "error_type": "Unknown Error",
        "cause": "This error is uncommon or complex.",
        "fix": "Carefully inspect the traceback and execution context.",
        "context": execution_trace
    }
