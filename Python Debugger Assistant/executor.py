import traceback
from tracer import ExecutionTracer

def execute_code(code):
    tracer = ExecutionTracer()
    try:
        tracer.start()
        exec(code, {})
        tracer.stop()
        return {
            "success": True,
            "output": "✅ Code ran successfully. No errors found."
        }
    except Exception:
        tracer.stop()
        return {
            "success": False,
            "error": traceback.format_exc(),
            "trace": tracer.error_context
        }
