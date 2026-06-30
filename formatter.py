import subprocess
import tempfile
import os


def format_code(file_path):
    """
    Formats Python code using Black and returns the formatted code.
    """

    try:
        # Create a temporary copy of the file
        with open(file_path, "r", encoding="utf-8") as f:
            original_code = f.read()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".py",
            mode="w",
            encoding="utf-8"
        ) as temp_file:

            temp_file.write(original_code)
            temp_path = temp_file.name

        # Run Black formatter
        result = subprocess.run(
            ["black", "--quiet", temp_path],
            capture_output=True,
            text=True
        )

        # If formatting fails
        if result.returncode != 0:
            os.remove(temp_path)
            return f"Formatting Error:\n{result.stderr}"

        # Read formatted code
        with open(temp_path, "r", encoding="utf-8") as f:
            formatted_code = f.read()

        # Delete temporary file
        os.remove(temp_path)

        return formatted_code

    except FileNotFoundError:
        return (
            "Black is not installed.\n"
            "Run:\n"
            "pip install black"
        )

    except Exception as e:
        return f"Unexpected Error:\n{str(e)}"