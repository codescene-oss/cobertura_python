# run_coverage.py

import subprocess
import sys

def run_coverage():
    """Run tests with coverage and generate Cobertura XML report."""

    print("Running tests with coverage...\n")

    # Run coverage
    result = subprocess.run([
        sys.executable, "-m", "coverage", "run",
        "--source=./app/donkey,./app/monkey",
        "-m",
        "pytest"
    ])

    if result.returncode != 0:
        print("\n❌ Tests failed!")
        sys.exit(1)

    print("\n" + "="*50)
    print("Generating coverage report...")
    print("="*50 + "\n")

    # Generate terminal report
    subprocess.run([sys.executable, "-m", "coverage", "report", "-m"])

    # Generate HTML report
    subprocess.run([sys.executable, "-m", "coverage", "html"])
    print("\n📊 HTML coverage report generated in 'htmlcov/index.html'")

    # Generate Cobertura XML report
    subprocess.run([sys.executable, "-m", "coverage", "xml", "-o", "coverage.xml"])
    print("📄 Cobertura XML report generated as 'coverage.xml'")

    print("\n✅ Coverage analysis complete!")

if __name__ == "__main__":
    run_coverage()