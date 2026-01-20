import sys

class ExecutionTracer:
    def __init__(self):
        self.error_context = None

    def trace(self, frame, event, arg):
        if event == "exception" and self.error_context is None:
            exc_type, exc_value, _ = arg
            self.error_context = {
                "function": frame.f_code.co_name,
                "line_no": frame.f_lineno,
                "locals": {
                    k: repr(v) for k, v in frame.f_locals.items()
                },
                "exception": exc_type.__name__,
                "message": str(exc_value)
            }
        return self.trace

    def start(self):
        sys.settrace(self.trace)

    def stop(self):
        sys.settrace(None)
