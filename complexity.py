import subprocess


def analyze_complexity(file_path):
    """
    Analyze cyclomatic complexity using Radon.
    Returns the complexity report as a string.
    """

    try:
        result = subprocess.run(
            ["radon", "cc", file_path, "-a"],
            capture_output=True,
            text=True
        )

        if result.stdout:
            return result.stdout

        if result.stderr:
            return result.stderr

        return "No complexity issues found."

    except FileNotFoundError:
        return (
            "Error: Radon is not installed.\n"
            "Install it using:\n"
            "pip install radon"
        )

    except Exception as e:
        return f"Unexpected Error:\n{str(e)}"