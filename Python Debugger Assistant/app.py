import streamlit as st
from executor import execute_code
from error_analyzer import analyze_error

st.set_page_config(page_title="AI Python Debugging Assistant")

st.title("🧠 AI Python Debugging Assistant")
st.write("Now with execution tracing for complex code.")

code_input = st.text_area("✍️ Paste your Python code here", height=250)

if st.button("🔍 Analyze Code"):
    result = execute_code(code_input)

    if result["success"]:
        st.success(result["output"])
    else:
        analysis = analyze_error(result["error"], result.get("trace"))

        st.error("❌ Error Detected")

        st.subheader("📌 Error Type")
        st.write(analysis["error_type"])

        st.subheader("🧠 Why this happened")
        st.write(analysis["cause"])

        st.subheader("🛠️ How to fix it")
        st.write(analysis["fix"])

        if analysis["context"]:
            st.subheader("📍 Execution Context (At Crash Point)")
            st.write(f"**Function:** {analysis['context']['function']}")
            st.write(f"**Line Number:** {analysis['context']['line_no']}")
            st.write("**Local Variables:**")
            st.json(analysis["context"]["locals"])

