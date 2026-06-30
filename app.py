import streamlit as st
import tempfile
import os

from analyzer import analyze_code
from formatter import format_code
from complexity import analyze_complexity
from report import generate_report

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Reviewer")
st.write("Analyze your Python code using flake8, Black, and Radon.")

st.sidebar.header("Upload Python File")

uploaded_file = st.sidebar.file_uploader(
    "Choose a Python file",
    type=["py"]
)

st.sidebar.write("OR")

manual_code = st.sidebar.text_area(
    "Paste Python Code",
    height=250
)

code = ""

# Read uploaded file
if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

elif manual_code.strip():
    code = manual_code

if code:

    st.subheader("📄 Source Code")

    st.code(code, language="python")

    if st.button("🔍 Analyze Code"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".py",
            mode="w",
            encoding="utf-8"
        ) as temp:

            temp.write(code)

            temp_file = temp.name

        st.success("File Loaded Successfully")

        # --------------------------
        # Flake8 Analysis
        # --------------------------

        st.header("📌 Style Analysis (flake8)")

        flake_result = analyze_code(temp_file)

        if flake_result.strip():

            st.text(flake_result)

        else:

            st.success("No Style Issues Found ✅")

        # --------------------------
        # Black Formatting
        # --------------------------

        st.header("🎨 Formatted Code (Black)")

        formatted = format_code(temp_file)

        st.code(formatted, language="python")

        # --------------------------
        # Radon Complexity
        # --------------------------

        st.header("📊 Code Complexity")

        complexity = analyze_complexity(temp_file)

        st.text(complexity)

        # --------------------------
        # Suggestions
        # --------------------------

        st.header("💡 Improvement Suggestions")

        suggestions = []

        if flake_result.strip():
            suggestions.append("✔ Fix PEP8 style issues.")

        if "Unused" in flake_result:
            suggestions.append("✔ Remove unused imports.")

        if "too long" in flake_result:
            suggestions.append("✔ Reduce line length.")

        if "Complexity" in complexity:
            suggestions.append("✔ Reduce function complexity.")

        if len(suggestions) == 0:
            suggestions.append("✔ Excellent! Your code follows good practices.")

        for item in suggestions:
            st.write(item)

        # --------------------------
        # Generate Report
        # --------------------------

        report = generate_report(
            flake_result,
            complexity,
            suggestions,
            formatted
        )

        st.header("📄 Analysis Report")

        st.text(report)

        st.download_button(
            label="⬇ Download Report",
            data=report,
            file_name="analysis_report.txt",
            mime="text/plain"
        )

        os.remove(temp_file)

else:

    st.info("Upload a Python file or paste code to begin.")