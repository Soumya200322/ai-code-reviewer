from datetime import datetime


def generate_report(flake_result, complexity_result, suggestions, formatted_code):
    """
    Generate a detailed code analysis report.
    """

    report = []

    report.append("=" * 60)
    report.append("            AI CODE REVIEW REPORT")
    report.append("=" * 60)

    report.append(f"\nGenerated On : {datetime.now()}")
    report.append("\n")

    # -----------------------------------
    # Style Analysis
    # -----------------------------------
    report.append("=" * 60)
    report.append("1. STYLE ANALYSIS (FLAKE8)")
    report.append("=" * 60)

    if flake_result.strip():
        report.append(flake_result)
    else:
        report.append("No style issues found.")

    report.append("\n")

    # -----------------------------------
    # Complexity Analysis
    # -----------------------------------
    report.append("=" * 60)
    report.append("2. COMPLEXITY ANALYSIS (RADON)")
    report.append("=" * 60)

    report.append(complexity_result)

    report.append("\n")

    # -----------------------------------
    # Suggestions
    # -----------------------------------
    report.append("=" * 60)
    report.append("3. IMPROVEMENT SUGGESTIONS")
    report.append("=" * 60)

    if suggestions:
        for i, suggestion in enumerate(suggestions, start=1):
            report.append(f"{i}. {suggestion}")
    else:
        report.append("No suggestions.")

    report.append("\n")

    # -----------------------------------
    # Formatted Code
    # -----------------------------------
    report.append("=" * 60)
    report.append("4. FORMATTED CODE")
    report.append("=" * 60)

    report.append(formatted_code)

    report.append("\n")

    # -----------------------------------
    # Overall Score
    # -----------------------------------
    score = 100

    if flake_result.strip():
        score -= 20

    if "Average complexity: B" in complexity_result:
        score -= 10

    elif "Average complexity: C" in complexity_result:
        score -= 20

    elif "Average complexity: D" in complexity_result:
        score -= 30

    elif "Average complexity: E" in complexity_result:
        score -= 40

    elif "Average complexity: F" in complexity_result:
        score -= 50

    if score < 0:
        score = 0

    report.append("=" * 60)
    report.append("5. OVERALL CODE QUALITY SCORE")
    report.append("=" * 60)

    report.append(f"Score : {score}/100")

    if score >= 90:
        report.append("Excellent Code Quality ⭐⭐⭐⭐⭐")

    elif score >= 75:
        report.append("Good Code Quality ⭐⭐⭐⭐")

    elif score >= 60:
        report.append("Average Code Quality ⭐⭐⭐")

    else:
        report.append("Needs Improvement ⭐⭐")

    report.append("\n")
    report.append("=" * 60)
    report.append("End of Report")
    report.append("=" * 60)

    return "\n".join(report)