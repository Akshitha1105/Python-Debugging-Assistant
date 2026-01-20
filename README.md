# 🧠 AI-Powered Python Debugging Assistant

An intelligent developer-focused tool that analyzes Python code, captures runtime errors with execution context, and explains bugs in clear, human-readable language along with fix suggestions.

This project goes beyond basic traceback printing by combining **execution tracing** and **error reasoning**, making it suitable for debugging **complex, multi-function Python programs**.

---

## 🚀 Features

- ✅ Executes user-provided Python code safely
- ✅ Detects runtime and syntax errors
- ✅ Captures **exact execution context at crash time**
  - Function name
  - Line number
  - Local variables and their values
- ✅ Explains errors in simple English
- ✅ Provides fix suggestions for common Python errors
- ✅ Displays full traceback for advanced users
- ✅ Handles complex, multi-line and multi-function programs

---

## 🧠 How It Works (High Level)

1. User pastes Python code into the UI
2. Code is executed in an isolated environment
3. A custom **execution tracer** hooks into Python’s runtime
4. When an exception occurs:
   - The exact failure frame is captured
   - Local variables and function context are frozen
5. An error analyzer maps the exception to:
   - Root cause explanation
   - Fix recommendation
6. Results are displayed via a clean web interface

---

## 🧩 Tech Stack

- **Language:** Python  
- **UI:** Streamlit  
- **Debugging:** `sys.settrace`, `traceback`  
- **Analysis:** Rule-based error reasoning  

No external APIs. No paid tools.

---

## 📁 Project Structurepython-debugging-assistant/
│
├── app.py # Streamlit UI
├── executor.py # Executes code and manages tracing
├── tracer.py # Execution tracing (core logic)
├── error_analyzer.py # Maps errors to explanations
├── error_rules.py # Error causes and fixes
├── requirements.txt

