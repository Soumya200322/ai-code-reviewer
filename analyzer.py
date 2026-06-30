import subprocess


def analyze_code(file_path):
    """
    Analyze Python code using flake8.
    Returns style issues as a string.
    """

    try:
        result = subprocess.run(
            ["flake8", file_path],
            capture_output=True,
            text=True
        )

        if result.stdout:
            return result.stdout

        if result.stderr:
            return result.stderr

        return ""

    except FileNotFoundError:
        return "Error: flake8 is not installed. Install it using:\npip install flake8"

    except Exception as e:
        return f"Unexpected Error:\n{str(e)}"